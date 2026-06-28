from youtube_transcript_api import YouTubeTranscriptApi

video_id = "Rni7Fz7208c"

ytt_api = YouTubeTranscriptApi()

transcript = ytt_api.fetch(video_id)

print("transcript lenght")
print(len(transcript))

print("First:")
print(transcript[0])

print("\nLast:")
print(transcript[-1])