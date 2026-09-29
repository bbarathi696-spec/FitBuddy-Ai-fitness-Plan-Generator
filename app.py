import streamlit as st
import google.generativeai as genai
import os

# Page Config
st.set_page_config(page_title="FitBuddy AI", page_icon="💪", layout="wide")
st.title("💪 FitBuddy - AI Fitness Plan Generator")
st.markdown("Your Personal AI Trainer using **Google Gemini AI** | Google Cloud GenAI Project")

# Sidebar - User Input
st.sidebar.header("Enter Your Details")
age = st.sidebar.number_input("Age", 15, 80, 22)
weight = st.sidebar.number_input("Weight (kg)", 30, 150, 65)
height = st.sidebar.number_input("Height (cm)", 100, 220, 170)
goal = st.sidebar.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Stay Fit", "Weight Gain"])
diet_type = st.sidebar.selectbox("Diet Type", ["Veg", "Non-Veg", "Vegan", "Eggetarian"])
api_key = st.sidebar.text_input("Gemini API Key (for demo)", type="password")

if st.sidebar.button("Generate My Plan"):
    if not api_key:
        st.error("Please enter Gemini API Key to generate plan. Get free key from aistudio.google.com")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Act as a professional fitness trainer and dietitian.
            Create a personalized 7-day plan for:
            Age: {age}, Weight: {weight}kg, Height: {height}cm, Goal: {goal}, Diet: {diet_type}
            
            Provide:
            1. 7-Day Workout Plan (with exercises, sets, reps)
            2. 7-Day Diet Plan (Breakfast, Lunch, Dinner, Snacks with calories)
            3. 3 Important Tips for {goal}
            
            Format it clearly with emojis.
            """
            
            with st.spinner("FitBuddy is creating your personal plan..."):
                response = model.generate_content(prompt)
                st.success("Your Plan is Ready!")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

st.info("This project is built for SkillWallet - Google Cloud Generative AI Learning Path")
