from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List

@CrewBase
class MarketingCrew():
    """MarketingCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    
    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reviewer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer_agent'], # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'], # type: ignore[index]
            output_file='content.md',
            verbose=True
        )
    
    @task
    def reviewing_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_task'], # type: ignore[index]
            output_file='improvements.md',
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingCrew crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            
        )
