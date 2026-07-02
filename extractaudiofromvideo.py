from moviepy import VideoFileClip
video=VideoFileClip("videoplayback.mp4")
audio=video.audio
audio.write_audiofile("extract_audio.mp3")
