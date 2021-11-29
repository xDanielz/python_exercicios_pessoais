from pytube import YouTube
import string
import moviepy
import moviepy.editor
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import os


class YtbDownloader:
    @staticmethod
    def download_video(url, savelocal=None):
        if savelocal is None:
            savelocal = os.path.dirname(os.path.realpath(__file__))
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(savelocal)

    def download_and_convertmp3(self, url, savelocal=None):
        if savelocal is None:
            savelocal = os.path.dirname(os.path.realpath(__file__))
        self.download_video(url, savelocal)
        filename = title_suit(YouTube(url).title)
        os.chdir(savelocal)
        try:
            video = moviepy.editor.VideoFileClip(savelocal+'/'+filename+'.mp4')
            audio = video.audio
            audio.write_audiofile(filename + '.mp3')
        except:
            print(filename)
        else:
            video.close()
            audio.close()
            os.remove(filename+'.mp4')

    def download_playlist(self, url, savelocal=None, tomp3=False):
        p = Playlist(url)
        if savelocal is None:
            savelocal = os.path.dirname(os.path.realpath(__file__))
        for u in p:
            try:
                if tomp3:
                    self.download_and_convertmp3(u, savelocal)
                else:
                    self.download_video(u, savelocal)
            except Exception as exc:
                print(exc)
                continue


class Playlist:
    def __init__(self, playlist_url):
        url = playlist_url
        query = parse_qs(urlparse(url).query, keep_blank_values=True)
        playlist_id = query[b"list"][0]
        youtube = googleapiclient.discovery.build("youtube", "v3",
                                                  developerKey="AIzaSyC474bkrVTilDLpHrbOzMnueAuJs9_aMi0")
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id
        )
        response = request.execute()
        playlist_items = []
        while request is not None:
            response = request.execute()
            playlist_items += response["items"]
            request = youtube.playlistItems().list_next(request, response)
        self.urls = [f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
                     for t in playlist_items]

    def __len__(self):
        return len(self.urls)

    def __iter__(self):
        return iter(self.urls)


def title_suit(title: str) -> str:
    punctuation = str.maketrans({}.fromkeys(string.punctuation, ''))
    return title.translate(punctuation)
