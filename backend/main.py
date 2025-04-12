from utils.transcript import save_transcript
from models.Summarize import summarize_transcript
from crew_models.summarizer_flow import SummarizerFlow
from dotenv import load_dotenv

load_dotenv()
# https://www.youtube.com/watch?v=7ARBJQn6QkM
def main():
    print("Hello from podcast-summarizer!")
    # video_id = "xFvlUVkMPJY"
    video_id = "7ARBJQn6QkM"
    save_transcript(video_id)
    
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.writelines(summarize_transcript('input.txt'))

def test_summary():
    flow = SummarizerFlow()
    flow.kickoff()
    flow.plot()
if __name__ == "__main__":
    test_summary()
    # main()
