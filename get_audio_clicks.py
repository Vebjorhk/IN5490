from pydub import AudioSegment
from pydub.generators import Sine
import simpleaudio as sa
import numpy as np

def get_audio_duration(file_path):
    audio = AudioSegment.from_file(file_path)
    duration_in_ms = len(audio)  # Duration in milliseconds
    duration_in_seconds = duration_in_ms / 1000.0  # Convert to seconds
    return duration_in_seconds

def calculate_click_times(bpm, duration_in_seconds):
     # Convert BPM to beats per second
    beats_per_second = bpm / 60.0
    
    # Calculate the interval between beats in milliseconds
    interval_ms = 1000 / beats_per_second
    
    # Calculate the number of beats (clicks) within the duration of the song
    num_beats = int(duration_in_seconds * beats_per_second)
    
    # Generate a list of times (in milliseconds) when each click occurs
    click_times_ms = [i * interval_ms for i in range(num_beats)]
    
    return click_times_ms

def generate_sine_wave(frequency, duration_ms, amplitude=-3.0):
    return Sine(frequency).to_audio_segment(duration=duration_ms, volume=amplitude)


def add_sine_wave_to_beats(song, beat_times, sine_wave):
    for beat_time in beat_times:
        song = song.overlay(sine_wave, position=beat_time)
    return song



# Example usage:
file_path = "audio/main-song.wav"  # Replace with your audio file path
duration = get_audio_duration(file_path)
bpm = 127

beat_times = calculate_click_times(bpm, duration)

song = AudioSegment.from_file("audio/main-song.wav")

# Generate the sine wave
frequency = 440  # Frequency in Hz (A4)
duration_ms = 100  # Duration in milliseconds
sine_wave = generate_sine_wave(frequency, duration_ms)


# Add the sine wave to the beats
song_with_sine = add_sine_wave_to_beats(song, beat_times, sine_wave)

# Save the modified song
song_with_sine.export("song_with_sine.wav", format="wav")


