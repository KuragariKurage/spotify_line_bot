# Spotify recommendation bot for LINE

アーティスト名は知ってるけど何から聞いたらいいかわからない時に役立ちそうなBot.

<img src="demo.gif" width=30%>

## how to use

Set your api keys as environment variables.

- [Spotify Web API](https://developer.spotify.com/dashboard/login)
    - SPOTIFY_CLIENT_ID
    - SPOTIFY_CLIENT_SECRET
    - optional (SPOTIFY_REDIRECT_URL)
    - optional (SPOTIFY_USERNAME)
- [LINE](https://developers.line.biz/ja/services/messaging-api/)
    - YOUR_CHANNEL_ACCESS_TOKEN
    - YOUR_CHANNEL_SECRET

Run

```bash:
python bot.py
```

## reference

- [HerokuでLINE BOT(python)を動かしてみた](https://qiita.com/akabei/items/38f974716f194afea4a5)
- [Spotify APIで遊んでみる](https://qiita.com/musiccoffeetea/items/69a58d6d66e42b3c113f)