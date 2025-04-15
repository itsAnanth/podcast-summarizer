from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class SummarizerTask(BaseModel):
    summary: str
    
class TranslatorTask(BaseModel):
    translated: str


LLM = llm = LLM(model="gemini/gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))

@CrewBase
class SummarizerCrew:
    """Crew for summarizing podcasts."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    
    
    @agent
    def podcast_summarizer(self) -> Agent:
        """Agent for summarizing podcasts."""
        return Agent(
            config=self.agents_config['podcast_summarizer'],
            llm=LLM,
        )

    @task
    def summarize_task(self) -> Task:
        """Task for summarizing podcasts."""
        return Task(
            config=self.tasks_config["analyze_podcast_transcript"],
            output_pydantic=SummarizerTask
        )
        
        
    @agent
    def podcast_translator(self) -> Agent:
        """Agent for translating podcasts."""
        return Agent(
            config=self.agents_config['podcast_translator'],
            llm=LLM,
        )
    
    @task
    def translate_task(self) -> Task:
        """Task for translating podcasts."""
        return Task(
            config=self.tasks_config["translate_podcast_transcript"],
            output_pydantic=TranslatorTask
        )
        
    @crew
    def crew(self) -> Crew:
        """Crew for summarizing podcasts."""
        return Crew(
            agents=[self.podcast_translator(), self.podcast_summarizer()],
            tasks=[self.translate_task(), self.summarize_task()],
            process=Process.sequential,
            verbose=False
        )