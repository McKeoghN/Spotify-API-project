import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import numpy as np
import time
import Constants

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Constants.cid, \
                                               client_secret=Constants.secret, \
                                               redirect_uri=Constants.redirect_uri, \
                                               scope=Constants.scope))


def create_new_playlist(tracks, playlist_name):
    # Need to change it so my Spotify username isn't public
    new_playlist = spotify.user_playlist_create('mckeoghn', 'Slaylistified ' + playlist_name)
    playlist_id = new_playlist['id']
    spotify.playlist_add_items(playlist_id, tracks)


def get_playlist_tracks(playlist_id):
    results = spotify.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks


def get_playlist_bpms(playlist_id):
    playlist_songs = get_playlist_tracks(playlist_id)
    s_names = []
    for i in enumerate(playlist_songs):
        try:  # Exception to skip Podcasts in playlists
            s_names.append([i[1]['track']['name'], i[1]['track']['id'],
                            spotify.audio_analysis(i[1]['track']['id'])['track']['tempo']])
        except spotipy.exceptions.SpotifyException:
            pass
    return s_names


def get_user_playlists():  # Get the users 100 newest playlists
    playlists = spotify.current_user_playlists(limit=100, offset=0)
    p_names = []
    for i in enumerate(playlists['items']):
        p_names.append([i[1]['name'], i[1]['id']])
    return p_names


def main():
    p_names = get_user_playlists()
    numPlaylists = len(p_names)
    for i in range(numPlaylists):
        print(i+1, p_names[i][0])
    print('\n')

    # Error handling for non integer inputs:
    try:  
        # User input to select a playlist:
        playlist_input = int(input('What playlist do you want Slaylistified?'))  
    except ValueError:
        print("\nIncorrect input, try again.\n")
        time.sleep(0.5)
        main()

    # Error handling for invalid integer inputs:
    if playlist_input > numPlaylists or playlist_input <= 0:  
        print("\nIncorrect input, try again.\n")
        time.sleep(0.5)
        main()
    
    s_names = sorted(s_names, key=lambda x: x[2])
    pprint(s_names)
    print('\n')
    np_s_names = np.array(s_names)
    create_new_playlist(np_s_names[:,1], p_names[playlist_input-1][0])


if __name__ == '__main__':
    main()