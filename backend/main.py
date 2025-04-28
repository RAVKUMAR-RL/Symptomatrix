from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from dotenv import load_dotenv
from agents.medical_image_analysis_agent import ImageAnalysisHelperAgent as ImageAnalysisAgent
import json
import uuid
from crew import CrewClass as MedicalAnalysisCrew



# Load environment variables from a .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# Create FastAPI instance
app = FastAPI()

# Enable Cross-Origin Resource Sharing (CORS) middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allow requests from any origin
    allow_methods=["*"],    # Allow all HTTP methods
    allow_headers=["*"],    # Allow all headers
)


# Directory where uploaded images will be stored
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)      # Create directory if it does not exist

# Initialize medical image analysis agent
analyzer = ImageAnalysisAgent()

@app.get("/")
async def root():
    """
    Root endpoint to check if the medical chatbot backend is running.
    """
    return {"message": "Medical Chatbot Backend is up and running!"}


@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    """
    Endpoint to analyze uploaded medical images.
    - Ensures the file type is valid.
    - Saves the uploaded file.
    - Performs image analysis using GPT-4o mini model.
    - Retrieves multiple treatment options in kannada an Hindi languages.
    - Retrieves analysis and recommendation based on allopathic, ayurvedic and modren integrative treatments.
    - Retrieves diet plan.
    - Deletes the file after processing.
    """    
    
    # Check if the file type is jpeg, png, or jpg
    allowed_extensions = {"jpeg", "png", "jpg"}
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Only jpeg, png, and jpg are allowed."
        )
    
   # Save the uploaded file with a unique identifier to avoid overwriting
    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename )
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    try:
        # Analyze the uploaded image using GPT-4o mini model

        analysis_result = analyzer.call_gpt4_model_for_analysis(file_path)
        print("Image Analysis Completed")
        
        # Prepare input data for crew kickoff
        input_data = {"analysis_result": analysis_result}

        # Create a new crew instance for every request to handle various analysis tasks
        medical_crew = MedicalAnalysisCrew()
        crew = medical_crew.get_crew()
        
         # Trigger the crew kickoff
        try:
            result = crew.kickoff(input_data)
        except Exception as crew_error:
            raise HTTPException(status_code=500, detail=f"Crew kickoff failed: {str(crew_error)}")
        
        
        # Parse JSON results from analysis and crew tasks
        try:
            parsed_data_english = json.loads(analysis_result)       # Image analysis in English
            parsed_data_kannada = json.loads(result.tasks_output[0].raw)        # Kannada translation
            parsed_data_hindi = json.loads(result.tasks_output[1].raw)      # Hindi translation
            parsed_data_allopathic_treatment = json.loads(result.tasks_output[2].raw)   # Allopathic treatment recommendations
            parsed_data_ayurvedic_treatment = json.loads(result.tasks_output[3].raw)    # Ayurvedic treatment recommendations
            parsed_data_modern_treatment = json.loads(result.tasks_output[4].raw)       # Modern treatment approaches
            parsed_data_advanced_diet_plan = json.loads(result.tasks_output[5].raw)     # Diet recommendations
        except json.JSONDecodeError as json_error:
            raise HTTPException(status_code=500, detail=f"Error decoding task output JSON: {str(json_error)}")
             
             
        # Return all parsed data in the response
        return {
                "image_analysis_english": parsed_data_english,
                "image_analysis_kannada": parsed_data_kannada,
                "image_analysis_hindi": parsed_data_hindi,
                "allopathic_treatment": parsed_data_allopathic_treatment,
                "ayurvedic_treatment": parsed_data_ayurvedic_treatment,
                "modren_treatment": parsed_data_modern_treatment,
                "advanced_diet_plan": parsed_data_advanced_diet_plan,
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Ensure the uploaded file is deleted after processing to free storage
        if os.path.exists(file_path):
            os.remove(file_path)