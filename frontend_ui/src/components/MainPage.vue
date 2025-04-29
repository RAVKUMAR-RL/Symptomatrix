<template>
    <div class="min-h-screen bg-gradient-to-r from-blue-50 to-green-100 relative overflow-hidden">
      <!-- Background Design -->
      <div class="absolute top-0 right-0 w-[500px] h-[500px] -mt-40 -mr-40 bg-teal-300 rounded-full opacity-30 animate-pulse"></div>
      <div class="absolute top-0 right-0 w-[300px] h-[300px] -mt-20 -mr-10 bg-teal-200 rounded-full opacity-50 animate-pulse"></div>
  
      <div class="max-w-[1450px] mx-auto p-6 bg-gradient-to-r from-white via-blue-50 to-green-50 rounded-2xl shadow-2xl shadow-blue-200 mt-10 relative z-10 animate-expand border border-teal-300"
        style="max-height: 93vh; min-height:93vh;margin-top: 25px;">
        
        <!-- Main Container (Top) -->
        <div>
          <!-- Header Section (Centered) -->
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
  
          
          <div class="flex items-center justify-center mb-4 p-2 rounded-t-lg shadow-inner bg-gradient-to-r from-blue-100 to-green-100 relative overflow-hidden space-x-6" style="height: 525px;">
           
            <!-- Vertical Tabs Menu -->
      <div class="flex flex-col space-y-4">
        <div v-for="tab in tabs" 
             :key="tab" 
             :class="['tab-label', { 'active-tab': currentTab === tab }]" 
             @click="currentTab = tab">
          <div class="tab-text">{{ tab }}</div>
        </div>
      </div>

      <!-- Expanded Content Area -->
      <div class="relative flex-1 transition-all duration-500 ml-4" style="height: 500px;" >
        <!-- About Us Tab -->
        <transition name="slide-fade">
        <div v-if="currentTab === 'About Us'" class="tab-content flex items-center space-x-6 p-6">
            <!-- Image Section -->
            <div class="flex-shrink-0">
            <img 
                :src="require('@/assets/aboutus.png')" 
                alt="About Us Image" 
                class="w-64 h-64 rounded-lg shadow-md object-cover"
            />
            </div>
            <!-- Text Section -->
            <div>
            <h2 class="text-3xl font-bold mb-4 text-blue-800">About Us</h2>
            <p class="text-gray-700 max-w-l leading-relaxed">
                "At <strong>Symptomatrix</strong>, we are pioneering a new era in healthcare decision-making through innovative technology and unparalleled precision.
                Our advanced platform harnesses the power of artificial intelligence and machine learning to analyze complex medical reports, transforming intricate 
                data into clear, actionable insights that empower both patients and healthcare professionals. Whether you're seeking clarity on health diagnoses or striving 
                to optimize treatment plans, our application provides accurate, reliable, and timely solutions tailored to individual needs.
            </p>
            <p class="text-gray-700 mt-2 max-w-l leading-relaxed">
                Driven by a commitment to excellence, accessibility, and patient-centricity, we bridge the gap between raw medical data and informed decision-making, 
                fostering trust and understanding in the healthcare journey. By simplifying critical medical information and enhancing communication between patients 
                and providers, we aim to improve health outcomes and elevate the standard of care globally. At <strong>Symptomatrix</strong>, we believe in shaping the future of 
                healthcare—one report at a time—with innovation, compassion, and a dedication to advancing lives.
            </p>
            <p class="text-gray-700 mt-2 max-w-l leading-relaxed">
                Our AI-powered medical diagnostic assistant is specialize in analyzing health data such as X-rays, blood reports, and more,providing accurate diagnostics with allopathic and ayurvedic recommendations.
                Our cutting-edge technology combines modern medicine with holistic approaches to offer the best possible care, ensuring a healthier future for everyone."
            </p>
            </div>
        </div>
        </transition>


        <transition name="slide-fade">
          <div v-if="currentTab === 'Testimony'" class="tab-content">
            <h2 class="text-3xl font-bold mb-2 text-green-800">Testimony</h2>
            <p class="text-gray-700">
              “Symptomatrix transformed my healthcare journey with precise analysis and guidance. Truly a game-changer!” - Sarah K.
            </p>
          </div>
        </transition>

        <transition name="slide-fade">
          

          <div v-if="currentTab === 'What Drives Us'" class="tab-content flex items-center space-x-6 p-6">
            <!-- Image Section -->
            <div class="flex-shrink-0">
            <img 
                :src="require('@/assets/whatdrivesus.png')" 
                alt="About Us Image" 
                class="w-64 h-64 rounded-lg shadow-md object-cover"
            />
            </div>
            <!-- Text Section -->
            <div>
            <h2 class="text-3xl font-bold mb-4 text-blue-800">What Drives Us</h2>
            <p class="text-gray-700 max-w-l leading-relaxed">
                "At <strong>Symptomatrix</strong>, the heart of our journey lies an unwavering commitment to making a difference. 
                We are driven by the belief that healthcare should be accessible, accurate, and empowering for all. 
                Each step we take is fueled by the desire to bridge gaps, simplify complexities, and transform how people interact with medical information.           
            
            </p>
            <p class="text-gray-700 mt-2 max-w-l leading-relaxed">
                Innovation is our compass, and excellence is our destination.
                By leveraging cutting-edge technology and harnessing the power of collaboration, we aim to empower individuals, healthcare professionals, and communities to make informed decisions that lead to better outcomes.
            </p>
            <p class="text-gray-700 mt-2 max-w-l leading-relaxed">
                <strong>What drives us</strong> is more than a mission—it’s a passion for change. It’s the understanding that every report analyzed, every insight shared, and every life improved brings us closer to a healthier, more informed world. Together, we are shaping the future of care, one transformative step at a time.
            
            </p>
            </div>
        </div>
        </transition>
        
        <!-- Ask AI Icon animation -->
        <transition name="fade">
      <div 
        v-if="isLoggedIn" 
        class="ai-icon-container"
        @click="goToAnalyzePage"
      >
        <img :src="require('@/assets/ai.png')" alt="AI Icon" class="ai-icon continuous-bounce" />
      </div>
    </transition>
        
        <transition name="slide-fade">
  <div v-if="currentTab === 'Contact Us'" class="tab-content bg-white shadow-lg rounded-lg p-6 mt-4 space-y-6 max-w-5xl mx-auto">

    <!-- Heading -->
    <h2 class="text-3xl font-bold mb-4 text-red-800 animate__animated animate__fadeInDown" style="margin-bottom: 5px;">Contact Us</h2>
    
    <!-- Overview Section -->
    <div class="space-y-2 mb-4 animate__animated animate__fadeIn" style="margin-top: 0px;">
      <p class="text-gray-700 text-base">
        Our dedicated team of professionals is available to assist you during our working hours. 
        Your inquiries are important to us, and we strive to respond promptly and effectively.
      </p>
    </div>

    <!-- Contact Information Section -->
    <div class="flex flex-col md:flex-row justify-between space-y-4 md:space-y-0 md:space-x-4">

      <!-- Contact Details -->
      <div class="w-full md:w-1/2 space-y-4 text-gray-800 text-sm animate__animated animate__fadeInLeft">
        
        <!-- Email -->
        <div class="flex items-center space-x-2">
          <i class="fas fa-envelope text-red-600"></i>
          <h3 class="font-bold text-lg">Email:</h3>
          <p>marketing@relevancelab.com</p>
        </div>

        <!-- Address -->
        <div class="flex items-center space-x-2">
          <i class="fas fa-map-marker-alt text-red-600"></i>
          <h3 class="font-bold text-lg">Address:</h3>
          <p>Smartworks - Vaishnavi Tech Park, South Tower, 10th Floor, Sy. No.16/1 and 17/2, Bellandur Gate, Sarjapur Main Road, Ambalipura, Bengaluru, Karnataka – 560103</p>
        </div>

        <!-- Working Hours -->
        <div class="flex items-center space-x-2">
          <i class="fas fa-clock text-red-600"></i>
          <h3 class="font-bold text-lg">Working Hours:</h3>
          <p>Mon - Sat: 9:00 AM - 6:00 PM | Sun: Closed</p>
        </div>
        
        <!-- Social Media Icons -->
        <div class="mt-8">
          <h3 class="font-bold text-xl mb-2 text-red-800">Connect With Us:</h3>
          <div class="flex space-x-6">
            <a href="https://www.facebook.com/RelevanceLabFacebook" target="_blank" class="social-icon text-blue-600 hover:text-blue-800 transition duration-300 transform hover:scale-125">
              <i class="fab fa-facebook fa-2x"></i>
            </a>
            <a href="https://twitter.com/Relevancelab" target="_blank" class="social-icon text-blue-400 hover:text-blue-600 transition duration-300 transform hover:scale-125">
              <i class="fab fa-twitter fa-2x"></i>
            </a>
            <a href="https://www.linkedin.com/in/relevance-lab/" target="_blank" class="social-icon text-blue-700 hover:text-blue-900 transition duration-300 transform hover:scale-125">
              <i class="fab fa-linkedin fa-2x"></i>
            </a>
            <a href="https://www.instagram.com/relevancelab/" target="_blank" class="social-icon text-pink-600 hover:text-pink-800 transition duration-300 transform hover:scale-125">
              <i class="fab fa-instagram fa-2x"></i>
            </a>
            <a href="https://www.youtube.com/channel/UCAtwgWJOSVCBUPjbL8QcOgw?view_as=subscriber" target="_blank" class="social-icon text-pink-600 hover:text-pink-800 transition duration-300 transform hover:scale-125">
              <i class="fab fa-youtube fa-2x"></i>
            </a>
          </div>
        </div>
       
      </div>

      <!-- Google Map Embed -->
      <div class="w-full md:w-1/2 animate__animated animate__fadeInRight">
        <iframe
          class="w-full h-64 rounded-lg shadow-md"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.814482094586!2d77.66898757489211!3d12.91964218739099!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae144501d2e229%3A0xad9928e02a4a17dc!2sRelevance%20Lab%20Pvt.%20Ltd.!5e0!3m2!1sen!2sin!4v1743587128798!5m2!1sen!2sin"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade">
        </iframe>
      </div>
    </div>
  </div>
