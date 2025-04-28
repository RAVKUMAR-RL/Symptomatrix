from crewai import Agent
from textwrap import dedent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

# Create a customized LLM instance with desired temperature
custom_llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.2,    # Making the output more deterministic and precise.
    max_tokens=2000     # Restricting max token for the LLM model.
)


class MultilingualAgentClass:
    def __init__(self):  
        
        
        # This Agent is responsible to intepret the Summary into kannada and Hindi for the medical report analyzed.
        # This Agent has to perform two tasks : analysis_interpreter_kannada_task, analysis_interpreter_hindi_task      
                    
        self.analysis_interpreter_multilingual = Agent(
            role="Expert Medical Report Analysis Specialist in kannada and Hindi language",
            goal=dedent("""
                        Kindly remember that you are highly expert and proferssional in medical field and you are interpreting the medical report in kannada and hindi language and respond in simple kannda and hindi language expressing to be understood by a common man. 
                        Response should always be in kannada  or Hindi language as per the response_templet provided as in task.
                        """
            ),
            backstory=dedent("""
                        A highly trained and experienced Medical report analysis Specialist with an exceptional ability to decode complex diagnostis in kannada and hindi language.
                        Possessing extensive expertise in radiological analysis, pathology reports, blood reports, and various diagnostic imaging techniques,
                        this expert leverages cutting-edge models trained on vast medical datasets. Their analytical capabilities are finely tuned to produce highly accurate,
                        structured, and clinically relevant insights with a focus on providing clear, actionable information for medical professionals.
                        """
            ),
            verbose=True,
            llm=custom_llm,
            allow_delegation=False,                
        )
  
  