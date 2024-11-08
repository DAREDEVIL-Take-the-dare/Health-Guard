import os
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Set the page configuration with custom title and layout
st.set_page_config(page_title="Health Guard - Disease Prediction System", layout="wide")

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open("diabetese.pkl", "rb"))
heart_model = pickle.load(open("heart.pkl", "rb"))
parkinsons_model = pickle.load(open("parkinsons.pkl", "rb"))


# Sidebar menu with custom icons
with st.sidebar:
    st.markdown(
    """
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .rounded-border-blur {
        border-radius: 50%;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5); /* Adds a blur effect */
        transition: transform 0.3s ease; /* Smooth transition */
        width: 200px;
    }
    .rounded-border-blur:hover {
        transform: scale(1.05); /* Slight zoom on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML code for image display with the specified class
    st.markdown(
    """
    <div class="centered-image">
        <img src="https://thumbs.dreamstime.com/b/illustration-health-care-logo-design-isolated-white-background-its-suitable-hospitals-privet-channel-centers-vector-211897081.jpg"
        class="rounded-border-blur">
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown("<h1 style='text-align: center; text-size:large;'>Health Guard</h1>", unsafe_allow_html=True)

    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=["activity", "heart", "person"],
        menu_icon="hospital-fill",
        default_index=0,
        styles={
        "container": {"padding": "0", "background-color": "#ffffff"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "5px",
            "padding": "10px",
            "background-color": "#e3f2fd",
        },
        "nav-link-selected": {"background-color": "#90caf9"},
    }
    )
