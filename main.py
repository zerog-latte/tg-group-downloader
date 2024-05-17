import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

load_dotenv()

api_id = os.getenv('APP_API_ID')
api_hash = os.getenv('APP_API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
group_id = os.getenv('GROUP_ID')
output_dir = f"{os.getenv('OUTPUT_DIR')}/".replace('//', '/')
message_limit = os.getenv('MESSAGE_LIMIT')

with TelegramClient('anon', api_id, api_hash) as client:
  # Authenticate
  client.connect()
  if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

  # Get the group entity
  entity = client.get_entity(int(group_id))

  # Fetch group messages
  messages = client.get_messages(entity, limit=10)

  # Iterate through messages
  for message in messages:
    # Check if the message contains media (photo or video)
    if message.media:
      if isinstance(message.media, MessageMediaPhoto):
        # Get photo details
        file_name = f"{message.id}.jpg"
        file_path = output_dir + file_name
        try:
          media_size = message.media.photo.sizes[-1].sizes[-1]
          media_size = round(media_size / 1024**2, 2)
        except Exception:
          media_size = -1
        # Check if file exists
        if os.path.exists(file_path):
          print(f"{file_name} already exists. Skipping...")
          continue
        # Output filename and media size
        print(f"Downloading {file_name} ({media_size} Mb) ...", end='')

        # Download and save photo
        client.download_media(message, file_path)
        print(" DONE")
      elif isinstance(message.media, MessageMediaDocument):
        # Check if the document is a video
        if message.media.document.mime_type.split('/')[0] == 'video':
          # Get video details
          file_name = f"{message.id}.mp4"
          file_path = output_dir + file_name
          try:
            media_size = message.media.document.size
            media_size = round(media_size / 1024**2, 2)
          except Exception:
            media_size = 0
          if os.path.exists(file_path):
            print(f"{file_name} already exists. Skipping...")
            continue
          # Output filename and media size
          print(f"Downloading {file_name} ({media_size} Mb) ...", end='')

          # Download and save video
          client.download_media(message, file_path)
          print(" DONE")
