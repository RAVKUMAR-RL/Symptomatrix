<template>
    <div class="min-h-screen bg-gradient-to-r from-blue-50 to-green-100 relative overflow-hidden">
      <!-- Background Design -->
      <div class="absolute top-0 right-0 w-[500px] h-[500px] -mt-40 -mr-40 bg-teal-300 rounded-full opacity-30 animate-pulse"></div>
      <div class="absolute top-0 right-0 w-[300px] h-[300px] -mt-20 -mr-10 bg-teal-200 rounded-full opacity-50 animate-pulse"></div>
  
     <div class="max-w-[1450px] mx-auto p-6 bg-gradient-to-r from-white via-blue-50 to-green-50 rounded-2xl shadow-2xl shadow-blue-200 mt-10 relative z-10 animate-expand border border-teal-300"
        style="max-height: 93vh; min-height:93vh;margin-top: 25px;">
        <!-- Main Container (Top) -->
        <div>
          <!-- Header Section -->
          <div class="relative mb-8 p-6 pb-16 bg-blue-50 rounded-t-2xl shadow-inner overflow-hidden" style="margin-bottom: 5px; padding-bottom: 5px; padding-top: 5px;"> 
        <!-- Wavy Line SVG -->
        <svg class="absolute top-0 right-0 w-1/2 h-full -mr-10 -mt-4 opacity-40" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
          <path fill="#61A0FF" fill-opacity="0.3" d="M0,128L120,122.7C240,117,480,107,720,117.3C960,128,1200,160,1320,176L1440,192L1440,320L1320,320C1200,320,960,320,720,320C480,320,240,320,120,320L0,320Z"></path>
        </svg>
    
      <!-- Home Button -->
      <div class="absolute top-6 left-6 z-20 group">
          <!-- Home Icon with Tooltip -->
          <div class="relative">
              <img 
                  @click="$router.push('/')" 
                  src="@/assets/home.png" 
                  alt="Home" 
                  class="w-12 h-12 cursor-pointer transition-transform transform hover:scale-110 duration-300 ease-in-out"
                  style="border: none; background-color: transparent;"
              />
              <!-- Tooltip -->
              <div 
                  class="absolute left-14 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white text-xs rounded px-2 py-1 opacity-0 group-hover:opacity-100 transition-opacity duration-300 ease-in-out">
                  Home
              </div>
          </div>
      </div>

      <!-- Doctor Image (Aligned Top-Right) -->
      <div class="absolute top-2 right-6 z-20">
          <img src="@/assets/doctor.jpg" alt="Doctor Icon" 
              class="w-20 h-20 rounded-full border-2 border-white shadow-lg transition-transform transform hover:scale-105 cursor-pointer" />
      </div>

      <!-- Stylish Header -->
      <div class="flex items-center justify-center w-full">
        <!-- Brand Logo -->
        <img src="@/assets/RL_profile.jpg" alt="Symptomatrix Logo" class="brand-logo" />

        <!-- Title and Subtitle -->
        <div class="ml-4 text-center">
          <h1 class="text-5xl stylish-text relative z-10 text-center"
              style="background: linear-gradient(90deg, #1E3C72, #2A5298, #4A69BB);
                    background-clip: text; -webkit-text-fill-color: transparent; 
                    text-shadow: 0px 0px 8px rgba(30, 60, 114, 0.4);
                    padding-bottom: 5px;">
            Symptomatrix
          </h1>
          <p class="text-gray-700 text-sm">Catalyzing Transformative Care</p>
        </div>
      </div>   
    
  
      <!-- Center Wavy Shape (SVG) -->
      <div class="absolute inset-0 flex items-center justify-center">
          <svg width="100%" height="100%" viewBox="0 0 1440 320" class="opacity-20">
            <path fill="#61A0FF" fill-opacity="0.3" d="M0,160L80,176C160,192,320,224,480,202.7C640,181,800,107,960,74.7C1120,43,1280,53,1360,58.7L1440,64L1440,0L1360,0C1280,0,1120,0,960,0C800,0,640,0,480,0C320,0,160,0,80,0L0,0Z"></path>
          </svg>
      </div>
    </div>
          <div class="flex items-center justify-between w-full mt-4 relative z-10">
                  <!-- Left Section -->
                  <div class="ml-4">
                    <h1 class="text-xl font-bold text-blue-800">Comprehensive Health Re Analysis</h1>
                  </div>    
                  
          </div>
          <!-- Tabs -->
          <div class="flex items-center justify-start mb-4 p-2 rounded-t-lg shadow-inner bg-gradient-to-r from-blue-100 to-green-100 relative overflow-hidden">
            <div 
              v-for="tab in tabs" 
              :key="tab"
              @click="activeTab = tab"
              :class="[ 'cursor-pointer px-6 py-2 transition-all duration-300 text-sm relative z-10',
                activeTab === tab ? 'bg-gradient-to-r from-teal-400 to-blue-500 text-white font-bold rounded-md shadow-lg transform scale-105' : 'text-gray-600 hover:text-blue-700'
              ]"
              style="margin-right: 8px; padding: 8px 16px; border-radius: 8px;"
            >
              {{ tab }}
            </div>
          </div>
  
  
          <!-- Tab Content -->
          <transition name="fade" mode="out-in">
            <!-- Ask AI Tab -->
            <div v-if="activeTab === 'Ask AI'" 
            style="display: flex; align-items: center; justify-content: space-between; height: 400px;">
          
            <!-- Card 1: Icons and Uploaded Image -->
            <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-gray-300 transition-all duration-500 flex items-center justify-center"
                style="width: 48%; height: 100%; display: flex; align-items: center;">
                
                <!-- Icons Section (Upload & Analyze) -->
                <div style="display: flex; flex-direction: column; align-items: flex-start; margin-right: 20px;">
                    <div class="flex items-center space-x-4 mb-4">
                        <!-- Upload Icon -->
                        <div class="relative group cursor-pointer">
                        <label for="file-upload" class="cursor-pointer">
                            <img src="@/assets/upload.png" alt="Upload" class="w-12 h-12 transition-transform transform hover:scale-105" 
                                @click="showAuthorizationMessage" />
                        </label>
                        <input id="file-upload" type="file" @change="onFileChange" accept="image/*" class="hidden" />
                        <!-- Tooltip -->
                        <div class="absolute bottom-full mb-2 left-1/2 transform -translate-x-1/2 px-3 py-1 text-xs text-white bg-black bg-opacity-75 rounded-md shadow-lg transition-opacity duration-300 opacity-0 group-hover:opacity-100">
                                        Upload Image
                                    </div>
                                </div>
                        <!-- Analyze Icon -->
                        <div class="relative group cursor-pointer">
                        <button @click="showConsentPopup = true" 
                                class="flex items-center justify-center transition-transform transform hover:scale-105">
                            <img src="@/assets/inspection.png" alt="Analyze" class="w-12 h-12" />
                        </button>
                        <!-- Tooltip -->
                    <div class="absolute bottom-full mb-2 left-1/2 transform -translate-x-1/2 px-3 py-1 text-xs text-white bg-black bg-opacity-75 rounded-md shadow-lg transition-opacity duration-300 opacity-0 group-hover:opacity-100">
                        Analyze Image
                    </div>
                </div>
                    </div>
                </div>

                <!-- Uploaded Image Display -->
                <div v-if="imageUrl" 
                    class="relative group"
                    style="max-width: 375px; max-height: 375px; overflow: hidden; border-radius: 10px;">
                    <img :src="imageUrl" 
                        alt="Uploaded Image" 
                        class="w-full h-full object-contain cursor-pointer transition-transform transform hover:scale-105"
                        @click="showImagePopup = true" />
                </div>
            </div>

            <!-- Card 2: Response Display -->
            <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-gray-300 transition-all duration-500 flex items-center justify-center"
                style="width: 48%; height: 100%;">
                <div class="text-sm text-gray-600 whitespace-pre-wrap text-center">
                    {{ textContent || displayMessage || "Kindly Upload image for analysis" }}
                </div>
            </div>

            <!-- Image Popup for Zooming -->
            <div v-if="showImagePopup" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50">
                <div class="relative">
                    <!-- Enhanced X Mark -->
                    <button @click="showImagePopup = false" 
                            class="absolute top-2 right-2 text-red-500 text-3xl font-bold transition-transform transform hover:scale-110 hover:text-red-700">
                        ✕
                    </button>
                    <img :src="imageUrl" alt="Zoomed Image" class="max-w-full max-h-screen rounded shadow-lg" />
                </div>
            </div>
            
        <!-- Stylish Authorization Message (New Addition) -->
        <div v-if="showAuthorization" class="fixed top-1/4 left-1/2 transform -translate-x-1/2 z-50">
            <div class="relative text-white text-xl font-bold py-3 px-6 rounded-full shadow-lg animate-bounce-glow bg-gradient-to-r from-purple-500 to-indigo-500 border border-white">
                You are Authorized
                <div class="absolute -inset-1 bg-gradient-to-r from-pink-500 to-purple-500 blur-xl opacity-50 rounded-full"></div>
            </div>
        </div>

            <!-- Consent Popup -->
            <div v-if="showConsentPopup" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50">
                <div class="bg-white p-6 rounded shadow-lg text-center w-96">
                    <h2 class="text-lg font-bold mb-4">Consent Required</h2>
                    <p class="text-gray-700 mb-4">We will proceed uploading image for analysis. Click " Accept " to proceed ?</p>
                    <div class="flex justify-around">
                        <button @click="acceptConsent"
                                class="px-4 py-2 bg-green-500 text-white rounded-full transition transform hover:scale-105">
                            Accept
                        </button>
                        <button @click="showConsentPopup = false"
                                class="px-4 py-2 bg-red-500 text-white rounded-full transition transform hover:scale-105">
                            Decline
                        </button>
                    </div>
                </div>
            </div>
            </div>

            <!--  Summary Tab -->
            <div v-else-if="activeTab === 'Summary' && analysisData.image_analysis_english">
                      <div v-if="Object.keys(analysisData.image_analysis_english).length > 0" class="grid grid-cols-3 gap-6 mt-4">
                        
                        <!-- Clinical Observations -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-blue-300 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto; filter: none !important; backdrop-filter: none;">
                          <h2 class="text-lg font-bold text-blue-800">Clinical Observations</h2>
                          <ul class="mt-2 space-y-2">
                            <li v-for="(finding, index) in analysisData.image_analysis_english.ClinicalObservations?.Findings || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ finding.Parameter }}:</strong> {{ finding.Result }} ({{ finding.Observation }})
                            </li>
                          </ul> 
                          <ul class="mt-2 space-y-2">
                          <p class="text-gray-700">
                            <strong>Summary:</strong> {{ analysisData.image_analysis_english.ClinicalObservations?.Summary || "Summary Unavialable." }}
                          </p>
                        </ul>
                        </div>

                        <!-- Diagnosis Impression -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-red-400 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto;">
                          <h2 class="text-lg font-bold text-yellow-600">Diagnosis Impression</h2>
                          <ul class="mt-2">
                            <li v-for="(condition, index) in analysisData.image_analysis_english.DiagnosisImpression?.Conditions || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ condition.Condition }}:</strong> {{ condition.Evidence }}
                            </li>
                          </ul>
                          <h3 class="text-md font-semibold mt-4 text-yellow-600">Differential Diagnoses</h3>
                          <ul class="mt-2">
                            <li v-for="(diagnosis, index) in analysisData.image_analysis_english.DiagnosisImpression?.DifferentialDiagnoses || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ diagnosis.Condition }}:</strong> {{ diagnosis.Reason }}
                            </li>
                          </ul>
                          <h3 class="text-md font-semibold mt-4 text-yellow-600">Guidelines Reference</h3>
                          <ul class="mt-2">
                            <p class="text-gray-700">
                            {{ analysisData.image_analysis_english.DiagnosisImpression?.GuidelinesReference || "Guidelines Reference Unavialable." }}
                          </p>
                          </ul>
                        </div>

                        <!-- Prognosis -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-red-400 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto;">
                          <h2 class="text-lg font-bold text-red-600">Prognosis</h2>
                          <p class="text-gray-700">
                            <strong>Clinical Correlation:</strong> {{ analysisData.image_analysis_english.Prognosis?.ClinicalCorrelation || "No correlation available." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>Recovery Chances:</strong> {{ analysisData.image_analysis_english.Prognosis?.RecoveryChances || "Not specified." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>Expected Progression:</strong> {{ analysisData.image_analysis_english.Prognosis?.ExpectedProgression || "Unknown progression." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>Survival Rates:</strong> {{ analysisData.image_analysis_english.Prognosis?.SurvivalRates || "Unknown progression." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>Quality of Life:</strong> {{ analysisData.image_analysis_english.Prognosis?.QualityofLife || "Unknown progression." }}
                          </p>
                        </div>

                        <!-- Confidence Level -->
                        <div class="col-span-3 p-4 bg-white rounded-2xl shadow-lg border-t-4 border-green-400"
                        style="max-height: 100px; min-height: 100px;">
                          <h2 class="text-lg font-bold text-green-600">Confidence Level</h2>
                          <p class="text-gray-700">{{ analysisData.image_analysis_english.ConfidenceLevel?.Percentage }} - {{ analysisData.image_analysis_english.ConfidenceLevel?.Explanation }}</p>
                          <p class="text-gray-700" style="font-size:small;font-style: italic;font-variant: normal;">
                            <strong class="text-red-500">Medical Disclaimer:</strong>{{ analysisData.image_analysis_english.Disclaimer}}
                          </p>                            
                        </div>
                      </div>

                      <!-- Placeholder if No Data -->
                      <div v-else class="p-6 bg-white rounded-xl shadow-md text-center text-gray-600">
                        No analysis data available. Please upload a report for validation.
                      </div>
            </div>

            <!--  ಸಾರಾಂಶ Tab -->
            <div v-else-if="activeTab === 'ಸಾರಾಂಶ' && analysisData.image_analysis_kannada">
                      <div v-if="Object.keys(analysisData).length > 0" class="grid grid-cols-3 gap-6 mt-4">
                        
                        <!-- Clinical Observations -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-blue-300 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto; filter: none !important; backdrop-filter: none;">
                          <h2 class="text-lg font-bold text-blue-800">ವೈದ್ಯಕೀಯ ವೀಕ್ಷಣೆಗಳು</h2>
                          <ul class="mt-2 space-y-2">
                            <li v-for="(finding, index) in analysisData.image_analysis_kannada.ClinicalObservations?.Findings || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ finding.Parameter }}:</strong> {{ finding.Result }} ({{ finding.Observation }})
                            </li>
                          </ul> 
                          <ul class="mt-2 space-y-2">
                          <p class="text-gray-700">
                            <strong>ಸಾರಾಂಶ:</strong> {{ analysisData.image_analysis_kannada.ClinicalObservations?.Summary || "Summary Unavialable." }}
                          </p>
                        </ul>
                        </div>

                        <!-- Diagnosis Impression -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-red-400 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto;">
                          <h2 class="text-lg font-bold text-yellow-600">ವೈದ್ಯಕೀಯ ನಿರ್ಣಯದ ಅಭಿಪ್ರಾಯ</h2>
                          <ul class="mt-2">
                            <li v-for="(condition, index) in analysisData.image_analysis_kannada.DiagnosisImpression?.Conditions || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ condition.Condition }}:</strong> {{ condition.Evidence }}
                            </li>
                          </ul>
                          <h3 class="text-md font-semibold mt-4 text-yellow-600">ವೈಕಲ್ಪಿಕ ನಿರ್ಣಯಗಳು</h3>
                          <ul class="mt-2">
                            <li v-for="(diagnosis, index) in analysisData.image_analysis_kannada.DiagnosisImpression?.DifferentialDiagnoses || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ diagnosis.Condition }}:</strong> {{ diagnosis.Reason }}
                            </li>
                          </ul>
                          <h3 class="text-md font-semibold mt-4 text-yellow-600">ಮಾರ್ಗಸೂಚಿ ಸಂಧರ್ಭ</h3>
                          <ul class="mt-2">
                            <p class="text-gray-700">
                            {{ analysisData.image_analysis_kannada.DiagnosisImpression?.GuidelinesReference || "Guidelines Reference Unavialable." }}
                          </p>
                          </ul>
                        </div>

                        <!-- Prognosis -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-red-400 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto;">
                          <h2 class="text-lg font-bold text-red-600">ಆರೋಗ್ಯದ ಮುನ್ಸೂಚನೆ </h2>
                          <p class="text-gray-700">
                            <strong>ವೈದ್ಯಕೀಯ ಸಂಬಂಧ:</strong> {{ analysisData.image_analysis_kannada.Prognosis?.ClinicalCorrelation || "No correlation available." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>ಚೇತರಿಕೆ ಸಾಧ್ಯತೆಗಳು:</strong> {{ analysisData.image_analysis_kannada.Prognosis?.RecoveryChances || "Not specified." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>ಕಾಂಕ್ಷಿತ ಪ್ರಗತಿ:</strong> {{ analysisData.image_analysis_kannada.Prognosis?.ExpectedProgression || "Unknown progression." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>ಜೀವ ಉಳಿಯುವ ಪ್ರಮಾಣ:</strong> {{ analysisData.image_analysis_kannada.Prognosis?.SurvivalRates || "Unknown progression." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>ಜೀವನದ ಗುಣಮಟ್ಟ:</strong> {{ analysisData.image_analysis_kannada.Prognosis?.QualityofLife || "Unknown progression." }}
                          </p>
                        </div>

                        <!-- Confidence Level -->
                        <div class="col-span-3 p-4 bg-white rounded-2xl shadow-lg border-t-4 border-green-400"
                        style="max-height: 100px; min-height: 100px;">
                          <h2 class="text-lg font-bold text-green-600">ಆತ್ಮವಿಶ್ವಾಸದ ಮಟ್ಟ</h2>
                          <p class="text-gray-700">{{ analysisData.image_analysis_kannada.ConfidenceLevel?.Percentage }} - {{ analysisData.image_analysis_kannada.ConfidenceLevel?.Explanation }}</p>
                          <p class="text-gray-700" style="font-size:small;font-style: italic;font-variant: normal;">
                            <strong class="text-red-500">ವೈದ್ಯಕೀಯ ಅಡಿಬಂಧನೆ:</strong>{{ analysisData.image_analysis_kannada.Disclaimer}}
                          </p> 
                        </div>
                      </div>

                      <!-- Placeholder if No Data -->
                      <div v-else class="p-6 bg-white rounded-xl shadow-md text-center text-gray-600">
                        ವಿಶ್ಲೇಷಣೆ ಮಾಹಿತಿಗಳು ಲಭ್ಯವಿಲ್ಲ. ದಯವಿಟ್ಟು ಮೌಲ್ಯಮಾಪನಕ್ಕಾಗಿ ವರದಿಯನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ.
                      </div>
            </div>

            <!--  सारांश Tab -->
            <div v-else-if="activeTab === 'सारांश' && analysisData.image_analysis_hindi">
                      <div v-if="Object.keys(analysisData).length > 0" class="grid grid-cols-3 gap-6 mt-4">
                        
                        <!-- Clinical Observations -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-blue-300 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto; filter: none !important; backdrop-filter: none;">
                          <h2 class="text-lg font-bold text-blue-800">नैदानिक अवलोकन</h2>
                          <ul class="mt-2 space-y-2">
                            <li v-for="(finding, index) in analysisData.image_analysis_hindi.ClinicalObservations?.Findings || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ finding.Parameter }}:</strong> {{ finding.Result }} ({{ finding.Observation }})
                            </li>
                          </ul> 
                          <ul class="mt-2 space-y-2">
                          <p class="text-gray-700">
                            <strong>सारांश:</strong> {{ analysisData.image_analysis_hindi.ClinicalObservations?.Summary || "Summary Unavialable." }}
                          </p>
                        </ul>
                        </div>

                        <!-- Diagnosis Impression -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-red-400 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto;">
                          <h2 class="text-lg font-bold text-yellow-600"> रोग निदान की धारणा</h2>
                          <ul class="mt-2">
                            <li v-for="(condition, index) in analysisData.image_analysis_hindi.DiagnosisImpression?.Conditions || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ condition.Condition }}:</strong> {{ condition.Evidence }}
                            </li>
                          </ul>
                          <h3 class="text-md font-semibold mt-4 text-yellow-600"> विभेदक निदान</h3>
                          <ul class="mt-2">
                            <li v-for="(diagnosis, index) in analysisData.image_analysis_hindi.DiagnosisImpression?.DifferentialDiagnoses || []" 
                                :key="index" class="text-gray-700">
                              <strong>{{ diagnosis.Condition }}:</strong> {{ diagnosis.Reason }}
                            </li>
                          </ul>
                          <h3 class="text-md font-semibold mt-4 text-yellow-600">दिशानिर्देश संदर्भ</h3>
                          <ul class="mt-2">
                            <p class="text-gray-700">
                            {{ analysisData.image_analysis_hindi.DiagnosisImpression?.GuidelinesReference || "Guidelines Reference Unavialable." }}
                          </p>
                          </ul>
                        </div>

                        <!-- Prognosis -->
                        <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-red-400 transition-all duration-500 cursor-pointer transform"
                        style="max-height: 300px; min-height: 300px; overflow-y: auto;">
                          <h2 class="text-lg font-bold text-red-600"> रोगपूर्वानुमान</h2>
                          <p class="text-gray-700">
                            <strong>नैदानिक सहसंबंध.:</strong> {{ analysisData.image_analysis_hindi.Prognosis?.ClinicalCorrelation || "No correlation available." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>स्वास्थ्य लाभ की संभावना:</strong> {{ analysisData.image_analysis_hindi.Prognosis?.RecoveryChances || "Not specified." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>अपेक्षित प्रगति:</strong> {{ analysisData.image_analysis_hindi.Prognosis?.ExpectedProgression || "Unknown progression." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>जीवित रहने की दरें:</strong> {{ analysisData.image_analysis_hindi.Prognosis?.SurvivalRates || "Unknown progression." }}
                          </p>
                          <p class="text-gray-700">
                            <strong>जीवन की गुणवत्ता:</strong> {{ analysisData.image_analysis_hindi.Prognosis?.QualityofLife || "Unknown progression." }}
                          </p>
                        </div>

                        <!-- Confidence Level -->
                        <div class="col-span-3 p-4 bg-white rounded-2xl shadow-lg border-t-4 border-green-400"
                        style="max-height: 100px; min-height: 100px;">
                          <h2 class="text-lg font-bold text-green-600">आत्मविश्वास का स्तर</h2>
                          <p class="text-gray-700">{{ analysisData.image_analysis_hindi.ConfidenceLevel?.Percentage }} - {{ analysisData.image_analysis_hindi.ConfidenceLevel?.Explanation }}</p>
                          <p class="text-gray-700" style="font-size:small;font-style: italic;font-variant: normal;">
                            <strong class="text-red-500">चिकित्सा अस्वीकरण:</strong>{{ analysisData.image_analysis_hindi.Disclaimer}}
                          </p> 
                        </div>
                      </div>

                      <!-- Placeholder if No Data -->
                      <div v-else class="p-6 bg-white rounded-xl shadow-md text-center text-gray-600">
                        विश्लेषण जानकारी उपलब्ध नहीं है। कृपया मूल्यांकन के लिए रिपोर्ट अपलोड करें।
                      </div>
            </div>
            
            <!--  Allopathic Recommendation Tab -->
            <div v-else-if="activeTab === 'Allopathic Recommendation' && analysisData.allopathic_treatment">
                <div v-if="Object.keys(analysisData.allopathic_treatment).length > 0" class="grid grid-cols-3 gap-6 mt-4">
                  
                  <!-- Allopathic Diagnostics -->
                  <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-blue-400 transition-all duration-500 cursor-pointer transform"
                      style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                    
                    <h2 class="text-lg font-bold text-blue-800">Allopathic Diagnosis</h2>

                    <!-- Patient Details -->
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500 mb-3">
                      <p><strong class="text-blue-700">Report Type:</strong> {{ analysisData.allopathic_treatment.AllopathicDiagnostics.ReportType }}</p>
                      <p><strong class="text-blue-700">Patient Name:</strong> {{ analysisData.allopathic_treatment.AllopathicDiagnostics.PatientDetails.Name }}</p>
                      <p><strong class="text-blue-700">Age:</strong> {{ analysisData.allopathic_treatment.AllopathicDiagnostics.PatientDetails.Age }}</p>
                      <p><strong class="text-blue-700">Sex:</strong> {{ analysisData.allopathic_treatment.AllopathicDiagnostics.PatientDetails.Sex }}</p>
                    </div>

                    <!-- Confirmed Conditions -->
                    <h6 class="font-semibold mt-2 text-blue-700">Confirmed Condition:</h6>
                    <ul>
                      <li v-for="(med, index) in analysisData.allopathic_treatment.AllopathicDiagnostics.ConfirmedCondition.Findings" 
                          :key="index"
                          class="bg-gray-100 p-3 mb-2 rounded-lg shadow-md border-l-4 border-blue-500">
                        <strong class="text-blue-700">Condition:</strong> {{ med.Condition }}
                      </li>
                    </ul>

                    <!-- Supporting Evidence -->
                    <h6 class="font-semibold mt-2 text-blue-700">Supporting Evidence:</h6>
                    <ul>
                      <li v-for="(med, index) in analysisData.allopathic_treatment.AllopathicDiagnostics.SupportingEvidence.Evidence" 
                          :key="index"
                          class="bg-gray-100 p-3 mb-2 rounded-lg shadow-md border-l-4 border-blue-500">
                        <p><strong class="text-blue-700">Diagnostic Evidence:</strong> {{ med.DiagnosticEvidence }}</p>
                        <p><strong class="text-blue-700">Clinical Evidence:</strong> {{ med.ClinicalEvidence }}</p>
                      </li>
                    </ul>

                    <!-- Exclusion of Differential Diagnoses -->
                    <h6 class="font-semibold mt-2 text-blue-700">Exclusion of Differential Diagnoses:</h6>
                    <ul>
                      <li v-for="(med, index) in analysisData.allopathic_treatment.AllopathicDiagnostics.ExclusionofDifferentialDiagnoses" 
                          :key="index"
                          class="bg-gray-100 p-3 mb-2 rounded-lg shadow-md border-l-4 border-red-500">
                        <strong class="text-blue-700">Condition:</strong> {{ med.Condition }}
                      </li>
                    </ul>

                    <!-- Summary -->
                    <h6 class="font-semibold mt-2 text-blue-700">Exclusion of Differential Diagnoses:</h6>
                    <ul>
                    <p class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500">
                      <strong class="text-blue-700">Summary:</strong> {{ analysisData.allopathic_treatment.AllopathicDiagnostics.Summary }}
                    </p>
                    </ul>
                  </div>


                  <!-- Medication Recommendation -->
                  <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-green-400 transition-all duration-500 cursor-pointer transform"
                      style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                    <h2 class="text-lg font-bold text-green-600">Medication Recommendation</h2>

                    <div v-for="(med, index) in analysisData.allopathic_treatment.MedicationRecommendation.SuggestedMedicationRegimens" 
                        :key="index"
                        class="bg-gray-100 p-3 mb-3 rounded-lg shadow-md border-l-4 border-green-500">
                      <p><strong class="text-green-700">Medication:</strong> {{ med.Medication }}</p>
                      <p><strong class="text-green-700">Medication Type:</strong> {{ med.MedicationType }}</p>
                      <p><strong class="text-green-700">Dosage:</strong> {{ med.Dosage }}</p>
                      <p><strong class="text-green-700">Route:</strong> {{ med.RouteofAdministration }}</p>
                      <p><strong class="text-green-700">Duration:</strong> {{ med.Duration }}</p>
                      <p><strong class="text-green-700">Rationale:</strong> {{ med.Rationale }}</p>
                      <p><strong class="text-green-700">Chemical Composition:</strong> {{ med.ChemicalComposition }}</p>
                    </div>
                    <p class="text-gray-700" style="font-size:small;font-style: italic;font-variant: normal;">
                              <strong class="text-red-500">Medical Disclaimer:</strong>{{ analysisData.allopathic_treatment.Disclaimer }}
                    </p>
                  </div>


                  <!-- Monitoring & Further Tests -->
                  <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-yellow-400 transition-all duration-500 cursor-pointer transform"
                      style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                    
                    <h2 class="text-lg font-bold text-yellow-600">Monitoring & Further Tests</h2>

                    <!-- Follow-up Tests Section -->
                    <h6 class="font-semibold mt-2 text-yellow-700">Follow-up Tests:</h6>
                    <div v-for="(test, index) in analysisData.allopathic_treatment.MonitoringandFurtherDiagnosticTests.FurtherDiagnosticTests"
                        :key="index"
                        class="bg-gray-100 p-3 mb-3 rounded-lg shadow-md border-l-4 border-yellow-500">
                      <p><strong class="text-yellow-700">Test:</strong> {{ test.MedicalTest }}</p>
                      <p><strong class="text-yellow-700">Next Follow-up:</strong> {{ test.NextFollowupUp }}</p>
                      <p><strong class="text-yellow-700">Referral:</strong> {{ test.Referral }}</p>
                    </div>

                    <!-- Recommended Hospitals Section -->
                    <h6 class="font-semibold mt-4 text-yellow-700">Recommended Hospitals:</h6>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-yellow-500">
                      <ul>
                        <li v-for="(hospital, index) in analysisData.allopathic_treatment.MonitoringandFurtherDiagnosticTests.TopHospitalsforTreatment" 
                            :key="index" class="mb-2">
                          <strong class="text-yellow-800">{{ hospital.Name }}</strong> 
                          <span class="text-gray-700">({{ hospital.Specialty }} - {{ hospital.Website }})</span>
                        </li>
                      </ul>
                    </div>
  
                  </div>                  
                </div>

                <!-- Placeholder if No Data -->
                <div v-else class="p-6 bg-white rounded-xl shadow-md text-center text-gray-600">
                  No allopathic data available. Please upload a report for validation.
                </div>
            </div>

            <!--  Ayurvedic Recommendation Tab -->
            <div v-else-if="activeTab === 'Ayurvedic Recommendation' && analysisData.ayurvedic_treatment">
              <div v-if="Object.keys(analysisData.ayurvedic_treatment).length > 0" class="grid grid-cols-3 gap-6 mt-4">

                <!-- Ayurvedic Diagnosis -->
                <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-orange-400 transition-all duration-500 cursor-pointer transform"
                    style="max-height: 400px; min-height: 400px; overflow-y: auto;">

                  <h2 class="text-lg font-bold text-orange-800">Ayurvedic Diagnosis</h2>

                  <!-- Patient Details -->
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-orange-500 mb-3">
                    <p><strong class="text-orange-700">Report Type:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.ReportType }}</p>
                    <p><strong class="text-orange-700">Patient Name:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.PatientDetails.Name }}</p>
                    <p><strong class="text-orange-700">Age:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.PatientDetails.Age }}</p>
                    <p><strong class="text-orange-700">Sex:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.PatientDetails.Sex }}</p>
                  </div>

                  <!-- Prakriti Analysis -->
                  <h6 class="font-semibold mt-2 text-orange-700">Prakriti Analysis:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-orange-500 mb-3">
                    <ul>
                      <p><strong class="text-orange-700">Primary Dosha:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.PrakritiAnalysis.PrimaryDosha }}</p>
                      <p><strong class="text-orange-700">Secondary Dosha:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.PrakritiAnalysis.SecondaryDosha }}</p>
                      <p><strong class="text-orange-700">Body Type:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.PrakritiAnalysis.BodyType }}</p>
                      <p><strong class="text-orange-700">Mental Traits:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.PrakritiAnalysis.MentalTraits }}</p>                  
                    </ul>
                  </div>

                  <!-- Vikriti Analysis -->
                  <h6 class="font-semibold mt-2 text-orange-700">Vikriti Analysis:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-orange-500 mb-3">
                    <ul>
                      <p><strong class="text-orange-700">Imbalanced Dosha:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.VikritiAnalysis.ImbalancedDosha }}</p>
                    
                      <li v-for="(symptoms, index) in analysisData.ayurvedic_treatment.AyurvedicDiagnosis.VikritiAnalysis.Symptoms" 
                          :key="index"
                          class="bg-gray-100 p-3 mb-2 rounded-lg shadow-md border-l-4 border-orange-500">
                        <strong class="text-orange-700">Symptoms:</strong> {{ symptoms }}
                      </li>
                    </ul>
                  </div>

                  <!-- Agni Ama Assessment -->
                  <h6 class="font-semibold mt-2 text-orange-700">Agni Ama Assessment:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-orange-500 mb-3">
                    <ul>
                      <p><strong class="text-orange-700">Agni Type:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.AgniAmaAssessment.AgniType }}</p>
                      <p><strong class="text-orange-700">Ama Presence:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.AgniAmaAssessment.AmaPresence }}</p>
                      <p><strong class="text-orange-700">Signs Of Ama:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.AgniAmaAssessment.SignsOfAma }}</p>
                    </ul>
                  </div>

                   <!-- Dhatu Srotas Assessment -->
                  <h6 class="font-semibold mt-2 text-orange-700">Dhatu Srotas Assessment:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-orange-500 mb-3">
                    <ul>
                      <li v-for="(AffectedDhatus, index) in analysisData.ayurvedic_treatment.AyurvedicDiagnosis.DhatuSrotasAssessment.AffectedDhatus" 
                          :key="index"
                          class="bg-gray-100 p-3 mb-2 rounded-lg shadow-md border-l-4 border-orange-500">
                        <strong class="text-orange-700">Affected Dhatus:</strong> {{ AffectedDhatus }}
                      </li>

                      <li v-for="(AffectedSrotas, index) in analysisData.ayurvedic_treatment.AyurvedicDiagnosis.DhatuSrotasAssessment.AffectedSrotas" 
                          :key="index"
                          class="bg-gray-100 p-3 mb-2 rounded-lg shadow-md border-l-4 border-orange-500">
                        <strong class="text-orange-700">Affected Srotas:</strong> {{ AffectedSrotas }}
                      </li>
                    </ul>
                  </div>


                  <!-- Mental State Ojas Assessment -->
                  <h6 class="font-semibold mt-2 text-orange-700">Mental State Ojas:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-orange-500 mb-3">
                    <ul>
                      <p><strong class="text-orange-700">Mental State:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.MentalStateOjas.MentalState }}</p>
                      <p><strong class="text-orange-700">Ojas Level:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicDiagnosis.MentalStateOjas.OjasLevel }}</p>
                    </ul>
                  </div>
                </div>


                <!-- Ayurvedic Treatment Plan -->
                <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-green-400 transition-all duration-500 cursor-pointer transform"
                    style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                  <h2 class="text-lg font-bold text-green-600">Medication Recommandation</h2>

                  <!-- Lifestyle Modifications -->
                  <h6 class="font-semibold mt-2 text-green-700">Lifestyle Modifications:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                        <p><strong class="text-green-700">Dinacharya:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicTreatmentPlan.LifestyleModifications.Dinacharya }}</p>
                        <p><strong class="text-green-700">Exercise:</strong> {{ analysisData.ayurvedic_treatment.AyurvedicTreatmentPlan.LifestyleModifications.ExerciseRecommendations }}</p>
                        <p><strong class="text-green-700">Yoga & Pranayama:</strong></p>
                        <ul>
                          <li v-for="(yoga, index) in analysisData.ayurvedic_treatment.AyurvedicTreatmentPlan.LifestyleModifications.YogaAndPranayama" :key="index">
                            <strong class="text-green-700">{{ yoga.PracticeName }}</strong> - {{ yoga.Duration }}
                          </li>
                        </ul>
                  </div>

                  <!-- Shodhana Therapies -->
                    <h6 class="font-semibold mt-2 text-green-700">Shodhana Therapies:</h6>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                        <ul>
                          <li v-for="(therapy, index) in analysisData.ayurvedic_treatment.AyurvedicTreatmentPlan.ShodhanaTherapies" :key="index">
                            <strong class="text-green-700">{{ therapy.Therapy }}</strong> - {{ therapy.Purpose }}
                          </li>
                        </ul>
                    </div>

                        <!-- Shamana Therapies -->
                        <h6 class="font-semibold mt-2 text-green-700">Shamana Therapies:</h6>
                        <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                          <ul>
                            <li v-for="(therapy, index) in analysisData.ayurvedic_treatment.AyurvedicTreatmentPlan.ShamanaTherapies" :key="index">
                              <strong class="text-green-700">Herbal Remedy:</strong> {{ therapy.HerbalRemedy }} <br>
                              <strong class="text-green-700">Dosage:</strong> {{ therapy.Dosage }} <br>
                              <strong class="text-green-700">Usage:</strong> {{ therapy.Usage }} <br>
                              <strong class="text-green-700">Rationale:</strong> {{ therapy.Rationale }}
                            </li>
                          </ul>
                        </div>

                        <!-- Detoxification & Therapies -->
                        <h6 class="font-semibold mt-2">Detoxification & Therapies:</h6>
                        <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                          <ul>
                            <li v-for="(therapy, index) in analysisData.ayurvedic_treatment.AyurvedicTreatmentPlan.DetoxificationAndTherapies.RecommendedTherapies" :key="index">
                              {{ therapy }}
                            </li>
                          </ul>
                        </div>

                  <p class="text-gray-700" style="font-size:small;font-style: italic;font-variant: normal;">
                    <strong class="text-red-500">Medical Disclaimer:</strong>{{ analysisData.ayurvedic_treatment.Disclaimer }}
                  </p>
                </div>


                <!-- Monitoring & Further Tests -->
                <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-yellow-400 transition-all duration-500 cursor-pointer transform"
                    style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                  
                  <h2 class="text-lg font-bold text-yellow-600">Monitoring and Follow-ups</h2>

                  <!-- Follow-up Ayurvedic Recommendations -->
                  <h6 class="font-semibold mt-2 text-yellow-700">Follow-up Tests:</h6>
                  <div v-for="(test, index) in analysisData.ayurvedic_treatment.MonitoringandFurtherDiagnosticTests.FurtherDiagnosticTests"
                      :key="index"
                      class="bg-gray-100 p-3 mb-3 rounded-lg shadow-md border-l-4 border-yellow-500">
                    <p><strong class="text-yellow-700">Recommendation:</strong> {{ test.MonitoringParameters }}</p>
                    <p><strong class="text-yellow-700">Next Follow-up:</strong> {{ test.NextCheckup }}</p>
                    <p><strong class="text-yellow-700">Referral:</strong> {{ test.Referral }}</p>
                  </div>

                  <!-- Recommended Ayurvedic Centers -->
                  <h6 class="font-semibold mt-4 text-yellow-700">Recommended Ayurvedic Centers:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-yellow-500">
                    <ul>
                      <li v-for="(center, index) in analysisData.ayurvedic_treatment.MonitoringandFurtherDiagnosticTests.TopHospitalsforTreatment" 
                          :key="index" class="mb-2">
                        <strong class="text-yellow-800">{{ center.Name }}</strong> 
                        <span class="text-gray-700">({{ center.Specialty }} - {{ center.Specialty }})</span>
                      </li>
                    </ul>
                  </div>

                </div>                  
              </div>

              <!-- Placeholder if No Data -->
              <div v-else class="p-6 bg-white rounded-xl shadow-md text-center text-gray-600">
                No Ayurvedic data available. Please upload a report for validation.
              </div>
            </div>

            <!--  Modern Integrative Recommendation Tab -->
            <div v-else-if="activeTab === 'Modern Integrative Recommendation' && analysisData.modren_treatment">
              <div v-if="Object.keys(analysisData.modren_treatment).length > 0" class="grid grid-cols-3 gap-6 mt-4">

                <!-- Integrative Diagnostics Card -->
                <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-blue-400 transition-all duration-500 cursor-pointer transform"
                    style="max-height: 400px; min-height: 400px; overflow-y: auto;">

                    <h2 class="text-lg font-bold text-blue-800">Integrative Diagnostics</h2>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500 mb-3">
                    <p><strong class="text-blue-700">Report Type:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.ReportType }}</p>
                    <p><strong class="text-blue-700">Patient Name:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.PatientDetails.Name }}</p>
                    <p><strong class="text-blue-700">Age:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.PatientDetails.Age }}</p>
                    <p><strong class="text-blue-700">Sex:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.PatientDetails.Sex }}</p>
                    </div>

                    <!-- Allopathic Findings -->
                    <h6 class="font-semibold mt-2 text-blue-700">Allopathic Findings:</h6>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500 mb-3">
                    <ul>
                      <li v-for="(condition, index) in analysisData.modren_treatment.IntegrativeDiagnostics.AllopathicFindings.ConfirmedCondition" :key="index">
                        <strong class="text-blue-700">Condition:</strong> {{ condition.Condition }} <br>
                        <strong class="text-blue-700">Diagnostic Evidence:</strong> {{ condition.SupportingEvidence.DiagnosticEvidence }} <br>
                        <strong class="text-blue-700">Clinical Evidence:</strong> {{ condition.SupportingEvidence.ClinicalEvidence }} <br>
                      </li>
                    </ul>
                    </div>

                    <!-- Functional Medicine Insights -->
                    <h6 class="font-semibold mt-2 text-blue-700">Functional Medicine Insights:</h6>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500 mb-3">
                      <p><strong class="text-blue-700">Metabolic Imbalances:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.FunctionalMedicineInsights.MetabolicImbalances }}</p>
                      <p><strong class="text-blue-700">Hormonal Imbalances:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.FunctionalMedicineInsights.HormonalImbalances }}</p>
                      <p><strong class="text-blue-700">Oxidative Stress Markers:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.FunctionalMedicineInsights.OxidativeStressMarkers }}</p>
                      <p><strong class="text-blue-700">Nutritional Deficiencies:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.FunctionalMedicineInsights.NutritionalDeficiencies }}</p>
                      <p><strong class="text-blue-700">Inflammation Markers:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.FunctionalMedicineInsights.InflammationMarkers }}</p>
                      <p><strong class="text-blue-700">Gut Health Assessment:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.FunctionalMedicineInsights.GutHealthAssessment }}</p>
                    </div>

                    <!-- Ayurvedic Interpretation -->
                    <h6 class="font-semibold mt-2 text-blue-700">Ayurvedic Interpretation:</h6>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500 mb-3">
                      <p><strong class="text-blue-700">Dosha Imbalance:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.DoshaImbalance }}</p>
                      <p><strong class="text-blue-700">Agni Status:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.AgniStatus }}</p>
                      <p><strong class="text-blue-700">Ama Presence:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.AmaPresence }}</p>
                      <p><strong class="text-blue-700">Affected Srotas:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.AffectedSrotas }}</p>
                      <p><strong class="text-blue-700">Ojas Status:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.OjasStatus }}</p>
                      <p><strong class="text-blue-700">Mental State:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.AmaPresence }}</p>
                      <p><strong class="text-blue-700">Manas Prakriti:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.ManasPrakriti }}</p>
                      <p><strong class="text-blue-700">Prana Vayu Balance:</strong> {{ analysisData.modren_treatment.IntegrativeDiagnostics.AyurvedicInterpretation.PranaVayuBalance }}</p>                
                    </div>
                </div>

                <!-- Integrative Treatment Recommendations Card -->
                <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-green-400 transition-all duration-500 cursor-pointer transform mt-4"
                  style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                  <h2 class="text-lg font-bold text-green-600">Medication Recommendation</h2>

                  <!-- Lifestyle Modifications -->
                  <h6 class="font-semibold mt-2 text-green-700">Lifestyle Modifications:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                    <p><strong class="text-green-700">Hydration:</strong> {{ analysisData.modren_treatment.IntegrativeTreatmentRecommendations.LifestyleModifications.Hydration }}</p>
                    <p><strong class="text-green-700">Exercise:</strong> {{ analysisData.modren_treatment.IntegrativeTreatmentRecommendations.LifestyleModifications.Exercise }}</p>
                    <p><strong class="text-green-700">Sleep Hygiene:</strong> {{ analysisData.modren_treatment.IntegrativeTreatmentRecommendations.LifestyleModifications.SleepHygiene }}</p>
                  </div>

                  <!-- Herbal & Supplement Support -->
                  <h6 class="font-semibold mt-2 text-green-700">Herbal & Supplement Support:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                  <ul>
                    <li v-for="(herb, index) in analysisData.modren_treatment.IntegrativeTreatmentRecommendations.HerbalAndSupplementSupport" :key="index">
                      <strong class="text-green-700">Name:</strong> {{ herb.Name }} <br>
                      <strong class="text-green-700">Dosage:</strong> {{ herb.Dosage }} <br>
                      <strong class="text-green-700">Purpose:</strong> {{ herb.Purpose }}
                    </li>
                  </ul>
                  </div>

                  <!-- Detox & Therapies -->
                  <h6 class="font-semibold mt-2 text-green-700">Detox & Therapies:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                    <p><strong class="text-green-700">Detoxification:</strong> {{ analysisData.modren_treatment.IntegrativeTreatmentRecommendations.DetoxAndTherapies.Detoxification }}</p>
                    <p><strong class="text-green-700">Therapies:</strong> {{ analysisData.modren_treatment.IntegrativeTreatmentRecommendations.DetoxAndTherapies.Therapies }}</p>
                  </div>
                  <p class="text-gray-700" style="font-size:small;font-style: italic;font-variant: normal;">
                    <strong class="text-red-500">Medical Disclaimer:</strong>{{  analysisData.modren_treatment.Disclaimer }}
                  </p>
                </div>

                <!-- Monitoring & Follow-Up Card -->
                <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-yellow-400 transition-all duration-500 cursor-pointer transform mt-4"
                  style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                  <h2 class="text-lg font-bold text-yellow-600">Monitoring and Follow-ups</h2>

                  <h6 class="font-semibold mt-2 text-yellow-700">Follow-up Tests:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-yellow-500 mb-3">
                  <ul>
                    <li v-for="(test, index) in analysisData.modren_treatment.MonitoringAndFollowUp.FurtherDiagnosticTests" :key="index">
                      <strong class="text-yellow-700">Next Checkup:</strong> {{ test.NextCheckup }} <br>
                      <strong class="text-yellow-700">Tests To Monitor:</strong> 
                      <ul>
                        <li v-for="(t, idx) in test.TestsToMonitor" :key="idx">{{ t }}</li>
                      </ul>
                      <strong class="text-yellow-700">Referral:</strong> {{ test.Referral }}
                    </li>
                  </ul>
                  </div>

                  <h6 class="font-semibold mt-2 text-yellow-700">Recommended Hospitals:</h6>
                  <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-yellow-500 mb-3">
                  <ul>
                    <li v-for="(hospital, index) in analysisData.modren_treatment.MonitoringAndFollowUp.TopHospitalsforTreatment" :key="index">
                      <strong class="text-yellow-700">{{ hospital.Name }}</strong> ({{ hospital.Specialty }})
                    </li>
                  </ul>
                  </div>
                </div>
              </div>
            </div>


            <!--  Diet Recommendation Tab -->
            <div v-else-if="activeTab === 'Advance Diet Plan' && analysisData.advanced_diet_plan">
              <div v-if="Object.keys(analysisData.advanced_diet_plan).length > 0" class="grid grid-cols-3 gap-6 mt-4">

                <!-- Allopathic Diet Plan -->
                <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-blue-400 transition-all duration-500 cursor-pointer transform"
                style="max-height: 400px; min-height: 400px; overflow-y: auto;">

                      <h2 class="text-lg font-bold text-blue-800">Allopathic Diet Plan</h2>
                      <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500 mb-3">
                      <p><strong class="text-blue-700">Focus:</strong> {{ analysisData.advanced_diet_plan.AllopathicDietPlan.Focus }}</p>
                      <p><strong class="text-blue-700">Guidelines:</strong> {{ analysisData.advanced_diet_plan.AllopathicDietPlan.guidelines }}</p>
                      <p><strong class="text-blue-700">Cooking Style:</strong> {{ analysisData.advanced_diet_plan.AllopathicDietPlan.cooking_style }}</p>
                      <p><strong class="text-blue-700">Key Principles:</strong> {{ analysisData.advanced_diet_plan.AllopathicDietPlan.KeyPrinciples }}</p>
                      <p><strong class="text-blue-700">Foods to Avoid:</strong> {{ analysisData.advanced_diet_plan.AllopathicDietPlan.foodstoavoid }}</p>
                    </div>

                      <h3 class="text-lg font-bold text-blue-800">Meal Plan:</h3>
                      <div v-for="(meal, type) in analysisData.advanced_diet_plan.AllopathicDietPlan.Meals" :key="type"
                        class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-blue-500 mb-3">
                        <h4 class="text-blue-700 mt-2">{{ type }}</h4>
                        <ul>
                          <li v-for="(item, index) in meal" :key="index" class="border p-2 rounded-lg mt-1">
                            <strong class="text-blue-700">Dish:</strong> {{ item.Dish }} <br>
                            <strong class="text-blue-700">Mealtime:</strong> {{ item.mealtime }} <br>
                            <strong class="text-blue-700">Ingredients:</strong> {{ item.Ingredients }} <br>
                            <strong class="text-blue-700">Nutritional Value:</strong> {{ item.NutritionalValue }} <br>
                            <strong class="text-blue-700">Ingredients to Avoid:</strong> {{ item.ingredientstoavoid }}
                          </li>
                        </ul>
                      </div>
                  </div>


                  <!-- Ayurvedic Diet Plan -->
                  <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-green-400 transition-all duration-500 cursor-pointer transform"
                    style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                    <h2 class="text-lg font-bold text-green-600">Ayurvedic Diet Plan</h2>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                    <p><strong class="text-green-700">Focus:</strong> {{ analysisData.advanced_diet_plan.AyurvedicDietPlan.Focus }}</p>
                    <p><strong class="text-green-700">Cooking Style:</strong> {{ analysisData.advanced_diet_plan.AyurvedicDietPlan.cooking_style }}</p>
                    <p><strong class="text-green-700">Key Principles:</strong> {{ analysisData.advanced_diet_plan.AyurvedicDietPlan.KeyPrinciples }}</p>
                    <p><strong class="text-green-700">Foods to Avoid:</strong> {{ analysisData.advanced_diet_plan.AyurvedicDietPlan.foodsstoavoid }}</p>
                  </div>

                    <h3 class="mt-2 font-semibold">Meal Plan:</h3>
                    <div v-for="(meal, type) in analysisData.advanced_diet_plan.AyurvedicDietPlan.Meals" :key="type"
                      class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-green-500 mb-3">
                      <h4 class="text-green-700 mt-2">{{ type }}</h4>
                      <ul>
                        <li v-for="(item, index) in meal" :key="index" class="border p-2 rounded-lg mt-1">
                          <strong class="text-green-700">Dish:</strong> {{ item.Dish }} <br>
                          <strong class="text-green-700">Mealtime:</strong> {{ item.mealtime }} <br>
                          <strong class="text-green-700">Dosha Effect:</strong> {{ item.DoshaEffect }} <br>
                          <strong class="text-green-700">Ingredients:</strong> {{ item.Ingredients }} <br>
                          <strong class="text-green-700">Ingredients to Avoid:</strong> {{ item.ingredientstoavoid }}
                        </li>
                      </ul>
                    </div>
                  </div>

                  <!-- Modern Integrative Diet Plan -->
                  <div class="p-4 bg-white rounded-2xl shadow-lg border-t-4 border-yellow-400 transition-all duration-500 cursor-pointer transform"
                style="max-height: 400px; min-height: 400px; overflow-y: auto;">
                    <h2 class="text-lg font-bold text-yellow-600">Modern Integrative Diet Plan</h2>
                    <div class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-yellow-500 mb-3">
                    <p><strong class="text-yellow-700">Focus:</strong> {{ analysisData.advanced_diet_plan.ModernIntegrativeDietPlan.Focus }}</p>
                    <p><strong class="text-yellow-700">Cooking Style:</strong> {{ analysisData.advanced_diet_plan.ModernIntegrativeDietPlan.cooking_style }}</p>
                    <p><strong class="text-yellow-700">Foods to Avoid:</strong> {{ analysisData.advanced_diet_plan.ModernIntegrativeDietPlan.foodstoavoid }}</p>
                    <p><strong class="text-yellow-700">Key Principles:</strong> {{ analysisData.advanced_diet_plan.ModernIntegrativeDietPlan.KeyPrinciples }}</p>                   
                    </div>

                    <h3 class="mt-2 font-semibold">Meal Plan:</h3>
                    <div v-for="(meal, type) in analysisData.advanced_diet_plan.ModernIntegrativeDietPlan.Meals" :key="type"
                      class="bg-gray-100 p-3 rounded-lg shadow-md border-l-4 border-yellow-500 mb-3">
                      <h4 class="text-yellow-700 mt-2">{{ type }}</h4>
                      <ul>
                        <li v-for="(item, index) in meal" :key="index" class="border p-2 rounded-lg mt-1">
                          <strong class="text-yellow-700">Dish:</strong> {{ item.Dish }} <br>
                          <strong class="text-yellow-700">Mealtime:</strong> {{ item.mealtime }} <br>
                          <strong class="text-yellow-700">Ingredients:</strong> {{ item.Ingredients }} <br>
                          <strong class="text-yellow-700">Benefits:</strong> {{ item.Benefits }} <br>
                          <strong class="text-yellow-700">Ingredients to Avoid:</strong> {{ item.ingredientstoavoid }}
                        </li>
                      </ul>
                    </div>
                    <p class="text-gray-700" style="font-size:small;font-style: italic;font-variant: normal;">
                    <strong class="text-red-500">Medical Disclaimer:</strong>{{ analysisData.advanced_diet_plan.Disclaimer }}
                    </p>
                  </div>
                </div>
            </div>   

            <div v-else class="grid grid-cols-3 gap-6 mt-4">
            <div 
            v-for="card in cards[activeTab]"
            :key="card.title"
            class="p-4 bg-white rounded-2xl shadow-lg border-t-4 transition-all duration-500 cursor-pointer transform hover:scale-105 hover:shadow-xl"
            >
                <h2 class="text-lg font-bold">{{ card.title }}</h2>
                <p class="text-sm text-gray-600">{{ card.description }}</p>
            </div>
            </div>
          </transition>
        </div>

      </div>
       <!-- Full-Screen Black Overlay -->
      <div v-if="isLoading" class="overlay">
        <img src="@/assets/ai_spinner.gif" alt="Loading..." class="spinner" />
      </div>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  export default {
    name: "App",
    data() {
      return {
        tabs: ["Ask AI","Summary", "ಸಾರಾಂಶ","सारांश", "Allopathic Recommendation", "Ayurvedic Recommendation", "Modern Integrative Recommendation","Advance Diet Plan"],
        activeTab: "Ask AI",
        imageFile: null,
        imageUrl: null,        
        analysisData: {}, // Initialize to prevent errors
        showImagePopup: false,
        displayMessage: "Kindly Upload image for analysis",
        showConsentPopup: false,
        uploadAuthorized: false,
        showAuthorization: false,
        textContent: '',
        isLoading: false, // Controls overlay visibility
        cards: {
          "Summary": [],
          "ಸಾರಾಂಶ": [],
          "सारांश" :[],
          "Allopathic Recommendation": [],
          "Ayurvedic Recommendation": [],
          "Modern Integrative Recommendation": [],
          "Advance Diet Plan": [],
        }
      };
    },
    methods: {
    toggleCard(selectedCard) {
      // Find the current tab's cards
      const currentCards = this.cards[this.activeTab];
      
      // Collapse all cards first
      currentCards.forEach(card => {
        if (card !== selectedCard) {
          card.open = false;
        }
      });
  
      // If the card was already open, close it
      if (selectedCard.open) {
        selectedCard.open = false;
        return;
      }
      
      // Remove the selected card from its original position
      const index = currentCards.indexOf(selectedCard);
      if (index > -1) currentCards.splice(index, 1);
  
      // Mark the card as open
      selectedCard.open = true;
  
      // Add the opened card at the bottom of the array (displayed last)
      currentCards.push(selectedCard);
    },
    onFileChange(event) {
        
        const file = event.target.files[0];
        if (file) {
            this.imageFile = file;
            this.imageUrl = URL.createObjectURL(file);
            this.showImagePopup = false;  // Ensure popup is closed if new file is uploaded
            this.displayMessage = "Authorize to analyse by clicking analyze icon";
            }
        
    },
    async analyzeImage() {
        if (!this.imageUrl) {
            alert("Please upload an image for analyzing.");
            return;
        }
        this.isLoading = true; // Show overlay
        this.displayMessage = "Analysis started once completed you will be redirected to Summary tab. Kindly be patience";
        this.analysisResult = `Analysis started`
        const formData = new FormData();
        formData.append("file", this.imageFile);

        try {
        const response = await fetch("http://127.0.0.1:8000/analyze/", {
          method: "POST",
          body: formData
        });

        if (!response.ok) throw new Error(`Failed to fetch. Status: ${response.status}`);
        const data = await response.json();
        console.log("API Response:", data);  // Log API Response
     // Correctly fetching nested structure
    
     if (data.image_analysis_english && data.image_analysis_kannada) {
          this.analysisData = data; //  Correctly assign data

          this.analysisResult = "Analysis Complete: Results available in Summary Tab.";
          this.activeTab = "Summary"; //  Auto-switch to Summary Tab
          console.log("Parsed Data:", this.analysisData);
        } else {
          throw new Error("Invalid response format. Missing 'image_analysis_english' or 'image_analysis_kannada' fields.");
        }
        setTimeout(() => {
        this.isLoading = false; // Hide overlay after process
      }, 1000); // Change 5000ms to actual analysis duration
        this.analysisResult = `Analysis Complete: ${this.analysisData.image_analysis_english.PatientDetails}`;
       
      } catch (error) {
        console.error("Error analyzing image:", error);
        this.analysisResult = "Error analyzing the image.";
        setTimeout(() => {
        this.isLoading = false; // Hide overlay after process
      }, 1000); // Change 5000ms to actual analysis duration
      alert("Error analyzing the image.");
      }   
    
    },
    toggleZoom() {
        this.zoomed = !this.zoomed;
    },

    acceptConsent() {
            this.showConsentPopup = false;
            this.analyzeImage();

    },
    authorizeUpload() {
        this.displayMessage = "You are Authorized";
        this.uploadAuthorized = false;

        setTimeout(() => {
            this.uploadAuthorized = true;
            this.displayMessage = "Kindly Upload image for analysis";
            document.getElementById("file-upload").click();
        }, 1000);
    },
    showAuthorizationMessage() {
        event.preventDefault();  // Prevent default click action
        this.showAuthorization = true;
        setTimeout(() => {
            this.showAuthorization = false;
            document.getElementById('file-upload').click(); // Trigger file upload after message
        }, 1000); // Display for 1 seconds
    },
    triggerFileUpload() {
            // Trigger file input after "You are Authorized" is shown
            document.getElementById('file-upload').click();
        },
  },
  
  
  };
  </script>
  
  <style scoped>
  body {
    margin: 0;
    font-family: 'Charsey', cursive;
  }
  .fade-enter-active, .fade-leave-active { transition: opacity 0.5s ease; }
  .fade-enter-from, .fade-leave-to { opacity: 0; }
  
  /* Footer Animation */
  @keyframes glow {
    0%, 100% { text-shadow: 0 0 5px #61A0FF, 0 0 10px #61A0FF; }
    50% { text-shadow: 0 0 10px #61A0FF, 0 0 20px #61A0FF; }
  }
  .animate-glow {
    animation: glow 1.5s infinite;
  }
  .flex > div:not(:last-child)::after {
    content: "";
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    height: 60%;
    width: 1px;
    background-color: #E0E0E0;
  }
  img {
  transition: transform 0.3s;
}

img.scale-150 {
  transform: scale(1.5);
}

button:disabled img {
  opacity: 0.5;
  cursor: not-allowed;
}

@keyframes bounce-glow {
    0%, 100% {
        transform: scale(1);
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.8), 0 0 20px rgba(255, 0, 255, 0.5), 0 0 30px rgba(0, 0, 255, 0.5);
    }
    50% {
        transform: scale(1.1);
        box-shadow: 0 0 15px rgba(255, 255, 255, 1), 0 0 30px rgba(255, 0, 255, 0.7), 0 0 40px rgba(0, 0, 255, 0.7);
    }
}

.animate-bounce-glow {
    animation: bounce-glow 1.5s ease-in-out infinite;
}

.card {
    transition: all 0.3s ease-in-out;
}
.card * {  
    text-shadow: none !important;  
    filter: none !important;  
    backdrop-filter: none !important;  
}
.card:hover {
    filter: none !important; 
    opacity: 1 !important;  
    transform: scale(1.05); /* Slight zoom effect for a better hover effect */
}

    /* Overlay Styling */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.9); /* Dark overlay */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 50;
}

/* Spinner Image */
.spinner {
  width: 150px; /* Adjust based on your image size */
  height: 150px;
}


/* Brand Logo Styling */
.brand-logo {
  height: 50px;
  width: auto;
}

/* Stylish Gradient Text */
.stylish-text {
  font-weight: bold;
}
  </style>
  