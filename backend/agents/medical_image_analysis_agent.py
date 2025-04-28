import os
import base64
from fastapi import HTTPException
from openai import OpenAI
from dotenv import load_dotenv
from crewai_tools import VisionTool

# Load the .env file to recieve system prompt file path
load_dotenv()

# Get the template path from the .env file
template_path = os.getenv('TEMPLATE_PATH')


# Method to pull system_prompt for the agent
staticmethod 
def load_prompt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# CrewAI tool helps to analyze Image
vision_tool=VisionTool()

class ImageAnalysisHelperAgent:
    def __init__(self):
        
        self.client = OpenAI()
        
    #Encodes an image to base64 format.  
    def encode_image(self, image_path: str) -> str:
    
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to encode image: {str(e)}")
        
        
    # Calls the GPT-4o-mini model to analyze the medical image.
    def call_gpt4_model_for_analysis(self, file: str) -> str:
        print("Image Analysis Started")
        
        base64_image = self.encode_image(file)
        system_prompt = load_prompt(template_path)

        messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text", "text": system_prompt
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "high"
                        }
                    }
                ]
            }
        ]

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=1500,    # Restricting max token for the LLM model.
                response_format={"type": "json_object"}     # mapping output format as json.
            )
            return response.choices[0].message.content
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error during model analysis: {str(e)}")
