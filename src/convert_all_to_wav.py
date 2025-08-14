# src/convert_all_to_wav.py
from pydub import AudioSegment
import os

assets_dir = "assets"
files = ["inhale.mp3", "hold.mp3", "exhale.mp3", "calm_music1.mp3"]

for file in files:
    path_in = os.path.join(assets_dir, file)
    path_out = os.path.join(assets_dir, file.replace(".mp3", ".wav"))
    if os.path.exists(path_in):
        AudioSegment.from_file(path_in).export(path_out, format="wav")
        print(f"{file} → {os.path.basename(path_out)}")
