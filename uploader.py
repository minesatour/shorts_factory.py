from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config import HASHTAGS, CATEGORY_ID

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_client():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=creds)

def upload(youtube, path, title):
    req = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title[:100],
                "description": title,
                "tags": HASHTAGS,
                "categoryId": CATEGORY_ID
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(path)
    )
    req.execute()
