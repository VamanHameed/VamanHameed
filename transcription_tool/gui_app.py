"""Simple PyQt5 GUI for the transcription tool."""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

from .core_transcribe import record_audio, transcribe_audio


class TranscriberGUI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Transcription App")
        self.text_area = QTextEdit()
        self.record_btn = QPushButton("Record")
        self.record_btn.clicked.connect(self.handle_record)

        layout = QVBoxLayout()
        layout.addWidget(self.record_btn)
        layout.addWidget(self.text_area)
        self.setLayout(layout)

    def handle_record(self) -> None:
        audio = record_audio()
        text = transcribe_audio(audio)
        self.text_area.setPlainText(text)


def main() -> None:
    app = QApplication(sys.argv)
    gui = TranscriberGUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
