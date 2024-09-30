# audio_helper.py
import pyaudio
import wave
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI client
openai.api_key = os.getenv('OPENAI_API_KEY')

# Audio recording settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = "output.wav"


def record_audio():
    """Record audio from the microphone and save it to a file."""
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = [stream.read(CHUNK) for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS))]

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    save_audio_to_file(frames, audio)

    return OUTPUT_FILENAME


def save_audio_to_file(frames, audio):
    """Save recorded audio frames to a WAV file."""
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))


def transcribe_audio(file_path):
    """Transcribe audio file using OpenAI's Whisper model."""
    try:
        with open(file_path, "rb") as audio_file:
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
        return transcription['text']
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


if __name__ == "__main__":
    audio_file = record_audio()
    transcription = transcribe_audio(audio_file)
    if transcription:
        print(f"Transcription: {transcription}")
    else:
        print("Transcription failed.")