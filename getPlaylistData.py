#
# import argparse
# import pprint
# import sys
# import os
# import subprocess
# import json
# import spotipy
# import spotipy.util as util
# import pandas as pd
# import time
# from spotipy.oauth2 import SpotifyClientCredentials
#
#
# client_credentials_manager = SpotifyClientCredentials(client_id= "084866772c3e4a86a022b28acb4fe63a", client_secret= "084866772c3e4a86a022b28acb4fe63a")
#
#
# def show_tracks(tracks):
#     for i, item in enumerate(tracks['items']):
#         track = item['track']
#         print (" %d %s %s" % (i, track['artists'][0]['name'],track['name']))
#
# def get_track_features(track_id,sp):
#     if track_id is None:
#         return None
#     else:
#         features = sp.audio_features([track_id])
#     return features
#
# def get_features(tracks,sp):
#     tracks_with_features=[]
#
#     for track in tracks:
#         features = get_track_features(track['id'],sp)
#         print (track['name'])
#         if not features:
#             print("passing track %s" % track['name'])
#             pass
#         else:
#             f = features[0]
#             tracks_with_features.append(dict(
#                                             name=track['name'],
#                                             artist=track['artist'],
#                                             id=track['id'],
#                                             danceability=f['danceability'],
#                                             energy=f['energy'],
#                                             loudness=f['loudness'],
#                                             speechiness=f['speechiness'],
#                                             acousticness=f['acousticness'],
#                                             tempo=f['tempo'],
#                                             liveness=f['liveness'],
#                                             valence=f['valence']
#                                             ))
#
#         # time.sleep(0.1)
#
#     # print(tracks_with_features[0])
#     return tracks_with_features
#
# def get_tracks_from_playlists(username, sp):
#     playlists = sp.user_playlists(username)
#     trackList = []
#     for playlist in playlists['items']:
#         if playlist['owner']['id'] == username:
#             print (playlist['name'],' no. of tracks: ',playlist['tracks']['total'])
#             results = sp.user_playlist(username, playlist['id'],fields="tracks,next")
#             tracks = results['tracks']
#             for i, item in enumerate(tracks['items']):
#                 track = item['track']
#                 trackList.append(dict(name=track['name'], id=track['id'], artist=track['artists'][0]['name']))
#
#     # print(trackList[0])
#     return trackList
#
# def write_to_csv(track_features):
#     df = pd.DataFrame(track_features)
#     df.drop_duplicates(subset=['name','artist'])
#     print ('Total tracks in data set', len(df))
#     df.to_csv('mySongsDataset.csv',index=False)
#
# def main(username):
#     sp = spotipy.Spotify(auth_manager=client_credentials_manager)
#     print ("Getting user tracks from playlists")
#     tracks = get_tracks_from_playlists(username, sp)
#     print ("Getting track audio features")
#     tracks_with_features = get_features(tracks,sp)
#     print ("Storing into csv")
#     write_to_csv(tracks_with_features)
#
#
# if __name__ == '__main__':
#     print ('Starting...')
#     parser = argparse.ArgumentParser(description='this sript will grab user playlists')
#     parser.add_argument('--username', help='username')
#     args = parser.parse_args()
#     main(args.username)

# import spotipy
# import spotipy.util as util
# import pandas as pd
#
# CLIENT_ID = '9e6124af17514d6e834c3168ee74081d'
# CLIENT_SECRET = '1a95ffc314fa47c9847fd96634fb668e'
# token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# cache_token = token.get_access_token()
# sp = spotipy.Spotify(cache_token)
# # username=tpelr9ixp9xg8v12bk6epz4zh
# # playlist_id=2THc7FbUpd84Qsvv9Jvzgz
# sp.playlist_items("spotify", "tpelr9ixp9xg8v12bk6epz4zh")
#
# playlist_creator = "spotify"
# playlist_id = "2THc7FbUpd84Qsvv9Jvzgz"
#
#
# def analyze_playlist(playlist_creator, playlist_id):
#     # Create empty dataframe
#     playlist_features_list = ["Artist", "Album", "Song.Name", "Song.ID", "Danceability", "Energy", "Key", "Loudness",
#                               "mode", "Speechiness", "Acousticness", "Liveness", "Valence", "Tempo", "duration_ms",
#                               "time_signature"]
#
#     playlist_df = pd.DataFrame(columns=playlist_features_list)
#
#     # Loop through every track in the playlist, extract features and append the features to the playlist df
#
#     playlist = sp.playlist_items(playlist_id)["items"]
#     for track in playlist:
#         # Create empty dict
#         playlist_features = {}
#         # Get metadata
#         playlist_features["Artist"] = track["track"]["album"]["artists"][0]["name"]
#         playlist_features["Album"] = track["track"]["album"]["name"]
#         playlist_features["Song.Name"] = track["track"]["name"]
#         playlist_features["Song.ID"] = track["track"]["id"]
#
#         # Get audio features
#         audio_features = sp.audio_features(playlist_features["track_id"])[0]
#         for feature in playlist_features_list[4:]:
#             playlist_features[feature] = audio_features[feature]
#
#         # Concat the dfs
#         track_df = pd.DataFrame(playlist_features, index=[0])
#         playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)
#
#     return playlist_df
#
#
# df = analyze_playlist(playlist_creator, playlist_id)
# df.to_csv("spotify_df.csv", index=False)

# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="9e6124af17514d6e834c3168ee74081d", client_secret="1a95ffc314fa47c9847fd96634fb668e"))
#
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
#
import sys
import spotipy
import spotipy.util as util

username='xxx'
CLIENT_ID = '9e6124af17514d6e834c3168ee74081d'
CLIENT_SECRET = '1a95ffc314fa47c9847fd96634fb668e'

redirecturi='http://localhost'
thescope='playlist-read-private'
token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=thescope, redirecturi= redirecturi )
cache_token = token.get_access_token()
sp = spotipy.Spotify(cache_token)
if token:
 sp = spotipy.Spotify(auth=token)
 playlists = sp.current_user_playlists()
 while playlists:
     for i, playlist in enumerate(playlists['items']):
         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
     if playlists['next']:
         print("getting next 50")
         playlists = sp.next(playlists)
     else:
         playlists = None
else:
 print ("Can't get token for", username)