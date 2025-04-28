from crewai import Task
from textwrap import dedent
from dotenv import load_dotenv
from agents.modren_integrative_diagnostic_recommendation_agent import ModrenIntegrativeDiagnosticRecommendationAgentClass

load_dotenv()

# Instance of ModrenIntegrativeDiagnosticRecommendationAgentClass to pass as agent parameter value to task
modrenIntegrativeDiagnosticRecommendationAgent = ModrenIntegrativeDiagnosticRecommendationAgentClass().modren_integrative_diagnostic_recommendation_specialist

class ModrenIntegrativeDiagnosticRecommendationAgentTaskClass:
    def __init__(self):  
        
       # Task related to modern intergrative recommendation Agent
        self.modren_integrative_diagnostic_recommendation_specialist_task = Task(
            description=dedent(
                        """ 
                            To generate a structured modren integrative diagnosis and treatment plan based on patient data, clinical observations, modren integrative principles and provided medical Recommendation.    
                            1. Analyze input context : {analysis_result}, thoroughly analyze provided medical reports. 
                            2. Generating a detailed treatment plan that includes medications, therapies, and follow-up recommendations1. 
                            3. Analyze the provided patient medical report to identify health imbalances and conditions. 
                            4. Synthesize findings from allopathic diagnostics, functional medicine insights, and Ayurvedic interpretations to create a comprehensive health assessment. 
                            5. Based on this analysis, develop personalized recommendations encompassing dietary guidelines, lifestyle modifications, herbal supplements, and therapeutic interventions.
                            6. Provide the medication regimens with dosages, routes of administration, duration, etc.
                            7. Further diagnostic tests or follow-up actions if necessary.
                            8. Provide list top 5 Modren integrative hospitals to undergo suggested treatment in Karnataka
                            9. Always use authentic websites realated to modren integrative diagnosis and recommandation when pulling required datas.
                            10. Always follow structured output format in a JSON format provided in expected_output document 
                        """
                ),
            agent=modrenIntegrativeDiagnosticRecommendationAgent,
            expected_output=dedent(
                                """ 
                                    {
                                    "IntegrativeDiagnostics": {
                                        "ReportType": "[Report Type]",
                                        "PatientDetails": {
                                            "Name": "[Patient Name]",
                                            "Age": "[Patient Age]",
                                            "Sex": "[Patient Sex]",
                                            "ReportID": "[Report ID]",
                                            "SampleCollectedDate": "[Sample Collection Date]",
                                            "ReportDate": "[Report Date]"
                                        },
                                        "AllopathicFindings": {
                                            "ConfirmedCondition": [
                                                {
                                                    "Condition": "[Allopathic Diagnosis]",
                                                    "SupportingEvidence": {
                                                        "DiagnosticEvidence": "[Lab Test Results]",
                                                        "ClinicalEvidence": "[Symptoms or Observations]"
                                                    }
                                                }
                                            ]
                                        },
                                        "FunctionalMedicineInsights": {
                                            "MetabolicImbalances": "[Metabolic Issue, e.g., Kidney Stress]",
                                            "HormonalImbalances": "[Cortisol, Thyroid, Insulin, etc.]",
                                            "OxidativeStressMarkers": "[Reactive Oxygen Species, Lipid Peroxidation Products, Protein Oxidation, etc.]",
                                            "NutritionalDeficiencies": "[Deficiencies, e.g., Low Phosphorus]",
                                            "InflammationMarkers": "[Markers Indicating Inflammation]",
                                            "GutHealthAssessment": "[Gut Health Insights]"
                                        },
                                        "AyurvedicInterpretation": {
                                            "DoshaImbalance": "[Vata/Pitta/Kapha Imbalance]",
                                            "AgniStatus": "[Agni Type: Mandagni, Tikshnagni, etc.]",
                                            "AmaPresence": "[Presence of Toxins: Yes/No]",
                                            "AffectedSrotas": "[Affected Channels, e.g., Mutravaha Srotas]",
                                            "OjasStatus": "[Strong/Weak Ojas]",
                                            "MentalState": "[Emotional & Mental Well-being]",
                                            "ManasPrakriti": "[Sattva, Rajas, Tamas]",
                                            "PranaVayuBalance": "[Airflow and Nervous System Health]"
                                        }
                                    },
                                    "IntegrativeTreatmentRecommendations": {
                                        "LifestyleModifications": {
                                            "Hydration": "[Water Intake Guidelines]",
                                            "Exercise": "[Recommended Physical Activity]",
                                            "SleepHygiene": "[Sleep Schedule & Relaxation Techniques]"
                                        },
                                        "HerbalAndSupplementSupport": [
                                            {
                                                "Name": "[Herbal Remedy or Supplement]",
                                                "Dosage": "[Dosage]",
                                                "Purpose": "[Benefit of This Supplement]"
                                            }
                                        ],
                                        "DetoxAndTherapies": {
                                            "Detoxification": "[Panchakarma/Detox Plan]",
                                            "Therapies": "[Massage, Yoga, etc.]"
                                        }
                                    },
                                    "MonitoringAndFollowUp": {
                                        "FurtherDiagnosticTests": [
                                            {
                                                "NextCheckup": "[Recommended Follow-up Time]",
                                                "TestsToMonitor": ["[Lab Tests to Track Progress]"],
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
                                    "Disclaimer": "This integrative health plan combines allopathic, functional medicine, and Ayurvedic perspectives. Consult your healthcare provider before making significant changes to diet, medication, or therapy."
                                    }                         
                                """                
            ),     
        )