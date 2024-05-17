# Telegram Group Media Downloader

This script allows you to download photos and videos from a Telegram group. It uses the Telethon library to connect to Telegram and fetch messages containing media attachments (photos or videos) from the specified group. The downloaded media files are saved to a local directory.

## Basic Usage

Ensure that you have the necessary permissions to access the group and that your Telegram API credentials are correctly configured in the .env file.

The script will connect to Telegram, authenticate using your phone number, and fetch the latest messages from the specified group. It will then iterate through each message and download any photos or videos attached to the message.

1. Clone the repository:
`git clone https://github.com/zerog-latte/tg-group-downloader.git`

2. Navigate to the cloned repository: `cd tg-group-downloader`

2. Install the required Python packages: `pip install -r requirements.txt`

1. Create a .env file in the project directory and configure it with your Telegram API credentials and other settings. See the example .env file provided.

2. Run the main.py script: `python main.py`

## Installation

### Windows
To run the script on Windows, you can create a start.ps1 script with the following content or run it directly in the PowerShell console:

```powershell
# Check if Python 3.12 is installed
if (!(Test-Path "C:\Python312")) {
    # Download Python 3.12 installer
    Invoke-WebRequest "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" -OutFile "python-3.12.0-amd64.exe"

    # Install Python 3.12
    Start-Process -FilePath "python-3.12.0-amd64.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item "python-3.12.0-amd64.exe"
}
git clone https://github.com/zerog-latte/tg-group-downloader.git
cd tg-group-downloader
# Install required Python packages
pip install -r requirements.txt

# Run the main.py script
python main.py
```

### Linux
To run the script on Linux, you can create a start.sh script with the following content or run it directly in the Bash console:
```bash
#!/bin/bash

# Check if Python 3.12 is installed
if ! command -v python3.12 &> /dev/null; then
    # Install dependencies
    sudo apt-get update
    sudo apt-get install -y software-properties-common

    # Add deadsnakes PPA for Python 3.12
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt-get update

    # Install Python 3.12
    sudo apt-get install -y python3.12
fi

# Install pip for Python 3.12
sudo apt-get install -y python3.12-distutils
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.12 get-pip.py

git clone https://github.com/zerog-latte/tg-group-downloader.git
cd tg-group-downloader
# Install required Python packages
pip install -r requirements.txt

# Run the main.py script
python3.12 main.py
```

### MacOS
```bash
#!/bin/bash

# Check if Python 3.12 is installed
if ! command -v python3.12 &> /dev/null; then
    # Install Homebrew if not already installed
    if ! command -v brew &> /dev/null; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    # Install Python 3.12
    brew install python@3.12
fi

# Install pip for Python 3.12
curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.12 get-pip.py

git clone https://github.com/zerog-latte/tg-group-downloader.git
cd tg-group-downloader
# Install required Python packages
pip install -r requirements.txt

# Run the main.py script
python3.12 main.py
```


## Example .env file:
```
OUTPUT_DIR=./output/
APP_API_ID=12345
APP_API_HASH=12345
PHONE_NUMBER='+91XXXXXXXXXX'
GROUP_ID=-100000000000
MESSAGE_LIMIT=1000
```

Make sure to replace the placeholder values with your actual Telegram API credentials and group ID.

## How to Obtain API ID and API Hash

To use the Telegram API, you need to create a Telegram application and obtain the API ID and API hash. Here's how you can do it:

1. Go to the Telegram API website: [https://my.telegram.org/auth](https://my.telegram.org/auth).

2. Log in with your Telegram account.

3. Once logged in, click on "API development tools" and then "Create application".

4. Fill in the required details for your application (name, description, etc.) and submit the form.

5. After creating the application, you will be provided with the API ID and API hash. Copy these values and paste them into your .env file.

## Note

This script assumes that you have already set up a Telegram application and obtained the necessary API credentials. If you haven't done so, you can create a new application on the Telegram API website (https://my.telegram.org/auth) and obtain the API ID and hash.
