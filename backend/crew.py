from crewai import Agent,Task,Crew,Process
from dotenv import load_dotenv
import agents.multilingual_agent as multilingual_agent
import agents.allopathic_diagnostic_recommendation_agent as allopathic_diagnostic_recommendation_agent
import agents.ayurvedic_diagnostic_recommendation_agent as ayurvedic_diagnostic_recommendation_agent
import agents.modren_integrative_diagnostic_recommendation_agent as modren_integrative_diagnostic_recommendation_agent
import agents.advanced_diet_wellness_consultant_agent as advanced_diet_wellness_consultant_agent
import tasks.advanced_diet_wellness_consultant_agent_task as advanced_diet_wellness_consultant_agent_task
import tasks.allopathic_diagnostic_recommendation_agent_task as allopathic_diagnostic_recommendation_agent_task
import tasks.ayurvedic_diagnostic_recommendation_agent_task as ayurvedic_diagnostic_recommendation_agent_task
import tasks.modren_integrative_diagnostic_recommendation_agent_task as modren_integrative_diagnostic_recommendation_agent_task
import tasks.multilingual_agent_task as multilingual_agent_task


load_dotenv()

# Agents Intialization 
multilingualagent = multilingual_agent.MultilingualAgentClass().analysis_interpreter_multilingual
allopathicdiagnosticrecommendationagent = allopathic_diagnostic_recommendation_agent.AllopathicDiagnosticRecommendationAgentClass().allopathic_diagnostic_recommendation_specialist
ayurvedicdiagnosticrecommendationagent = ayurvedic_diagnostic_recommendation_agent.AyurvedicDiagnosticRecommendationAgentClass().ayurvedic_diagnostic_recommendation_specialist
modrenintegrativediagnosticrecommendationagent = modren_integrative_diagnostic_recommendation_agent.ModrenIntegrativeDiagnosticRecommendationAgentClass().modren_integrative_diagnostic_recommendation_specialist
advanceddietwellnessconsultantagent = advanced_diet_wellness_consultant_agent.AdvancedDietWellnessConsultantAgentClass().advanced_diet_wellness_consultant

# Tasks Intialization
multilingualagentkannadatask = multilingual_agent_task.MultilingualAgentTaskClass().analysis_interpreter_kannada_task
multilingualagenthinditask = multilingual_agent_task.MultilingualAgentTaskClass().analysis_interpreter_hindi_task
allopathicdiagnosticrecommendationtask = allopathic_diagnostic_recommendation_agent_task.AllopathicDiagnosticRecommendationAgentTaskClass().allopathic_diagnostic_recommendation_specialist_task
ayurvedicdiagnosticrecommendationtask = ayurvedic_diagnostic_recommendation_agent_task.AyurvedicDiagnosticRecommendationAgentTaskClass().ayurvedic_diagnostic_recommendation_specialist_task
modrenintegrativediagnosticrecommendationtask = modren_integrative_diagnostic_recommendation_agent_task.ModrenIntegrativeDiagnosticRecommendationAgentTaskClass().modren_integrative_diagnostic_recommendation_specialist_task
advanceddietwellnessconsultanttask = advanced_diet_wellness_consultant_agent_task.AdvancedDietWellnessConsultantAgentTaskClass().advanced_diet_wellness_consultant_task


class CrewClass:
    def __init__(self):  
        
        # Crew Definition
        self.crew = Crew(
            agents=[multilingualagent, allopathicdiagnosticrecommendationagent, ayurvedicdiagnosticrecommendationagent, modrenintegrativediagnosticrecommendationagent, advanceddietwellnessconsultantagent],
            tasks=[multilingualagentkannadatask, multilingualagenthinditask, allopathicdiagnosticrecommendationtask, ayurvedicdiagnosticrecommendationtask, modrenintegrativediagnosticrecommendationtask, advanceddietwellnessconsultanttask],
            process=Process.sequential,
            verbose=True,           
        )
        
    def get_crew(self):
        return self.crew