from pytube import YouTube

SAVE_PATH = "./audio"
video_link = "https://www.youtube.com/watch?v=bDAyquF-BrQ"

# Retrieve YouTube video
try:
    yt = YouTube(video_link)
    print(f"Retrieved youtube video: {yt.title}")
except:
    print('Error: Unable to retrieve video')

# Download audio
try:
    audio = yt.streams.get_audio_only()
    audio.download(output_path=SAVE_PATH, filename='yt_audio1.mp3')
    print('Successfully downloaded audio file')
except Exception as e:
    print(e)


