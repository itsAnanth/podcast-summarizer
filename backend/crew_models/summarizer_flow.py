from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from .summarizer_crew import SummarizerCrew

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
            
            
    @listen(load_transcript)
    def generate_summary(self):
        """Generate summary of the podcast."""
        output = (
            SummarizerCrew()
            .crew()
            .kickoff(inputs={"transcript": self.state.transcript})
        )
        
        
        print("FLOW OUTPUT", output)
        return output['summary']