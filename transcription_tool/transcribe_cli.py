"""Command line interface for the transcription tool."""

import argparse

from .core_transcribe import record_audio, transcribe_audio, transcribe_file


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI transcription tool")
    parser.add_argument("--duration", type=int, default=5, help="Record duration in seconds")
    parser.add_argument("--file", type=str, help="Transcribe an existing audio file")
    parser.add_argument("--model", type=str, default="base", help="Whisper model size")
    args = parser.parse_args()

    if args.file:
        text = transcribe_file(args.file, model_name=args.model)
    else:
        audio = record_audio(duration=args.duration)
        text = transcribe_audio(audio, model_name=args.model)

    print("Transcription:\n" + text)


if __name__ == "__main__":
    main()
