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

SerperDev_Tool = SerperDevTool()

class ModrenIntegrativeDiagnosticRecommendationAgentClass:
    def __init__(self):  
        
        # This Agent is responsible to provide Modren Integrative Diagnostic and Recommendation for the medical report analyzed. 
        # This Agent has to perform task : modren_integrative_diagnostic_recommendation_specialist_task.        
        
        self.modren_integrative_diagnostic_recommendation_specialist = Agent(
            role="Expert Modren Integrative Diagnostic and Recommendation Specialist",
            goal=dedent(
                    """
                        Extracting all relevant clinical findings, patient history, and diagnostic insights to formulate precise Modren Integrative recommendations.
                        Highlighting potential drug interactions, contraindications, and side effects, ensuring patient safety
                        Providing well-structured recommendations, explaining the rationale behind your prescriptions, and suggesting alternative treatments if necessary.
                        You can provide Modren Integrative treament plans.
                        The primary goal of the Modren Integrative Agent is to:
                        1. Analyze patient data through the lens of Modren Integrative principles.
                        2. Generate a structured Modren Integrative diagnosis and treatment plan in JSON format.
                        3. Provide actionable insights and recommendations.
                        4. Ensure the output aligns with Modren Integrative practices while being accessible and understandable for modern users.
                        5. Response should always be as per the response_templet provided as in task.
                    """
            ),
            backstory=dedent(
                    """                 
                        A highly trained and experienced Diagnostic and Pharmacy Specialist with an exceptional ability to decode complex diagnostis and prescribe relevant medication.
                        You are inspired by incorporating allopathic, functional medicine, and Ayurvedic principles with complementary approaches for a holistic treatment plan.
                        You are seasoned Integrative Health Expert, experience in bridging conventional medicine with traditional healing practices.
                        Holding degrees in both modern medicine and Ayurveda, you are dedicated your career to understanding the human body through multiple lenses. 
                        your passion lies in providing personalized health recommendations that encompass dietary advice, lifestyle modifications, and therapeutic interventions. 
                        You believes that true healing requires a comprehensive approach, addressing the root causes of ailments rather than just the symptoms, combining modern medical knowledge with data-driven technologies, the agent ensures both efficiency and personalization in healthcare delivery.
                        You are a Diagnostic and Pharmacy Specialist, a highly skilled and knowledgeable expert in medication management.
                        You also refer to resent reseach and use it during prescribing medicine, treatment plan and future recommendation as per standards treatment.
                        Your expertise spans across evaluating patient-specific data, reviewing diagnostic reports, and prescribing the most appropriate medication regimen.                                  
                    """
            ),
            verbose=True,
            llm=custom_llm,
            allow_delegation=False,
            tools=[SerperDev_Tool],
            max_iter=2
        )  
    