# Styling for each section
if selected == 'Diabetes Prediction':
    st.markdown("""
    <style>
        /* Set background image for the entire app */
        .stApp {
            background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe_ugRYa3xG_vZv3r39nqeDKowEvQ12JVJ-A&s');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Make the background image responsive */
        @media (max-width: 1024px) {
            .stApp {
                background-size: contain;  /* Make sure the image fits when sidebar is open */
                background-repeat: no-repeat;
                background-position: center;
            }
        }

        /* For larger screens when sidebar is closed */
        @media (min-width: 1024px) {
            .stApp {
                background-size: cover;  /* Ensure the image fully covers the screen */
            }
        }

        /* Style the sidebar menu */
        .css-1d391kg {
            width: 300px;
        }

        /* Style the main content area */
        .css-1d391kg + .css-1v0mbdj {
            padding: 20px;
            width: 100%;
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)


    st.markdown("<h1 style='text-align: center; color: #fc7a28;'>Welcome to the Diabetes Prediction Model 🩺</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 2px solid #fc7a28;'>", unsafe_allow_html=True)

    st.markdown("""
    <style>
        /* Style for the slider label */
        .stSlider p {
            border-top: 5px;
            font-size: 24px;
            font-weight: 700;
            color: #fc6405;
            }
        .stButton{
            align: center;
            }
        .stButton p{
            color:#db5909;
            text-align:center;
            font-size:25px;}

    </style>
""", unsafe_allow_html=True) 

    # Input sliders
    c1, c2, c3 = st.columns(3)
    glucose = c1.slider('🩸 Glucose Level', 0, 500, 120)
    BP = c2.slider('💉 Blood Pressure Level', 0, 240, 120)
    skthick = c3.slider('📏 Skin Thickness', 0, 100, 20)
    insuline = c1.slider('💉 Insulin Level', 0, 900, 30)
    bmi = c2.slider('⚖️ BMI Value', 0.0, 70.0, 25.0)
    dpf = c3.slider('🧬 Diabetes Pedigree Function', 0.0, 2.5, 0.5)
    age = c1.slider(' Age', 0, 100, 30)
    
    if st.button('🔍 Generate Diabetes Result'):
        result = diabetes_model.predict([[glucose, BP, skthick, insuline, bmi, dpf, age]])[0]
        # Example of enlarging text size for the result
        if result == 1:
           st.markdown("<h2 style='color: red; text-align:center;'>⚠️ You are likely to have diabetes.</h2>", unsafe_allow_html=True)
        else:
           st.markdown("<h2 style='color: green;text-align:center;'>✅ You are not likely to have diabetes.</h2>", unsafe_allow_html=True)
    



elif selected == 'Heart Disease Prediction':
    st.markdown("""
    <style>
        /* Set background image for the entire app */
        .stApp {
            background-image: url('https://wallpaper.dog/large/20427828.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Make the background image responsive */
        @media (max-width: 1024px) {
            .stApp {
                background-size: contain;  /* Make sure the image fits when sidebar is open */
                background-repeat: no-repeat;
                background-position: center;
            }
        }

        /* For larger screens when sidebar is closed */
        @media (min-width: 1024px) {
            .stApp {
                background-size: cover;  /* Ensure the image fully covers the screen */
            }
        }

        /* Style the sidebar menu */
        .css-1d391kg {
            width: 300px;
        }

        /* Style the main content area */
        .css-1d391kg + .css-1v0mbdj {
            padding: 20px;
            width: 100%;
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #DC143C;'>Welcome to the Heart Disease Prediction Model ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 2px solid #DC143C;'>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        /* Style for the slider label */
        .stSlider p {
            border-top: 5px;
            font-size: 24px;
            font-weight: 700;
            color: #c21010;
            }
        div.st-emotion-cache-1puwf6r p{
            border-top: 5px;
            font-size: 24px;
            font-weight: 700;
            color: #c21010;
            }
        div.st-emotion-cache-p0pjm p{
            font-size: 12px;
            color: #c21009;
            }
        div.st-el ul li{
            font-size: 12px;
            color: #c21009;}
        .stButton{
            align: center;
            }
        .stButton button div.st-emotion-cache-12h5x7g p{
            color:#c21010;
            text-align:center;
            font-size:24px;}

    </style>
""", unsafe_allow_html=True)



    # Input sliders and options
    c1, c2, c3 = st.columns(3)
    age = c1.slider('🎂 Age', 0, 100, 30)
    gender = c2.radio('⚧ Gender', ['Male', 'Female'])
    cp = c3.selectbox('💓 Chest Pain Types', ['Type1', 'Type2', 'Type3', 'Type'])
    tresttbs = c1.slider('💊 Resting Blood Pressure', 0, 200, 120)
    chol = c2.slider('🩸 Serum Cholesterol', 50, 600, 200)
    fbs = c3.radio('🍬 Fasting Blood Sugar > 120 mg/dL', ['Yes', 'No'])
    restecg = c1.radio('🧠 Resting ECG', ["Normal", "Abnormal"])
    mhra = c2.slider("❤️ Maximum Heart Rate", 50, 200, 80)
    ang = c3.radio('🚴‍♂️ Exercise-Induced Angina', ["Yes", "No"])
    oldpeak = c1.slider('📉 ST Depression', 0.0, 10.0, 1.0)
    slope = c2.selectbox("🧗‍♀️ Slope of Peak Exercise", ['Upsloping', 'Flat', 'Downsloping'])
    cf = c3.slider('🩺 Major Vessels', 0, 4, 0)
    thal = c1.selectbox('🧬 Thalassemia', ['Normal', 'Fixed defect', 'Reversible Defect'])

    # Mapping for categorical data
    cp_mapping = {'Type1': 0, 'Type2': 1, 'Type3': 2, 'Type': 3}
    slope_map = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    thal_map = {'Normal': 0, 'Fixed defect': 1, 'Reversible Defect': 2}
    gender = 0 if gender == 'Male' else 1
    fbs = 1 if fbs == 'Yes' else 0
    restecg = 0 if restecg == 'Normal' else 1
    ang = 1 if ang == 'Yes' else 0

    if st.button('🔍 Generate Heart Disease Result'):
        result = heart_model.predict([[age, gender, cp_mapping[cp], tresttbs, chol, fbs, restecg, mhra, ang, oldpeak, slope_map[slope], cf, thal_map[thal]]])[0]
        if result == 1:
           st.markdown("<h2 style='font-size: 30px; color: red;text-align:center;'>⚠️ You are likely to have heart disease.</h2>", unsafe_allow_html=True)
        else:
           st.markdown("<h2 style='font-size: 30px; color: green;text-align:center;'>✅ You are not likely to have heart disease.</h2>", unsafe_allow_html=True)







elif selected == 'Parkinson\'s Prediction':
    st.markdown("""
    <style>
        /* Global body style */
        body {
            margin: 0;
        }

        /* Set background image */
        .stApp {
            background-image: url('https://e1.pxfuel.com/desktop-wallpaper/787/971/desktop-wallpaper-blue-white-gradient-backgrounds-blue-white.jpg');
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: background-position 0.5s ease;
        }

        /* Sidebar styling */
        .css-1d391kg {
            transition: all 0.3s ease; /* Sidebar open/close animation */
        }

        /* When sidebar is open, move the background to the left */
        .css-1d391kg.stSidebar {
            width: 300px;
            z-index: 2;
        }

        /* Main content area */
        .css-1d391kg + .css-1v0mbdj {
            padding: 20px;
            width: 100%;
            display: flex;
            flex-direction: column;
            transition: margin-left 0.3s ease; /* Main content shift */
        }

        /* Adjust the content when sidebar is open */
        .stSidebar.stSidebarOpen + .css-1v0mbdj {
            margin-left: 300px;
        }
    </style>
""", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #4682B4;'>Welcome to the Parkinson's Prediction Model 🧠</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 2px solid #4682B4;'>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        /* Style for the slider label */
        .stSlider p {
            border-top: 5px;
            font-size: 20px;
            font-weight: 700;
            color: #1183ed;
            }
        .stButton{
            align: center;
            }
        .stButton p{
            color:#1183ed;
            text-align:center;
            font-size:24px;}

    </style>
""", unsafe_allow_html=True)
    # Input sliders for Parkinson's
    c1, c2, c3 = st.columns(3)
    MDVP_Fo = c1.slider('Average Vocal Fundamental Frequency (MDVP:Fo(Hz))', 0.0, 200.0, 119.992,format='%.3f')
    MDVP_Fhi = c2.slider('Maximum Vocal Fundamental Frequency (MDVP:Fhi(Hz))', 0.0, 200.0, 157.302,format='%.3f')
    MDVP_Flo = c3.slider('Minimum Vocal Fundamental Frequency (MDVP:Flo(Hz))', 0.0, 200.0, 74.997,format='%.3f')

    MDVP_Jitter = c1.slider('Frequency Variation (MDVP:Jitter(%))', 0.0, 10.0, 0.00784,format='%.5f')
    MDVP_Jitter_Abs = c2.slider('Absolute Frequency Variation (MDVP:Jitter(Abs))', 0.0, 1.0, 0.00007,format='%.5f')
    MDVP_RAP = c3.slider('Relative Amplitude Perturbation (MDVP:RAP)', 0.0, 1.0, 0.0037,format='%.5f')

    MDVP_PPQ = c1.slider('Five-Point Period Perturbation Quotient (MDVP:PPQ)', 0.0, 1.0, 0.00554,format='%.5f')
    Jitter_DDP = c2.slider('Difference of Differential Perturbation (Jitter:DDP)', 0.0, 1.0, 0.01109,format='%.5f')

    MDVP_Shim = c3.slider('Amplitude Variation (MDVP:Shimmer)', 0.0, 1.0, 0.04374,format='%.5f')
    MDVP_Shim_dB = c1.slider('Amplitude Variation in Decibels (MDVP:Shimmer(dB))', 0.0, 10.0, 0.426,format='%.3f')

    Shimmer_APQ3 = c2.slider('Three-Point Amplitude Perturbation Quotient (Shimmer:APQ3)', 0.0, 1.0, 0.02182,format='%.5f')
    Shimmer_APQ5 = c3.slider('Five-Point Amplitude Perturbation Quotient (Shimmer:APQ5)', 0.0, 1.0, 0.0313,format='%.5f')
    
    MDVP_APQ = c1.slider('Average Amplitude Perturbation Quotient (MDVP:APQ)', 0.0, 1.0, 0.02971,format='%.5f')
    Shimmer_DDA = c2.slider('Difference of Differential Amplitude (Shimmer:DDA)', 0.0, 1.0, 0.06545,format='%.5f')

    NHR = c3.slider('Noise-to-Harmonics Ratio (NHR)', 0.0, 50.0, 0.02211,format='%.5f')
    HNR = c1.slider('Harmonics-to-Noise Ratio (HNR)', 0.0, 50.0, 21.033,format='%.3f')
    
    RPDE = c2.slider('Recurrence Period Density Entropy (RPDE)', 0.0, 1.0, 0.414783,format='%.6f')
    DFA = c3.slider('Detrended Fluctuation Analysis (DFA)', 0.0, 1.0, 0.815285,format='%.6f')

    spread1 = c1.slider('Fundamental Frequency Spread (spread1)', -10.0, 10.0, -4.813031,format='%.6f')
    spread2 = c2.slider('Frequency Spread (spread2)', -10.0, 10.0, 0.266482,format='%.6f')

    D2 = c3.slider('Nonlinear Dynamical Complexity Measure (D2)', -10.0, 10.0, 2.301442,format='%.6f')
    PPE = c1.slider('Pitch Period Entropy (PPE)', -10.0, 10.0, 0.284654,format='%.6f')

    # When the user presses the button
    if st.button('🔍 Generate Parkinson Disease Result'):
        # Create an input array with the user input values
        input_data = np.array([[MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, 
                                MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shim, MDVP_Shim_dB, 
                                Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, 
                                RPDE, DFA, spread1, spread2, D2, PPE]])

        # Make prediction using the trained model
        prediction = parkinsons_model.predict(input_data)[0]

        # Show result to the user
        if prediction == 1:
           st.markdown("<h2 style='font-size: 30px; color: red;text-align:center;'>⚠️ You are likely to have Parkinson's disease.</h2>", unsafe_allow_html=True)
        else:
           st.markdown("<h2 style='font-size: 30px; color: green;text-align:center;'>✅ You are not likely to have Parkinson's disease.</h2>", unsafe_allow_html=True)
 
