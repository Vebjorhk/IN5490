import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

audio_file = 'audio/SONIKKU - Sweat ft. LIZ (SOPHIE Remix) [Official Audio] epilepsy warning.mp3'

# Load the audio file
audio, sr = librosa.load(audio_file, sr=44100)

start_time = 80.0
end_time = 140.0

start_sample = int(start_time * sr)
end_sample = int(end_time * sr)

trimmed_audio = audio[start_sample:end_sample]
sf.write("./audio/trimmed_audio_3.mp3", trimmed_audio, sr)