# TODO: select specific song to run
# TODO: lookup on spotify
import json
import spotipy
import webbrowser
  
username = 'leomyth123@gmail.com'
clientID = '28493365acaf4b1eaa86768eb221a7a2'
clientSecret = '6babca25098a4a30bdc6b9dc32463cc8'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  
# To print the JSON response from 
# browser in a readable format.
# optional can be removed
print(json.dumps(user_name, sort_keys=True, indent=4))

def playSong(search_song):
    results = spotifyObject.search(search_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)

playSong("I Wanna Cry Seori")