# 🎵📺 Spot2Tube - Spotify to YouTube Music 🎶🎥

Spot2Tube is a Python application that allows you to copy any publicly shared playlist from Spotify to YouTube Music. It uses the Spotify and YouTube APIs to retrieve and add songs to the respective playlists.

# Features ✨
1.🎵 Copy any publicly shared playlist from Spotify to YouTube Music.

2.🔑 Authenticate with YouTube Music using your Google Account (OAuth 2.0) to add songs to your private playlists (using Youtube Data API v3).

3.🎉 Create a new private playlist in YouTube Music or select from existing one and add the songs to it.

4.💻 Simple and easy-to-use command-line interface.

# Prerequisites 🛠️
To use Spot2Tube, you need the following:

1. 🔗 Clone or download the Spot2Tube repository from GitHub. To clone, go to your desired directory and run the following command: ```git clone https://github.com/Sidyboy-Codes/spot2tube.git``` in your terminal or command prompt.

2. 🐍 Python installed on your system (https://www.python.org/downloads/).

3. 🎶 Spotify Developer Credentials:
    * Create a Spotify Developer account at https://developer.spotify.com/dashboard/.
    * Get the `client_id` and `client_secret` from your Spotify Developer Dashboard and replace the empty strings in the code with these credentials.

4. 📲 Google Developer Credentials:

    * You need to create a project in the Google Developers Console (https://console.developers.google.com/).
    * Enable the YouTube Data API v3 for your project.
    * Create credentials for the project and download the `client_secrets.json` file.
    * Place the `client_secrets.json` file in the same directory as the Python script.
# Installation ⚙️

1.📝 Open the Python script (spot2tube.py) in a text editor and replace the `client_id` and `client_secret` in the Spotify section with your actual Spotify Developer credentials.

2.🗂️ Place th ` client_secrets.json` file, obtained from the Google Developer Credentials, in the same directory as the Python script.

3.💻 Install the required Python libraries using pip: ```pip install spotipy google-auth-oauthlib google-api-python-client youtube-search-python```

4.💾 Save the changes.

# How to Use 🚀
1.▶️ Run the Spot2Tube Python script (spot2tube.py).

2.🎵 You will be prompted to enter the Spotify playlist link (URL) you want to copy to YouTube Music.

3.🔄 The script will then retrieve the track information from the Spotify playlist and search for the corresponding YouTube videos for each track.

4.🤔 You will be asked if you want to add the songs to your current playlist in YouTube Music (Y/N). If you choose 'Y,' you will be provided with a list of your playlists to select from.

5.🎶 If you choose to add songs to your current playlist, the script will add the songs to the selected playlist.

6.➕ If you choose 'N' or if you want to create a new playlist, you will be prompted to enter the title for the new playlist. The script will create a new private playlist in YouTube Music and add the songs to it.

7.✅ The songs will be added to the playlist successfully, and the script will display a confirmation message.

# Future Improvements 🚧
Spot2Tube is currently at version 1 and might have some bugs. The current version is relatively simple and in the future will act as the backend for a public website that will allow anyone to use the app without needing Spotify and Google Developer accounts. The user will only need to provide access using their Google Account. Additionally, there are plans to implement the functionality to copy playlists from YouTube Music to Spotify.

--- 
📝 Please note that this project is for educational purposes and should be used responsibly and in compliance with the terms and conditions of Spotify and Google. 📚📝

## License
[MIT License](LICENSE)