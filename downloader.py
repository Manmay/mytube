from pytube import YouTube;


class Downloader:
    def __init__(self, target):
        self._target = target

    def download(self, url):
        print("Downloading : " + url)
        youtube = YouTube(url)
        video = youtube.filter('mp4')[-1]
        video.download(self._target)
        print("Downloaded : " + url)
