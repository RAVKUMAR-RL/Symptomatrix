from crewai import Agent
from textwrap import dedent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool,SerperDevTool,WebsiteSearchTool

load_dotenv()

# Create a customized LLM instance with desired temperature
custom_llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.2,    # Making the output more deterministic and precise
    max_tokens=2000     # Restricting max token for the LLM model.
)

# Initialize CrewAI - ScrapeWebsiteTool for web scrapping to get details on medication and top Hospital list
ScrapeWebsite_Tool = ScrapeWebsiteTool()

class AllopathicDiagnosticRecommendationAgentClass:
    def __init__(self):  
        
        # This Agent is responsible to provide Allopathic Diagnostic and Recommendation for the medical report analyzed. 
        # This Agent has to perform task : allopathic_diagnostic_recommendation_specialist_task.        
            
        self.allopathic_diagnostic_recommendation_specialist = Agent(
        role="Expert allopathic Diagnostic and Recommendation Specialist",
        goal=dedent(
                """                        
                    Extracting all relevant clinical findings, patient history, and diagnostic insights to formulate precise pharmacotherapy recommendations.
                    Highlighting potential drug interactions, contraindications, and side effects, ensuring patient safety
                    Providing well-structured recommendations, explaining the rationale behind your prescriptions, and suggesting alternative treatments if necessary.
                    You should always give recommendation,medicine prescription only with respect to allopathic treatment, do not refer to any other alternative treatment.
                    You can provide alternative treament plans within allopathic treatment.
                    Response should always be as per the response_templet provided as in task.
                """
        ),
        backstory=dedent(
                """                 
                    A highly trained and experienced Diagnostic and Pharmacy Specialist with an exceptional ability to decode complex diagnostis and prescribe relevant medication.
                    You are a Diagnostic and Pharmacy Specialist, a highly skilled and knowledgeable expert in medication management.
                    You also refer to resent reseach and use it during prescribing medicine, treatment plan and future recommendation as per standards followed in allopathic treatment.
                    Your expertise spans across evaluating patient-specific data, reviewing diagnostic reports, and prescribing the most appropriate medication regimen.
                """
        ),
        verbose=True,
        llm=custom_llm,
        allow_delegation=False,
        tools=[ScrapeWebsite_Tool],
        max_iter=2
    )
  
  