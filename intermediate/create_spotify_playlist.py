import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_billboard = "1997-06-20"
URL = f"https://www.billboard.com/charts/hot-100/{date_billboard}"
response = requests.get(URL).text
soup = BeautifulSoup(response, features="html.parser")
titles_tags = soup.select("li ul li h3")
artists_tags = soup.select("li ul li span a")
titles = [title.get_text().strip() for title in titles_tags]
artists = [artist.get_text().strip() for artist in artists_tags]
# print(titles)
# print(artists)
billboard_day_mix = [f"{title} - {artist}" for title, artist in zip(titles, artists)]
print(billboard_day_mix)


# https://developer.spotify.com/dashboard/
# Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.
# Spotify uses OAuth to allow third-party applications (e.g. our Python code) to access a Spotify user's account without giving them the username or password.
# Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username).
# As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.
# You need the "playlist-modify-private" scope in order to create a private playlist on Spotify.
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR UNIQUE CLIENT ID",
        client_secret="YOUR UNIQUE CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR SPOTIFY DISPLAY NAME",)
    )

song_uris = []
user_id = sp.current_user()["id"]
year = date_billboard.split("-")[0]
for song in billboard_day_mix:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_billboard} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)