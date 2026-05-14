"""
Empathy Engine – CLI Entry Point
Detects emotion in text and generates expressive, modulated speech audio.

Usage:
    python main.py
    python main.py --text "I just got promoted today!"
    python main.py --text "This is awful." --output sad_output.wav
    python main.py --voices   (list available system voices)
"""

import argparse
import os
import sys

from emotion_detector import detect_emotion
from tts_engine import speak_and_save, list_voices


BANNER = """
+--------------------------------------------------+
|           THE EMPATHY ENGINE                     |
|   Emotionally Expressive AI Voice Synthesizer    |
+--------------------------------------------------+
"""


def run_interactive():
    """Interactive CLI loop – keeps asking for input until the user quits."""
    print(BANNER)
    print("Type your text and press Enter. Type 'quit' or 'exit' to stop.\n")

    session = 1
    while True:
        text = input(">> Enter text: ").strip()
        if not text:
            continue
        if text.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        output_file = f"output_{session}.mp3"
        process(text, output_file)
        session += 1
        print()


def process(text: str, output_path: str):
    """Detect emotion, print results, and generate audio."""
    print("\n--- Analysing text ---")
    result = detect_emotion(text)

    print(f"  Text      : {text}")
    print(f"  Emotion   : {result['label']}")
    print(f"  Compound  : {result['compound']:.4f}")
    print(f"  Rate      : {result['rate']} wpm")
    print(f"  Volume    : {result['volume']:.2f}")
    print(f"\n  Generating audio → {output_path} ...")

    saved = speak_and_save(
        text=text,
        rate=result["rate"],
        volume=result["volume"],
        output_path=output_path,
    )

    print(f"  [OK] Audio saved to: {saved}")


def main():
    parser = argparse.ArgumentParser(
        description="Empathy Engine – Emotion-driven Text-to-Speech"
    )
    parser.add_argument(
        "--text", "-t",
        type=str,
        default=None,
        help="Text to synthesize (if omitted, runs in interactive mode).",
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="output.mp3",
        help="Output audio file path (default: output.mp3).",
    )
    parser.add_argument(
        "--voices",
        action="store_true",
        help="List available TTS voices on this system and exit.",
    )

    args = parser.parse_args()

    if args.voices:
        print("\nAvailable voices on this system:")
        for v in list_voices():
            print(f"  • {v['name']}")
            print(f"    ID: {v['id']}")
        sys.exit(0)

    if args.text:
        print(BANNER)
        process(args.text, args.output)
    else:
        run_interactive()


if __name__ == "__main__":
    main()
