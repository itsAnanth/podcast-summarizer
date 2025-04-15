from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from .summarizer_crew import SummarizerCrew
import tiktoken


class SummarizerState(BaseModel):
    """State for the summarizer."""
    id: str = "summarizer_flow_state"
    transcript: str = "Podcast transcript goes here"
    use_path: bool = False
    
    
class SummarizerFlow(Flow[SummarizerState]):
    
    initial_state = SummarizerState
    
    @start()
    def load_transcript(self):
        if self.state.use_path:
            with open(self.state.transcript, 'r', encoding='utf-8') as file:
                self.state.transcript = file.read()
                self.state.transcript = self.state.transcript[:10000]
                
                # tokenizer = tiktoken.get_encoding('cl100k_base')
                # tokens = tokenizer.encode(self.state.transcript)            
            
    @listen(load_transcript)
    def generate_summary(self):
        """Generate summary of the podcast."""
        sumcrew = SummarizerCrew()
        output = (
            sumcrew
            .crew()
            .kickoff(inputs={"transcript": self.state.transcript})
        )
        
        
        return output['summary'], sumcrew.translate_task().output.to_dict()['translated']