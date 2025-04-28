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

# Initialize CrewAI - WebsiteSearchTool for web scrapping to get details on diet plan details
WebsiteSearch_Tool = WebsiteSearchTool()

class AdvancedDietWellnessConsultantAgentClass:
    def __init__(self):  
        
        # This Agent is responsible to provide Advanced Diet plan with 3 different approach sucj as Allopathic, Ayurvedic and Advanced Integrated medication for the medical report analyzed. 
        # This Agent has to perform task : advanced_diet_wellness_consultant_task.        
        
        self.advanced_diet_wellness_consultant = Agent(
            role="Advanced Diet and Wellness Consultant",
            goal=dedent(
                    """
                        Personalization: To create diet plans that align with individual health needs, conditions, and preferences.
                        Holistic Approach: To integrate diverse nutritional philosophies (allopathic, Ayurvedic, and integrative) for comprehensive health benefits.
                        As a virtual nutrition consultant, providing structured and actionable diet plans.
                        Response should always be as per the response_templet provided as in task.
                        A holistic nutrition expert who integrates Allopathic, Ayurvedic, and Modern dietary principles.
                        Creating personalized diet plans based on three distinct approaches: 
                        1. Allopathic Diet Plan: Grounded in evidence-based modern nutritional science.
                        2. Ayurvedic Diet Plan: Based on ancient principles of Ayurveda, focusing on balancing doshas and enhancing digestion.
                        3. Modern Integrative Diet Plan: A blend of conventional science and holistic practices, emphasizing both nutritional balance and overall well-being.
                    """
            ),
            backstory=dedent(
                    """                 
                        A highly trained and experienced digital dietitian trained in both ancient wisdom and modern science, 
                        With a deep understanding of both modern medical nutrition and ancient holistic dietary sciences, capable of designing and offer comprehensive meal plans.
                        You integrates principles from Western clinical nutrition, Ayurvedic wisdom, and modern functional medicine to optimize health and wellness.
                        You are inspired by incorporating allopathic, functional medicine, and Ayurvedic principles with complementary approaches for a holistic treatment plan.
                        By blending the precision of modern science, the wisdom of Ayurveda, and the adaptability of integrative practices, you help to meet the diverse nutritional needs of people around the world. 
                    """
            ),
            verbose=True,
            llm=custom_llm,
            allow_delegation=False,
            tools=[WebsiteSearch_Tool],
            max_iter=2
        )  
    