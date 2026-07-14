import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"

st.set_page_config(page_title="Recipe Generator", page_icon="🍳")
st.title("🍳 AI Recipe Generator")
st.caption("Tell it what you have, and it'll cook up a recipe.")


@st.cache_resource
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("GEMINI_API_KEY not found. Add it to your .env file.")
        st.stop()
    return genai.Client(api_key=api_key)


def build_prompt(ingredients, cuisine, diet, servings, extra_notes):
    lines = [
        "You are a professional chef. Write a clear, easy-to-follow recipe.",
        f"Main ingredients to use: {ingredients}.",
        f"Number of servings: {servings}.",
    ]
    if cuisine and cuisine != "Any":
        lines.append(f"Cuisine style: {cuisine}.")
    if diet and diet != "None":
        lines.append(f"Dietary requirement: {diet}.")
    if extra_notes:
        lines.append(f"Additional notes: {extra_notes}.")
    lines.append(
        "Format the response in Markdown with a title, a short description, "
        "an 'Ingredients' section (as a bulleted list with quantities), and "
        "an 'Instructions' section (as numbered steps)."
    )
    return "\n".join(lines)


with st.form("recipe_form"):
    ingredients = st.text_input(
        "Ingredients you have (comma-separated)",
        placeholder="e.g. chicken breast, spinach, garlic, lemon",
    )
    col1, col2 = st.columns(2)
    with col1:
        cuisine = st.selectbox(
            "Cuisine style",
            ["Any", "Italian", "Indian", "Mexican", "Chinese", "Thai", "Mediterranean", "American"],
        )
    with col2:
        diet = st.selectbox(
            "Dietary requirement",
            ["None", "Vegetarian", "Vegan", "Gluten-free", "Low-carb", "Dairy-free"],
        )
    servings = st.number_input("Servings", min_value=1, max_value=12, value=2)
    extra_notes = st.text_area("Anything else? (optional)", placeholder="e.g. under 30 minutes, spicy")
    submitted = st.form_submit_button("Generate Recipe")

if submitted:
    if not ingredients.strip():
        st.warning("Please enter at least one ingredient.")
    else:
        client = get_client()
        prompt = build_prompt(ingredients, cuisine, diet, servings, extra_notes)
        with st.spinner("Cooking up your recipe..."):
            try:
                response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
