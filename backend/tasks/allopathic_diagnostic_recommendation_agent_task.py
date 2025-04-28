from crewai import Task
from textwrap import dedent
from dotenv import load_dotenv
from agents.allopathic_diagnostic_recommendation_agent import AllopathicDiagnosticRecommendationAgentClass

load_dotenv()

# Instance of AllopathicDiagnosticRecommendationAgentClass to pass as agent parameter value to task
allopathicDiagnosticRecommendationAgent = AllopathicDiagnosticRecommendationAgentClass().allopathic_diagnostic_recommendation_specialist

class AllopathicDiagnosticRecommendationAgentTaskClass:
    def __init__(self):  
        
       # Task related to allopathic recommendation Agent
        self.allopathic_diagnostic_recommendation_specialist_task = Task(
            description=dedent(
                            """ 
                            1. Analyze input context : {analysis_result}, Thoroughly analyze provided medical reports.   
                            2. Depending on the provided medical report, you need to provide the medication regimens with dosages, routes of administration, duration, etc.
                            3. Chemical composition of the suggested Medication. 
                            4. Alternative treatments if deemed appropriate.
                            5. Further diagnostic tests or follow-up actions if necessary.
                            6. Stick on to allopathic treatment approach only.
                            7. Further diagnostic tests or follow-up actions if necessary.
                            8. Provide list top 5 allopathic hospitals to undergo suggested treatment in Karnataka
                            9. Always use authentic websites realated to allopathic diagnostic recommendation when pulling required datas.
                            10. Always provided respone as per the format in expected_output.                            
                            """
                ),
            agent=allopathicDiagnosticRecommendationAgent,
            expected_output=dedent(
                                """
                                    {
                                    "AllopathicDiagnostics": {
                                        "ReportType": "[Report Type]",
                                        "PatientDetails": {
                                        "Name": "[Patient Name]",
                                        "Age": "[Patient Age]",
                                        "Sex": "[Patient Sex]",
                                        "ReportID": "[Report ID]",
                                        "SampleCollectedDate": "[Sample Collection Date]",
                                        "ReportDate": "[Report Date]"
                                        },
                                        "ConfirmedCondition": {
                                        "Findings": [
                                            {
                                            "Condition": "[Condition]"
                                            }
                                        ]
                                        },
                                        "SupportingEvidence": {
                                        "Evidence": [
                                            {
                                            "DiagnosticEvidence": "[Diagnostic Evidence]",
                                            "ClinicalEvidence": "[Clinical Evidence]"
                                            }
                                        ]
                                        },
                                        "ExclusionofDifferentialDiagnoses": [
                                        {
                                            "Condition": "[Potential Condition]"
                                        }
                                        ],
                                        "Summary": "[Summary of key findings]"
                                    },
                                    "MedicationRecommendation": {
                                        "SuggestedMedicationRegimens": [
                                        {
                                            "Medication": "[Medicine Name]",
                                            "MedicationType": "[Medicine type e.g., Tablet, Syrup, Injection]",
                                            "Dosage": "[Dosage as necessary]",
                                            "RouteofAdministration": "[Usage]",
                                            "Duration": "[Duration of medicine intake]",
                                            "Rationale": "[Reason for using this Medicine]",
                                            "ChemicalComposition": "[Detailed chemical composition present within this Medicine with the chemical formula]"
                                        }
                                        ]
                                    },
                                    "MonitoringandFurtherDiagnosticTests": {
                                        "FurtherDiagnosticTests": [
                                        {
                                            "MedicalTest": "[Medical test Name]",
                                            "NextFollowupUp": "[Next followup day]",
                                            "Referral": "[Referral department for medical test]"
                                        }
                                        ],
                                        "TopHospitalsforTreatment": [
                                        {
                                            "Name": "[Hospital Name, Address]",
                                            "Specialty": "[Specialty]",
                                            "Website": "[Website]"
                                        }
                                        ]
                                    },
                                    "Disclaimer": "This treatment plan is based on the provided medical report and should be discussed with a healthcare provider for personalized medical advice. Regular monitoring and adjustments may be necessary based on the patient's response to treatment."
                                    }       

                                """                
            ),
         )