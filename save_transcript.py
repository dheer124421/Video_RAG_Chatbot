import json
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "Rni7Fz7208c"

ytt_api = YouTubeTranscriptApi()

transcript = ytt_api.fetch(video_id)

data = []

for item in transcript:
    data.append({
        "text": item.text,
        "start": item.start,
        "end": item.start + item.duration
    })

with open(
    "transcript.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        data,
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"Saved {len(data)} transcript entries.")