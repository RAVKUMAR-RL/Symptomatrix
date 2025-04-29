# 🏥 Medical Image Analysis

## 📌 Overview
The **Medical Image Analysis** is an AI-powered system built using **FastAPI**. It allows users to upload medical images, analyze them with **GPT-4**, and receive treatment recommendations in multiple languages. The project aims to assist healthcare professionals in **diagnosing conditions** and suggesting relevant treatments using **AI-driven insights**.

## 🌟 Features
✅ AI-powered **medical image analysis** using **GPT-4o-mini**  
✅ Supports **JPEG, PNG, and JPG** file formats  
✅ Provides analysis in **English, Kannada, and Hindi**  
✅ Suggests **Allopathic, Ayurvedic, and Modern treatments**  
✅ Generates **Advanced Diet Plans** based on analysis  
✅ Implements **secure file handling** and cleanup  

## 🏗️ Technology Stack
The project leverages the following technologies:  
- **FastAPI** – Lightweight and high-performance API framework  
- **Python** – Backend programming language  
- **OpenAI GPT-40-mini** – AI-powered image interpretation  
- **Crew AI** – Task orchestration for medical analysis  
- **Dotenv** – Manages environment variables securely  
- **UUID** – Generates unique identifiers for image uploads  
- **JSON** – Handles structured data responses  


## ⚙️ Setup Instructions
### 🔹 Prerequisites
Ensure you have the following installed before proceeding:  
- **Python 3.8 or later**  
- **pip (Python Package Installer)**  
- **virtualenv** (optional but recommended)  

### 🔹 Installation Steps
1. **Clone the repository:**  
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>

2. **Create a virtual environment (optional, recommended):**
    python -m venv venv
    source venv/bin/activate  ( On Windows: venv\Scripts\activate)

3. **Install dependencies:**
    pip install -r requirements.txt

4. **Set up environment variables:**
    OPENAI_API_KEY=<your-openai-api-key>
    SERPER_API_KEY=<your-openai-api-key>   **Use the link to Signup and have Serper API Key https://serper.dev/login**

5. **Run the server:**
    uvicorn main:app --reload

6. **Access the API:**
    - Visit http://127.0.0.1:8000/ to check if the backend is running
    - Use the http://127.0.0.1:8000/analyze/ endpoint to upload and analyze images


## 🏥 Usage Guide
   - **How to analyze medical images:**
    Send a POST request to /analyze/  with an image file.
    The system processes the image and provides AI-generated insights.
    Responses include diagnosis interpretations and treatment suggestions.

    **Exmple Using cURL**
    curl -X POST "http://127.0.0.1:8000/analyze/" -F "file=@image.jpg"

    **Exmple Using Postman**
    Launch the Postman application.
    Click on "New" → "Request".
    Choose POST as the HTTP method.
    Enter the API endpoint:http://127.0.0.1:8000/analyze/
    Go to the Headers tab.
    Verify or Add the following key-value pair:
        Key: Content-Type
        Value: multipart/form-data
    Go to Body → Select "form-data".
        Key:  file(Make sure it's set to File )
        Value: Choose a JPEG, PNG, or JPG file from your system.
        Click the Send button.


## 🔒 Security & Best Practices
    ✅ Secure File Handling: Uploaded images are saved with unique identifiers to prevent conflicts.
    ✅ Automatic Cleanup: Images are deleted after processing to free up storage and maintain privacy.
    ✅ Validated File Types: The system only accepts JPEG, PNG, and JPG to avoid unsupported formats.

## 🎯 Future Improvement
    🔹 Enhancing AI models for more accurate image analysis
    🔹 Expanding language support for wider accessibility
    🔹 Optimizing performance to process large medical dataset

# UI Prerequisites

## Install Vue.js - version 3

https://vueframework.com/guide/installation.html#release-notes

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run dev
```


## 👥 Contributors
    🔹 Name - RaviKumar G
    🔹 Name - Ramya K
