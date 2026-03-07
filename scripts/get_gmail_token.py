"""
One-time local script to obtain Gmail OAuth2 refresh_token.

Prerequisites:
  1. Go to https://console.cloud.google.com/
  2. Create a project (or select existing)
  3. Enable Gmail API: APIs & Services → Library → search "Gmail API" → Enable
  4. Create OAuth credentials:
     - APIs & Services → Credentials → Create Credentials → OAuth client ID
     - Application type: "Desktop app"
     - Download the JSON file as 'client_secret.json' in this directory
  5. Configure OAuth consent screen:
     - APIs & Services → OAuth consent screen
     - Add test user: your Gmail address (hudejun2002@gmail.com)
     - Scopes: add gmail.readonly and gmail.send

Usage:
  pip install google-auth-oauthlib
  python scripts/get_gmail_token.py

Output:
  Prints the GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, and GMAIL_REFRESH_TOKEN
  to copy into GitHub Secrets.
"""
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

def main():
    # Load the client secret JSON downloaded from Google Cloud Console
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)

    # This opens a browser for authorization
    creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")

    # Read client_secret.json to extract client_id and client_secret
    with open("client_secret.json") as f:
        secret = json.load(f)
    client_info = secret.get("installed") or secret.get("web")

    print("\n" + "=" * 60)
    print("✅ Authorization successful! Copy these to GitHub Secrets:")
    print("=" * 60)
    print(f"\nGMAIL_CLIENT_ID:\n{client_info['client_id']}")
    print(f"\nGMAIL_CLIENT_SECRET:\n{client_info['client_secret']}")
    print(f"\nGMAIL_REFRESH_TOKEN:\n{creds.refresh_token}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
