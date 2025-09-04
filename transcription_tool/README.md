# Transcription Tool

A minimal transcription utility that provides both a command-line interface and a PyQt5-based GUI. It relies on OpenAI's Whisper model for speech recognition.

## CLI

Run from the repository root:

```bash
python -m transcription_tool.transcribe_cli --duration 5
```

Provide an existing file instead of recording:

```bash
python -m transcription_tool.transcribe_cli --file path/to/audio.wav
```

## GUI

Launch the GUI application:

```bash
python -m transcription_tool.gui_app
```

Dependencies include `whisper`, `sounddevice`, and `PyQt5`.