</transition>






      </div>
            
          </div>
        </div>
  
        <!-- Login Icon & Welcome Message -->
        <div class="fixed top-4 right-4 text-right flex flex-col items-end">
          <img 
            :src="isLoggedIn ? require('@/assets/logged.png') : require('@/assets/login.png')" 
            alt="Login Icon" 
            class="w-12 h-12 cursor-pointer transition-transform transform hover:scale-110" 
            @click="toggleLoginPopup"
          />
          <transition name="fade">
            <div v-if="isLoggedIn" class="mt-3 text-L text-blue-700 font-bold animate-slideIn p-2" style="margin-right: 55px; margin-top: 25px; color: #7D3C98;">
              Welcome, {{ usernameDisplay }}
            </div>
          </transition>
        </div>
  
        <!-- Login Popup -->
        <div v-if="showLoginPopup" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-20">
          <div class="bg-white p-6 rounded-xl shadow-lg w-96 animate-fadeIn scale-up-center">
            <h2 class="text-2xl font-bold mb-4 text-center text-blue-700">Login</h2>
            <div class="mb-4">
              <label class="block mb-1">Username</label>
              <input type="text" v-model="username" class="w-full p-2 border rounded"/>
            </div>
            <div class="mb-6">
              <label class="block mb-1">Password</label>
              <input type="password" v-model="password" class="w-full p-2 border rounded"/>
            </div>
            <div class="flex justify-end">
              <button class="analyze-button" @click="performLogin">Login</button>
            </div>
          </div>
        </div>
  
        <!-- Modern Success Message -->
        <transition name="fade">
          <div v-if="showSuccessMessage" class="fixed inset-0 flex items-center justify-center z-30">
            <div class="backdrop-blur-sm bg-gradient-to-br from-green-400 to-blue-500 text-white text-lg font-bold py-4 px-8 rounded-xl shadow-2xl transform animate-popUp">
              ✅ Successfully Logged In!
            </div>
          </div>
        </transition>
  
        <!-- Footer -->
        <footer class="absolute bottom-0 w-full text-center py-2 text-sm text-gray-500 animate-glow">       
          © 2025 Relevance Lab. All rights reserved. 
        </footer>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Main",
    data() {
        
      return {
        showLoginPopup: false,
        username: "",
        password: "",
        isLoggedIn: false,
        showSuccessMessage: false,
        usernameDisplay: "",
        tabs: ['About Us', 'Testimony', 'What Drives Us', 'Contact Us'],
      currentTab: 'About Us',
      isLoggedIn: false,
      };
    },
    mounted() {
    // Set the login status based on your login logic
    this.isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
  },
    methods: {
      toggleLoginPopup() {
        this.showLoginPopup = true;
      },
      performLogin() {
        if (this.username && this.password) {
          this.isLoggedIn = true;
          this.showLoginPopup = false;
          this.usernameDisplay = this.username.toUpperCase().slice(0, 10);
          this.username = "";
          this.password = "";
          this.showSuccessMessage = true;
  
          setTimeout(() => {
            this.showSuccessMessage = false;
          }, 2500);
        } else {
          alert("Please enter your username and password.");
        }
      },
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
          console.log("File uploaded:", file.name);
        }
      },
      goToAnalyzePage() {
        this.$router.push('/analysis');
    }
    }
  };
  </script>
  
  <style scoped>
  .analyze-button, .upload-button {
    background-color: #10B981;
    padding: 12px 24px;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
    color: white;
    font-size: 1rem;
    border: none;
  }
  .analyze-button:hover, .upload-button:hover {
    background-color: #059669;
  }
  .animate-popUp {
    animation: popUp 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
  }
  @keyframes popUp {
    0% { transform: scale(0.8); opacity: 0; }
    50% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(1); }
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }


  .tab-label {
  display: flex;
  align-items: center;
  padding: 12px 0;
  margin-left: -10px;
  cursor: pointer;
  transition: all 0.3s;
  border-left: 4px solid transparent;
}

.tab-text {
  padding-left: 15px;
  font-size: 18px;
  font-weight: 600;
  color: #0D4F8B;
  transition: all 0.3s;
}

.tab-label:hover .tab-text {
  color: #10B981;
}

.tab-label:hover {
  transform: translateX(5px);
  border-left: 4px solid #10B981;
}

.active-tab .tab-text {
  color: #10B981;
  font-weight: bold;
}

.active-tab {
  border-left: 4px solid #10B981;
  background-color: #E0F7FA;
}

.tab-content {
  padding: 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  
}

.slide-fade-enter-active, .slide-fade-leave-active {
  transition: all 0.5s;
}
.slide-fade-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}
.slide-fade-leave-to {
  transform: translateX(100%);
  opacity: 0;
}

.ai-icon-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  z-index: 9999;
}

.ai-icon {
  width: 60px;
  height: 60px;
  transition: transform 0.3s;
}

.ai-icon:hover {
  transform: scale(1.1) rotate(10deg);
}

/* Animation Effect */
@keyframes bounce {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
}

.bounce {
  animation: bounce 1s;
}


/* Continuous Bounce Animation */
@keyframes continuousBounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-15px);
  }
}

.continuous-bounce {
  animation: continuousBounce 1.5s infinite;
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
  