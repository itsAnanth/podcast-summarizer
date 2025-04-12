from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel

class SummarizerTask(BaseModel):
    summary: str


@CrewBase
class SummarizerCrew:
    """Crew for summarizing podcasts."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    llm = LLM(model="groq/deepseek-r1-distill-llama-70b")
    
    @agent
    def podcast_summarizer(self) -> Agent:
        """Agent for summarizing podcasts."""
        return Agent(
            config=self.agents_config['podcast_summarizer'],
            llm=self.llm,
        )

    @task
    def summarize_task(self) -> Task:
        """Task for summarizing podcasts."""
        return Task(
            config=self.tasks_config["analyze_podcast_transcript"],
            output_pydantic=SummarizerTask
        )
        
    @crew
    def crew(self) -> Crew:
        """Crew for summarizing podcasts."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )