try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Some modules are Missing {}".format(e))


url = "https://www.youtube.com/watch?v=UiRpVX8s6lI"
ytd = YouTube(url).streams.first().download()
print(ytd)
