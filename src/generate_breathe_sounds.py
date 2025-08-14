from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure assets folder exists
assets_dir = "assets"
os.makedirs(assets_dir, exist_ok=True)

def create_breath_sound(frequency, duration_ms, fade_in_ms, fade_out_ms, filename):
    """
    Generate a more natural breathing sound:
    - frequency: base pitch of tone
    - duration_ms: total duration in milliseconds
    - fade_in_ms / fade_out_ms: gradual increase/decrease to mimic breathing
    """
    tone = Sine(frequency).to_audio_segment(duration=duration_ms)
    
    if fade_in_ms > 0:
        tone = tone.fade_in(fade_in_ms)
    if fade_out_ms > 0:
        tone = tone.fade_out(fade_out_ms)
    
    tone.export(os.path.join(assets_dir, filename), format="mp3")
    print(f"{filename} created.")

# Generate inhale: soft rise
create_breath_sound(frequency=400, duration_ms=3000, fade_in_ms=1500, fade_out_ms=500, filename="inhale.mp3")

# Generate hold: very soft neutral tone (no fade)
create_breath_sound(frequency=300, duration_ms=2000, fade_in_ms=0, fade_out_ms=0, filename="hold.mp3")

# Generate exhale: soft release
create_breath_sound(frequency=200, duration_ms=3000, fade_in_ms=500, fade_out_ms=1500, filename="exhale.mp3")

print("\nAll breathing sounds generated in 'assets/' folder!")
