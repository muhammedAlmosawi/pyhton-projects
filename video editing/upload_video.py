#well it was a great attempt but it didn't work
#if you are wondering why it failed
#it was because the video kept being locked as private 
#and I wasn't able to publish it 
#and I don't know why
#ok now I know why 
#it is because my 'app' wasn't verified by google
#so all its videos will be restricted to private viewing only

from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

CLIENT_SECRETS_FILE = r"video editing/client_secrets.json"

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    return build('youtube', 'v3', credentials=credentials)


def upload_video(youtube, file, title, description, category, tags, privacy_status):
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category
        },
        'status': {
            'privacyStatus': privacy_status
        }
    }

    media = MediaFileUpload(file, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress()) * 100}%")

    print(f"Video uploaded successfully. Video ID: {response['id']}")

if __name__ == '__main__':
    youtube = get_authenticated_service()
    try:
        upload_video(
            youtube,
            file=r"video editing/FinalVideo.mp4",  
            title="just some random video",
            description='why are you here',
            category='22',  
            tags=['tag1', 'tag2'],
            privacy_status='private'  
        )
    except RefreshError:
        print('The credentials have been revoked or expired, please re-run the application to re-authenticate.')