from crewai import Task
from textwrap import dedent
from dotenv import load_dotenv
from agents.advanced_diet_wellness_consultant_agent import AdvancedDietWellnessConsultantAgentClass

load_dotenv()

# Instance of AdvancedDietWellnessConsultantAgentClass to pass as agent parameter value to task
advancedDietWellnessConsultantAgent = AdvancedDietWellnessConsultantAgentClass().advanced_diet_wellness_consultant

class AdvancedDietWellnessConsultantAgentTaskClass:
    def __init__(self):  
        
      # Task related to advanced diet wellnessconsultant Agent
        self.advanced_diet_wellness_consultant_task = Task(
            description=dedent(
                        """ 
                            Analyze input context : {analysis_result}, thoroughly analyze provided medical reports.
                            To generate a diet plan based on the medical reports, health goals, and dietary preferences, incorporating Allopathic, Ayurvedic, and Modern Integrative approaches.
                            1. Recommend meal timing, portion sizes, hydration, and food combinations.
                            2. Highlight foods to include and avoid for optimal health.
                            3. Ensure cultural and lifestyle compatibility with dietary recommendations.
                            4. Analyze user inputs to determine nutritional needs.
                            5. Accommodate different dietary philosophies while ensuring the output adheres to structured and practical guidelines.
                            6. Ensure the diet plan aligns with the user medical conditions and health goals.
                            7. Respect dietary restrictions, allergies, and cultural preferences.
                            8. Use evidence-based recommendations for each approach.
                            9. Apply distinct principles of:
                                a. Allopathy: Focus on macronutrient ratios, caloric needs, and evidence-based dietary practices.
                                b. Ayurveda: Assess user dosha constitution (Vata, Pitta, Kapha) and suggest dosha-balancing foods.
                                c. Modern Integrative: Blend conventional and holistic nutritional approaches with functional foods.
                                
                            10. Based on this analysis, develop personalized recommendations encompassing dietary guidelines.                      
                            11. Always use authentic websites realated to diet plans when pulling required datas.
                            12. Always follow structured output format in a JSON format provided in expected_output document.
                        """
                ),
            agent=advancedDietWellnessConsultantAgent,
            expected_output=dedent(
                                """ 
                                     {
                                        "AllopathicDietPlan": {
                                            "Focus": "[Focus of the plan, e.g., nutritional balance for specific health conditions]",
                                            "guidelines": "[Ingredients content to control Ex-Low sodium intake, Controlled protein consumption, Adequate hydration]",
                                            "Meals": {
                                            "Breakfast": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "NutritionalValue": "[Calories, Protein, etc.]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Snack": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Snack Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "NutritionalValue": "[Calories, Protein, etc.]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Lunch": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "NutritionalValue": "[Calories, Protein, etc.]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Dinner": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "NutritionalValue": "[Calories, Protein, etc.]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ]
                                            },
                                            "foodstoavoid": "[List of foods to avoid]",
                                            "KeyPrinciples": "[Brief description of dietary principles, e.g., high protein, low saturated fat]",
                                            "cooking_style": "[Cooking method used]"
                                        },
                                        "AyurvedicDietPlan": {
                                            "Focus": "[Focus of the plan, e.g., balancing the doshas and promoting digestion]",
                                            "guidelines": "[Ingredients content to control as per Ayurvedic principles]",
                                            "Meals": {
                                            "Breakfast": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "DoshaEffect": "[Effect on Doshas, e.g., pacifies Vata]",
                                                "Ingredients": "[List of Ingredients]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Snack": [
                                                {
                                                "mealtime": "[Time]",
                                                "SnackItem": "[Snack Name]",
                                                "DoshaEffect": "[Effect on Doshas]",
                                                "Ingredients": "[List of Ingredients]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Lunch": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "DoshaEffect": "[Effect on Doshas]",
                                                "Ingredients": "[List of Ingredients]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Dinner": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "DoshaEffect": "[Effect on Doshas]",
                                                "Ingredients": "[List of Ingredients]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ]
                                            },
                                            "foodsstoavoid": "[List of foods to avoid]",
                                            "KeyPrinciples": "[Brief description of dietary principles, e.g., include all six tastes, warm and seasonal foods]",
                                            "cooking_style": "[Cooking method used]"
                                        },
                                        "ModernIntegrativeDietPlan": {
                                            "Focus": "[Focus of the plan, e.g., anti-inflammatory and gut-friendly foods]",
                                            "Meals": {
                                            "Breakfast": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "Benefits": "[Benefits, e.g., rich in antioxidants]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Snack": [
                                                {
                                                "mealtime": "[Time]",
                                                "SnackItem": "[Snack Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "Benefits": "[Benefits, e.g., promotes gut health]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Lunch": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "Benefits": "[Benefits, e.g., high in fiber]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ],
                                            "Dinner": [
                                                {
                                                "mealtime": "[Time]",
                                                "Dish": "[Dish Name]",
                                                "Ingredients": "[List of Ingredients]",
                                                "Benefits": "[Benefits, e.g., anti-inflammatory properties]",
                                                "ingredientstoavoid": "[Ingredients to avoid]"
                                                }
                                            ]
                                            },
                                            "foodstoavoid": "[List of foods to avoid]",
                                            "KeyPrinciples": "[Brief description of dietary principles, e.g., balance macronutrients, include fermented foods]",
                                            "cooking_style": "[Cooking method used]"
                                        },
                                        "Disclaimer": "These diet plans are generic examples based on respective dietary philosophies. Consult a qualified healthcare professional or nutritionist for personalized recommendations."
                                        }
                                    
                                """                
            ),       
        )