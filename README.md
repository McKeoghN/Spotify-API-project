# Spotify-API-project
## 2025 Update
This was a fun little project I made to be able to sort a playlist in a way in which songs flow between each other better, almost as if played by a DJ. However, this no longer works because Spotify has changed their API so it no longer allows developers to use any of the interesting endpoints - the main one being "audio analysis" which provided songs bpm's which was vital for this project as the playlists were sorted by BPM. This is silly! Non-commercial and small projects such as this one should be allowed some kind of access to these parts of the Spotify API.
## Set up instructions
For this code to work you to generate a client id and client secret and store them, as well as your Spotify username, in a python file called Constants.py. Store this python file in the same folder that you save Main.py in.
You can generate a client id and client secret by following the instructions on this page: https://developer.spotify.com/documentation/web-api/concepts/apps

Store the client id, client secret and your Spotify username in the following formatin the Constants.py file:

cid = '[client id from developers.spotify.com]'

secret = '[client secret from developers.spotify.com]'

username = '[your Spotify username]'


The redirect_uri can be easily changed in the Main.py file if you wish to use a different one.