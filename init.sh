#!/usr/bin/env bash
sudo apt install ffmpeg
pip install youtube-dl
pip install -r /home/ryan0507/VoiceConversion/requirements.txt
cd /home/ryan0507/VoiceConversion/spleeter
pip install poetry
poetry install