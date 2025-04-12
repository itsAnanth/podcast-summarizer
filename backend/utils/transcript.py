from youtube_transcript_api import YouTubeTranscriptApi

def save_transcript(video_id):

    # video_id = "-lFAIxq8kaY"

    available_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
    # print(available_transcripts._generated_transcripts)

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=("en", "hi"))

    original_text = " ".join([entry['text'] for entry in transcript])

    with open('input.txt', 'w', encoding='utf-8') as f:
        f.write(original_text)
    
def load_transcript():
    text = None
    
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        
    return text