from crewai import Task
from textwrap import dedent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from agents.multilingual_agent import MultilingualAgentClass

load_dotenv()

# Instance of MultilingualAgentClass to pass as agent parameter value to task
MultilingualAgent = MultilingualAgentClass().analysis_interpreter_multilingual

class MultilingualAgentTaskClass:
    def __init__(self):  
        
        # Task related to Multilingual Agent for Interpretation of summary in Kannada Language
        self.analysis_interpreter_kannada_task = Task(
            description=dedent(
                        """    
                            1. Interpret context : {analysis_result} in kannada language as per the output templet provided. 
                            2. You need to interpret the source provided into kannnda language as per the expected output.
                            3. Always convert the english language provided in expected ouput into kannada langugae.
                            4. Accomplish this task and respond only in Kannada language, ensuring the use of accurate Kannada words.
                            5. Include this as Disclaimer : ಈ ಎಐ ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮಾಹಿತಿ ನೀಡುತ್ತದೆ ಮತ್ತು ವೃತ್ತಿಪರ ವೈದ್ಯಕೀಯ ಸಲಹೆಗೆ ಪರ್ಯಾಯವಾಗಿ ಬಳಸಬಾರದು. ಖಚಿತ ಶಾಂತರ ಮತ್ತು ಚಿಕಿತ್ಸೆಯಿಗಾಗಿ ಹಿತಾಯಧೀಶ ವೈದ್ಯರನ್ನು ಸದಾ ಸಂಪರ್ಕಿಸಿ. 
                        """
            ),
            agent=MultilingualAgent,
            expected_output=dedent(
                                """
                                    {
                                        "ReportType": "[Report Type in kannada language]",
                                        "PatientDetails": {
                                            "Name": "[Patient Name in kannada language]",
                                            "Age": "[Patient Age in kannada language]",
                                            "Sex": "[Patient Sex in kannada language]",
                                            "ReportID": "[Report ID in kannada language]",
                                            "SampleCollectedDate": "[Sample Collection Date in kannada language]",
                                            "ReportDate": "[Report Date in kannada language]"
                                        },
                                        "ClinicalObservations": {
                                            "Findings": [
                                            {
                                                "Parameter": "[Parameter Name in kannada language]",
                                                "Result": "[Value in kannada language]",
                                                "ReferenceRange": "[Min - Max Unit in kannada language]",
                                                "Observation": "[Observation in kannada language]"
                                            }
                                            ],
                                            "Summary": "[Summary of key findings in kannada language]"
                                        },
                                        "DiagnosisImpression": {
                                            "Conditions": [
                                            {
                                                "Condition": "[Condition Name in kannada language]",
                                                "Evidence": "[Supporting Evidence in kannada language]"
                                            }
                                            ],
                                            "DifferentialDiagnoses": [
                                            {
                                                "Condition": "[Potential Condition in kannada language]",
                                                "Reason": "[Supporting Reason in kannada language]"
                                            }
                                            ],
                                            "GuidelinesReference": "[Reference Guidelines in kannada language]"
                                        },
                                        "Prognosis": {
                                            "ClinicalCorrelation": "[Explanation of condition significance in kannada language]",
                                            "RecoveryChances": "[Likelihood of recovery based on findings in kannada language]",
                                            "ExpectedProgression": "[Possible disease progression in kannada language]",
                                            "SurvivalRates": "[Impact on life expectancy in kannada language]",
                                            "QualityofLife": "[Impact on daily life and activities in kannada language]"
                                        },
                                        "ConfidenceLevel": {
                                            "Percentage": "[Confidence level Percentage in kannada language]",
                                            "Explanation": "[Reasoning behind confidence level in kannada language]"
                                        },
                                        "Disclaimer": "[Medical disclaimer text in kannada language]"
                                        }                     
                                """                
            ),
            async_execution =True,
        )
        
              
         # Task related to Multilingual Agent for Interpretation of summary in Hindi Language
        self.analysis_interpreter_hindi_task = Task(
            description=dedent(
                        """     
                            1. Interpret context : {analysis_result} in hindi language as per the output templet provided.
                            2. You need to interpret the source provided into hindi language as per the expected output.
                            3. Always convert the english language provided in expected ouput into hindi langugae.
                            4. Accomplish this task and respond only in hindi language, ensuring the use of accurate hindi words.
                            5. Include this as Disclaimer :यह एआई केवल सामान्य स्वास्थ्य जानकारी प्रदान करता है और इसे पेशेवर चिकित्सा सलाह के विकल्प के रूप में उपयोग नहीं किया जाना चाहिए। सटीक निदान और उपचार के लिए हमेशा किसी योग्य चिकित्सक से परामर्श लें। 
                        """
                ),
            agent=MultilingualAgent,
            expected_output=dedent(
                                    """
                                        {
                                        "ReportType": "[Report Type in Hindi language]",
                                        "PatientDetails": {
                                            "Name": "[Patient Name in Hindi language]",
                                            "Age": "[Patient Age in Hindi language]",
                                            "Sex": "[Patient Sex in Hindi language]",
                                            "ReportID": "[Report ID in Hindi language]",
                                            "SampleCollectedDate": "[Sample Collection Date in Hindi language]",
                                            "ReportDate": "[Report Date in Hindi language]"
                                        },
                                        "ClinicalObservations": {
                                            "Findings": [
                                            {
                                                "Parameter": "[Parameter Name in Hindi language]",
                                                "Result": "[Value in Hindi language]",
                                                "ReferenceRange": "[Min - Max Unit in Hindi language]",
                                                "Observation": "[Observation in Hindi language]"
                                            }
                                            ],
                                            "Summary": "[Summary of key findings in Hindi language]"
                                        },
                                        "DiagnosisImpression": {
                                            "Conditions": [
                                            {
                                                "Condition": "[Condition Name in Hindi language]",
                                                "Evidence": "[Supporting Evidence in Hindi language]"
                                            }
                                            ],
                                            "DifferentialDiagnoses": [
                                            {
                                                "Condition": "[Potential Condition in Hindi language]",
                                                "Reason": "[Supporting Reason in Hindi language]"
                                            }
                                            ],
                                            "GuidelinesReference": "[Reference Guidelines in Hindi language]"
                                        },
                                        "Prognosis": {
                                            "ClinicalCorrelation": "[Explanation of condition significance in Hindi language]",
                                            "RecoveryChances": "[Likelihood of recovery based on findings in Hindi language]",
                                            "ExpectedProgression": "[Possible disease progression in Hindi language]",
                                            "SurvivalRates": "[Impact on life expectancy in Hindi language]",
                                            "QualityofLife": "[Impact on daily life and activities in Hindi language]"
                                        },
                                        "ConfidenceLevel": {
                                            "Percentage": "[Confidence level Percentage in Hindi language]",
                                            "Explanation": "[Reasoning behind confidence level in Hindi language]"
                                        },
                                        "Disclaimer": "[Medical disclaimer text in Hindi language]"
                                        }                     
                                    """                
            ),
            async_execution =True,
        )
        