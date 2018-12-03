import json
import os
import sys
import random
import time

import spotipy
import spotipy.util as util


def get_env():
    spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID', None)
    spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', None)
    spotify_redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI', None)
    spotify_username = os.getenv('SPOTIFY_USERNAME', None)
    if spotify_client_secret is None:
        print('Specify SPOTIFY_CLIENT_SECRET as environment variable.')
        sys.exit(1)
    if spotify_client_id is None:
        print('Specify SPOTIFY_CLIENTID as environment variable.')
        sys.exit(1)
    if spotify_redirect_uri is None:
        print('Specify SPOTIFY_REDIRECT_URI as environment variable.')
        sys.exit(1)
    if spotify_username is None:
        print('Specify SPOTIFY_USERNAME as environment variable.')
        sys.exit(1)

    return spotify_client_secret, spotify_client_id, spotify_redirect_uri, spotify_username


def user_followed_list(sp):
    if os.path.exists('followed_list_.json'):
        artists = json.load(open('followed_list.json', 'r'))
    else:
        artists = []
        after = None
        while True:
            results = sp.current_user_followed_artists(limit=50, after=after)
            items = results['artists']['items']

            if not items:
                break
            for item in items:
                # print(item['name'])
                artists.append(item)

            after = items[-1]['id']
            time.sleep(0.1)
        json.dump(artists, open('followed_list.json', 'w'))

    return artists


def todays_artists():

    spotify_client_secret, spotify_client_id, spotify_redirect_uri, username = get_env()

    token = util.prompt_for_user_token(username, scope='user-follow-read',
                                       client_id=spotify_client_id,
                                       client_secret=spotify_client_secret,
                                       redirect_uri=spotify_redirect_uri)

    outputs = []

    if token:
        sp = spotipy.client.Spotify(auth=token)

        artists = user_followed_list(sp)

        selected_artist = random.choice(artists)

        recommendations = sp.recommendations(
            seed_artists=[selected_artist['id']])

        print("recommended albums related to {} are:".format(
            selected_artist['name']))

        recommended_artists = set([item['album']['artists'][0]['name']
                                   for item in recommendations['tracks']
                                   if item['album']['artists'][0]['name'] != selected_artist['name']])

        selected_recommended_artists = list(set(random.choices(
            list(recommended_artists), k=5)))

        for name in selected_recommended_artists:
            item = sp.search(q='artist:' + name,
                             type='artist')['artists']['items'][0]
            try:
                thumbnail_img_url = item['images'][0]['url']
            except:
                thumbnail_img_url = None
            link_url = item['external_urls']['spotify']
            outputs.append(
                {'name': name, 'thumbnail': thumbnail_img_url, 'link': link_url})

        print(outputs)
    else:
        print("Can't get token for", username)

    return outputs


def recommended_artists(artist):
    spotify_client_secret, spotify_client_id, _, _ = get_env()

    client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
        client_id=spotify_client_id, client_secret=spotify_client_secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q='artist:' + artist, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist_id = items[0]['id']

        recommended = sp.recommendations(
            seed_artists=[artist_id]
        )

        results = recommended['tracks'][0]['album']['external_urls']['spotify']
        print('how about this?: {}'.format(results))

        return results
    else:
        return None


if __name__ == '__main__':
    todays_artists()
