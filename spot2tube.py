
# Copyright (c) 2023 Siddhant Nitin Patel
# Spot2Tube
# All Rights Reserved.
 
# spotify libs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# google libs
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from youtube_search import YoutubeSearch


message = "** Welcome to Spot2Tube by Sidyboy **"
border = '*' * (len(message))
print(border)
print(f'{message}')
print(border)



# ----------------------- spotify ----------------------------------------------------------------

# developer credentials (spotify developer mode: https://developer.spotify.com/dashboard/)
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Spotify credentials manager
ccm = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# creating spotify instance with credentials, so that app can be authenticated while accessing data from spotify API
sp = spotipy.Spotify(client_credentials_manager=ccm)



# a function to get spotify playlist id from an public shared url of spotify playlist
def get_playlist_id(pl_url):
    parts = pl_url.split('/')
    for i in range(len(parts)):
        if parts[i] == 'playlist':
            return parts[i+1].split('?')[0]
    return None

pl_url = input("Please enter playlist link >> ")
playlist_id = get_playlist_id(pl_url)


# Retrieving data from playlist_id which was provided previously
results = sp.playlist(playlist_id, fields="tracks")
tracks = results['tracks']['items']

songs = []

# Iterating from the list of tracks we got and extracting necessary data which is required to pass to youtube data api v3
for track in tracks:
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    album_name = track['track']['album']['name']
    
    # getting each track info and appending it to songs array
    # example of data: coca white by xyz official (this string will be searched in the future using youtube search module)
    songs.append(f"{track_name} by {artist_name} official")


# ---------------------------- Google ---------------------------------------------------------

# Set up the OAuth 2.0 credentials
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
# request using http instead of https
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Only for development purposes
api_service_name = "youtube"
api_version = "v3"

# client_secrete should be encrypted
client_secrets_file = "<PATH to your client_secret json file>"
# example
# client_secrets_file = "client_secrets.json"


youtube = None

# Authenticating the user and storing it, so that user dont need to be authenticated again and again for future function call
def authenticate():
    global youtube
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file( 
        client_secrets_file, scopes
    )
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)


def get_numbered_playlists():
    request = youtube.playlists().list(
        part='snippet',
        mine=True,
    )

    response = request.execute()
    playlists = response['items']

    # Iterate over the playlists and number them
    numbered_playlists = [(i+1, playlist['snippet']['title'], playlist['id']) for i, playlist in enumerate(playlists)]

    return numbered_playlists

# This function will create a new playlist in YouTube Music
def create_playlist(title):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "Playlist created using spot2tube, an app by Sidyboy",
            },
            "status": {"privacyStatus": "private"},
        },
    )
    response = request.execute()
    return response["id"]

# Search for songs and add them to the playlist
def add_songs_to_playlist(playlist_id, songs):
    for song in songs:
        results = YoutubeSearch(song, max_results=1).to_dict()
        if results:
            video_id = results[0]["id"]
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "position": 0,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id,
                        },
                    },
                },
            )
            request.execute()

# Check if the YouTube service is already authenticated if not authenticate first
if youtube is None:
    authenticate()

# user want to add songs to current playlist or want to create new
my_playlists = input("Want to add songs to your current playlist? (Y/N) >> ").lower()

# checking for valid input
while my_playlists not in ["y", "n"]:
    print("Please select a valid input.")
    my_playlists = input("Want to add songs to your current playlist? (Y/N) >> ").lower()


# add song to user's current playlist
def add_to_current_playlist():
    # get user's current playlist with number at front, so user can select playlist number
    numbered_playlists = get_numbered_playlists()
    
    # printing playlists  
    for number, playlist_name, playlist_id in numbered_playlists:
        print(f"{number}. {playlist_name} - {playlist_id}")

# selected playlist in which user wants to add/copy songs from spotify playlist
    selected_playlist = numbered_playlists[int(input("enter the number of the playlist >> "))-1][2] #playlist_id is at index 2. Example numbered_playlist[0][2] - gets id of playlist at 1
    add_songs_to_playlist(selected_playlist, songs)

# user wants to create a new playlist
def add_to_new_playlist():
    playlist_title = input("Creating new, enter the playlist title >> ")
    playlist_id = create_playlist(playlist_title)
    add_songs_to_playlist(playlist_id, songs)

if my_playlists == "y":
    add_to_current_playlist()   
else:
    add_to_new_playlist()

print("Songs added to the playlist successfully! Thank you for using Spot2Tube")
