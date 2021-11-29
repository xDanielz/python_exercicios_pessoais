from pytube import YouTube, Playlist


def download_video(video_url):
    yt = YouTube(video_url)
    video = yt.streams.first()
    video = yt.streams.get_lowest_resolution()
    video.download()


playlist = Playlist("https://www.youtube.com/playlist?list=PL4o29bINVT4Fa-_LPeMI6ON3xTjqE4yrX")
for url in playlist:
    try:
        print(url)
    except:
        continue
