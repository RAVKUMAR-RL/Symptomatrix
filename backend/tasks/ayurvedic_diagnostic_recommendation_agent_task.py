from crewai import Task
from textwrap import dedent
from dotenv import load_dotenv
from agents.ayurvedic_diagnostic_recommendation_agent import AyurvedicDiagnosticRecommendationAgentClass

load_dotenv()

# Instance of AyurvedicDiagnosticRecommendationAgentClass to pass as agent parameter value to task
ayurvedicDiagnosticRecommendationAgent = AyurvedicDiagnosticRecommendationAgentClass().ayurvedic_diagnostic_recommendation_specialist

class AyurvedicDiagnosticRecommendationAgentTaskClass:
    def __init__(self):  
        
      # Task related to ayurvedic recommendation Agent
        self.ayurvedic_diagnostic_recommendation_specialist_task = Task(
            description=dedent(
                        """ 
                            To generate a structured Ayurvedic diagnosis and treatment plan based on patient data, clinical observations, Ayurvedic principles and provided medical report.    
                            1. Analyze input context : {analysis_result}, thoroughly analyze provided medical reports, analyze the input data using Ayurvedic principles.
                            2. Identify the root cause of the condition (e.g., Dosha imbalance, weak Agni).
                            3. Recommend appropriate therapies (Shodhana, Shamana).
                            4. Suggest dietary and lifestyle changes (Pathya-Apathya).
                            5. Provide the medication regimens with dosages, routes of administration, duration, etc.
                            6. Further diagnostic tests or follow-up actions if necessary.
                            7. Stick on to ayurvedic treatment approach only.
                            8. Provide list top 5 ayurvedic hospitals to undergo suggested treatment in Karnataka
                            9. Always use authentic websites realated to ayurvedic diagnostic and recommendation when pulling required datas.
                            10. Structure the output in a JSON format provided in expected_output document detailing the patient's Ayurvedic diagnosis, including Prakriti (constitution) analysis,
                                Vikriti (current imbalances), Agni (digestive fire) and Ama (toxins) assessment, Dhatu and Srotas evaluation,
                                mental state and Ojas (vital energy) status, followed by a personalized treatment plan covering diet recommendations, lifestyle modifications, herbal remedies, detoxification therapies, and a follow-up plan.                           
                        """
                ),
            agent=ayurvedicDiagnosticRecommendationAgent,
            expected_output=dedent(
                            """ 
                                    {
                                    "AyurvedicDiagnosis": {
                                        "ReportType": "[Report Type]",
                                        "PatientDetails": {
                                            "Name": "[Patient Name]",
                                            "Age": "[Patient Age]",
                                            "Sex": "[Patient Sex]",
                                            "ReportID": "[Report ID]",
                                            "ConsultationDate": "[Consultation Date]",
                                            "ReportDate": "[Report Date]"
                                        },
                                        "PrakritiAnalysis": {
                                            "PrimaryDosha": "[Primary Dosha: Vata/Pitta/Kapha]",
                                            "SecondaryDosha": "[Secondary Dosha]",
                                            "BodyType": "[Slim/Medium/Heavy]",
                                            "MentalTraits": "[Calm/Anxious/Ambitious, etc.]"
                                        },
                                        "VikritiAnalysis": {
                                            "ImbalancedDosha": "[Vata/Pitta/Kapha]",
                                            "Symptoms": ["[List of symptoms like acidity, bloating, fatigue, skin issues]"]
                                        },
                                        "AgniAmaAssessment": {
                                            "AgniType": "[Weak/Strong/Irregular]",
                                            "AmaPresence": "[Yes/No]",
                                            "SignsOfAma": "[List of signs like tongue coating, sluggish digestion]"
                                        },
                                        "DhatuSrotasAssessment": {
                                            "AffectedDhatus": [
                                                "[Affected tissues like Rasa (plasma), Rakta (blood), Mamsa (muscles)]"
                                            ],
                                            "AffectedSrotas": [
                                                "[Affected channels like Annavaha (digestion), Raktavaha (blood circulation)]"
                                            ]
                                        },
                                        "MentalStateOjas": {
                                            "MentalState": "[Calm/Anxious/Overactive]",
                                            "OjasLevel": "[Low/Moderate/High]"
                                        }
                                    },
                                    "AyurvedicTreatmentPlan": {
                                        "LifestyleModifications": {
                                            "Dinacharya": "[Daily Routine Recommendations]",
                                            "ExerciseRecommendations": "[Type of exercise like walking, swimming]",
                                            "YogaAndPranayama": [
                                                {
                                                    "PracticeName": "[Yoga/Pranayama Name]",
                                                    "Duration": "[Duration]"
                                                }
                                            ]
                                        },
                                        "ShodhanaTherapies": [
                                            {
                                                "Therapy": "[Cleansing Therapy Name]",
                                                "Purpose": "[Purpose]"
                                            }
                                        ],
                                        "ShamanaTherapies": [
                                            {
                                                "HerbalRemedy": "[Herbal Name]",
                                                "Dosage": "[Dosage]",
                                                "Usage": "[How to take it]",
                                                "Rationale": "[Why this herb is used]"
                                            }
                                        ],
                                        "DetoxificationAndTherapies": {
                                            "RecommendedTherapies": [
                                                "[Panchakarma or detox methods like Abhyanga (oil massage), Nasya (nasal therapy)]"
                                            ]
                                        }
                                    },
                                    "MonitoringandFurtherDiagnosticTests": {
                                        "FurtherDiagnosticTests": [
                                            {
                                                "NextCheckup": "[Follow-up time frame]",
                                                "MonitoringParameters": "[What needs to be observed, like digestion, sleep, energy levels]",
                                                "Referral": "[Referral department for medical test]"
                                            }
                                        ],
                                        "TopHospitalsforTreatment": [
                                            {
                                                "Name": "[Hospital Name, Address]",
                                                "Specialty": "[Specialty]"
                                            }
                                        ]
                                    },
                                    "Disclaimer": "This Ayurvedic treatment plan is based on traditional knowledge and should be followed under the guidance of a qualified Ayurvedic practitioner. Regular follow-ups are essential to ensure effective results."
                                }
                            """                
            ),         
        )