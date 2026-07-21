import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


load_dotenv()

MODEL_NAME = "gemini-2.5-flash"


st.set_page_config(page_title="Recipe Generator", page_icon=":material/restaurant:", layout="centered")
st.title("AI Recipe Generator")
st.caption("Enter what you have in the kitchen and get a simple recipe.")


@st.cache_resource
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("GEMINI_API_KEY was not found. Add it to your .env file first.")
        st.stop()
    return genai.Client(api_key=api_key)


def build_recipe_prompt(
    ingredients,
    cuisine,
    meal_type,
    dietary_preference,
    cooking_time,
    servings,
    skill_level,
    extra_notes,
):
    prompt_parts = [
        "You are a helpful professional chef.",
        "Create one practical, tasty recipe using the user's available ingredients.",
        f"Available ingredients: {ingredients}",
        f"Meal type: {meal_type}",
        f"Servings: {servings}",
        f"Cooking time target: {cooking_time}",
        f"Cooking skill level: {skill_level}",
    ]

    if cuisine != "Any":
        prompt_parts.append(f"Cuisine style: {cuisine}")

    if dietary_preference != "No preference":
        prompt_parts.append(f"Dietary preference: {dietary_preference}")

    if extra_notes.strip():
        prompt_parts.append(f"Extra notes: {extra_notes}")

    prompt_parts.append(
        """
Return the recipe in Markdown with exactly these sections:

# Recipe Name
Short description.

## Ingredients
- Include quantities where possible.

## Instructions
1. Clear step-by-step method.

## Chef Tips
- 2 useful tips or substitutions.
"""
    )

    return "\n".join(prompt_parts)


with st.form("recipe_form"):
    ingredients = st.text_area(
        "Ingredients",
        placeholder="Example: rice, eggs, onion, tomato, garlic, cheese",
        height=100,
    )

    col1, col2 = st.columns(2)
    with col1:
        cuisine = st.selectbox(
            "Cuisine",
            [
                "Any",
                "Indian",
                "Italian",
                "Mexican",
                "Chinese",
                "Thai",
                "Mediterranean",
                "American",
            ],
        )
        meal_type = st.selectbox(
            "Meal type",
            ["Dinner", "Lunch", "Breakfast", "Snack", "Dessert"],
        )
        servings = st.number_input("Servings", min_value=1, max_value=12, value=2)

    with col2:
        dietary_preference = st.selectbox(
            "Dietary preference",
            [
                "No preference",
                "Vegetarian",
                "Vegan",
                "Gluten-free",
                "Dairy-free",
                "Low-carb",
                "High-protein",
            ],
        )
        cooking_time = st.selectbox(
            "Cooking time",
            ["Under 15 minutes", "Under 30 minutes", "Under 45 minutes", "No limit"],
        )
        skill_level = st.selectbox("Skill level", ["Beginner", "Intermediate", "Advanced"])

    extra_notes = st.text_input(
        "Extra notes",
        placeholder="Example: make it spicy, no oven, kid-friendly",
    )

    submitted = st.form_submit_button("Generate recipe")


if submitted:
    if not ingredients.strip():
        st.warning("Please enter at least one ingredient.")
    else:
        prompt = build_recipe_prompt(
            ingredients=ingredients,
            cuisine=cuisine,
            meal_type=meal_type,
            dietary_preference=dietary_preference,
            cooking_time=cooking_time,
            servings=servings,
            skill_level=skill_level,
            extra_notes=extra_notes,
        )

        with st.spinner("Generating your recipe..."):
            try:
                client = get_client()
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                )
                st.divider()
                st.markdown(response.text)
            except Exception as exc:
                st.error(f"Could not generate the recipe: {exc}")
