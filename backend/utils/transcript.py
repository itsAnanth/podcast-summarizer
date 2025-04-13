from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str) -> str:
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        try:
            transcript = transcript_list.find_manually_created_transcript(['en'])
        except:
            transcript = transcript_list.find_generated_transcript(['en'])
        
        full_transcript = transcript.fetch().to_raw_data()
        
        return " ".join([entry['text'] for entry in full_transcript])
    
    except Exception as e:
        print(f"Error getting transcript: {e}")
        return None

def save_transcript(text, path):
    print(f"Saving transcript to {path}")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    
def load_transcript():
    text = None
    
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        
    return text