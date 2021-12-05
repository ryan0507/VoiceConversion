#!/usr/bin/env bash
sudo apt-get update
sudo apt install ffmpeg
pip install youtube-dl
cd /home/ryan0507/VoiceConversion/spleeter
pip install poetry
poetry install
pip install -r /home/ryan0507/VoiceConversion/requirements.txt