from trends import get_best_trending_topic
from script_gen import generate_variations
from voiceover import generate_voice
from video_builder import build_video
from uploader import get_client, upload
from scheduler import wait
from analytics import log

def run():
    topic = get_best_trending_topic()
    scripts = generate_variations(topic)
    yt = get_client()

    for i, script in enumerate(scripts):
        voice = f"output/voice_{i}.mp3"
        video = f"output/final_videos/short_{i}.mp4"

        generate_voice(script, voice)
        build_video(voice, video, script)
        upload(yt, video, topic)
        log(topic, script[:60])
        wait(i)

if __name__ == "__main__":
    run()
