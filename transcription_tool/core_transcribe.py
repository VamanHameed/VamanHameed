"""Core utilities for audio recording and transcription."""

import tempfile
from pathlib import Path

import numpy as np
import sounddevice as sd
import whisper


DEFAULT_SAMPLE_RATE = 16000


def record_audio(duration: int = 5, samplerate: int = DEFAULT_SAMPLE_RATE) -> np.ndarray:
    """Record audio from the default microphone."""
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    return np.squeeze(audio)


def _save_temp_audio(audio: np.ndarray, samplerate: int) -> Path:
    """Store audio data to a temporary WAV file and return its path."""
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    try:
        whisper.audio.write_audio(tmp.name, audio, samplerate)
    finally:
        tmp.close()
    return Path(tmp.name)


def transcribe_audio(audio: np.ndarray, model_name: str = "base") -> str:
    """Transcribe an in-memory numpy array."""
    model = whisper.load_model(model_name)
    tmp_file = _save_temp_audio(audio, DEFAULT_SAMPLE_RATE)
    try:
        result = model.transcribe(str(tmp_file))
    finally:
        tmp_file.unlink(missing_ok=True)
    return result["text"].strip()


def transcribe_file(path: str, model_name: str = "base") -> str:
    """Transcribe an existing audio file."""
    model = whisper.load_model(model_name)
    result = model.transcribe(path)
    return result["text"].strip()
