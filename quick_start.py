import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID', None)
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', None)

if spotify_client_secret is None:
    print('Specify SPOTIFY_CLIENT_SECRET as environment variable.')
    sys.exit(1)
if spotify_client_id is None:
    print('Specify SPOTIFY_CLIENTID as environment variable.')
    sys.exit(1)

client_credential_manager = SpotifyClientCredentials(
    spotify_client_id, spotify_client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credential_manager)

name = 'Smashing Pumpkins'
result = spotify.search(q='artist:' + name, type='artist')

for i in result['artists']['items']:
    print('{0} popularity: {1}'.format(i['name'], i['popularity']))

print('---')

artist_id = result['artists']['items'][0]['id']
result = spotify.artist_related_artists(artist_id)

for artist in result['artists']:
    artist_name = artist['name']
    popularity = artist['popularity']
    unique_id = artist['id']
    print('{0} - popularity: {1}, id: {2}'.format(artist_name,
                                                  popularity, unique_id))
