from moviepy.editor import *
import os, random
from retention import is_keyword

def build_video(voice_path, output_path, script):
    bg = random.choice(os.listdir("assets/bg_videos"))
    music = random.choice(os.listdir("assets/music"))

    bg_clip = VideoFileClip(f"assets/bg_videos/{bg}").resize((1080,1920))
    voice = AudioFileClip(voice_path)
    music = AudioFileClip(f"assets/music/{music}").volumex(0.08)

    duration = voice.duration
    bg_clip = bg_clip.subclip(0, duration)
    music = music.subclip(0, duration)

    bg_clip = bg_clip.set_audio(CompositeAudioClip([voice, music]))

    words = script.replace("\n"," ").split()
    word_time = duration / len(words)

    captions = []
    t = 0
    for w in words:
        color = "yellow" if is_keyword(w) else "white"
        txt = TextClip(
            w.upper(),
            fontsize=95,
            color=color,
            stroke_color="black",
            stroke_width=3
        ).set_position("center").set_start(t).set_duration(word_time*1.05)
        captions.append(txt)
        t += word_time

    final = CompositeVideoClip([bg_clip, *captions])
    final.write_videofile(output_path, fps=30, codec="libx264", audio_codec="aac")
