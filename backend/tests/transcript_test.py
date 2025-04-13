from utils.transcript import save_transcript, get_transcript
from models.Summarize import summarize_transcript
from crew_models.summarizer_flow import SummarizerFlow

print(__file__)
# # https://www.youtube.com/watch?v=7ARBJQn6QkM
video_id = "7ARBJQn6QkM"
transcript = get_transcript(video_id)

save_transcript(transcript, 'tests/transcript.txt')

chunk_summary = summarize_transcript(transcript)

with open('tests/chunk_summary.txt', 'w', encoding='utf-8') as f:
    f.write(chunk_summary)
    
summary = SummarizerFlow().kickoff(inputs={'transcript': 'tests/chunk_summary.txt', 'use_path': True })

with open('tests/summary.txt', 'w', encoding='utf-8') as f:
    f.write(summary)