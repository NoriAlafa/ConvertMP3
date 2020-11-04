
import pafy


url = input("Masukkan link youtube")
video.pafy = pafy.new(url)

audios = video.getbestaudio()
audio.download