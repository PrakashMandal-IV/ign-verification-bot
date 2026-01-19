# IGN Discord Bot (v2)

Automatically sets a user's nickname based on their IGN and removes the Unverified role.

## Features
- Listens to a specific channel
- Validates IGN format
- Deletes IGN message for privacy
- Sets nickname
- Removes Unverified role
- Sends DM confirmation

## Setup
1. Python 3.10+
2. pip install -r requirements.txt
3. Create .env from .env.example
4. python bot.py

## Required Bot Permissions
- Manage Nicknames
- Manage Roles
- Manage Messages
- Read Messages
- Send Messages

## Notes
- Bot role must be ABOVE the Unverified role
