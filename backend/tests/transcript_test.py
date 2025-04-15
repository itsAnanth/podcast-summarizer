from utils.transcript import save_transcript, get_transcript
from models.Summarize import summarize_transcript
from models.Translate import translate_transcript
from crew_models.summarizer_flow import SummarizerFlow

print(__file__)
# # https://www.youtube.com/watch?v=7ARBJQn6QkM
video_id = "kDMSWgEZIYI"
# transcript = get_transcript(video_id, language=['ml'])

# save_transcript(transcript, 'tests/transcript.txt')

# translated_transcript = translate_transcript('tests/transcript.txt', use_path=True)

# save_transcript(translate_transcript, 'tests/translated_transcript.txt')

# chunk_summary = summarize_transcript(transcript)

# with open('tests/chunk_summary.txt', 'w', encoding='utf-8') as f:
#     f.write(chunk_summary)
    
# summary, translated = SummarizerFlow().kickoff(inputs={'transcript': 'tests/transcript.txt', 'use_path': True })


    
# with open('tests/summary.txt', 'w', encoding='utf-8') as f:
#     f.write(summary)
    
# with open('tests/translated.txt', 'w', encoding='utf-8') as f:
#     f.write(translated)


with open('tests/summary.txt', 'r', encoding='utf-8') as file:
    transcript = file.read()
    print(transcript)
    
    a = [1, 2]
    print(a[:1000])