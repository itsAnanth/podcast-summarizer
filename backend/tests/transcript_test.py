from utils.transcript import save_transcript, get_transcript
from models.Summarize import summarize_transcript

# # https://www.youtube.com/watch?v=7ARBJQn6QkM
video_id = "7ARBJQn6QkM"
transcript = get_transcript(video_id)

save_transcript(transcript, 'tests/transcript.txt')

summary = summarize_transcript(transcript)

print(summary)

with open('tests/summary.txt', 'w', encoding='utf-8') as f:
    f.write(summary)