import gradio as gr
import requests
import io
import os
from PIL import Image
from googleapiclient.discovery import build

# API and Model Setup using environment variables for security
headers = {"Authorization": os.getenv('HF_API_KEY')}
YOUTUBE_DATA_API = os.getenv('YOUTUBE_API_KEY')
mealdb_base_url = os.getenv('MEALDB_BASE_URL')

youtube = build('youtube', 'v3', developerKey=YOUTUBE_DATA_API)

# Function to convert image to base64 (unused in this script but defined)
def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    import base64
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Function to perform inference on the image using a Hugging Face model
def perform_inference(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    data = buffered.getvalue()
    model_url = "https://api-inference.huggingface.co/models/juliensimon/autotrain-food101-1471154053"
    response = requests.post(model_url, headers=headers, data=data)
    result = response.json()
    return result[0]['label']

# Function to search YouTube videos based on a query
def search_youtube_videos(query):
    search_params = {
        'q': query + " recipe",
        'part': 'snippet',
        'maxResults': 5,
        'type': 'video',
    }
    search_response = youtube.search().list(**search_params).execute()
    video_ids = [item['id']['videoId'] for item in search_response['items']]
    return [f"https://www.youtube.com/embed/{video_id}" for video_id in video_ids]

# Function to get recipe details from TheMealDB
def get_recipe_details(query):
    response = requests.get(f"{mealdb_base_url}search.php?s={query}")
    data = response.json()
    meals = data.get('meals', [])
    if meals:
        meal_id = meals[0]['idMeal']
        details_response = requests.get(f"{mealdb_base_url}lookup.php?i={meal_id}")
        details_data = details_response.json()
        recipe = details_data['meals'][0]
        ingredients = "\n".join([f"{recipe[f'strIngredient{i}']}: {recipe[f'strMeasure{i}']}" for i in range(1, 21) if recipe[f'strIngredient{i}']])
        return f"{recipe['strMeal']} -\n\nSteps:\n{recipe['strInstructions']}\n\nIngredients:\n{ingredients}"
    return "Recipe details not found."

# Function to generate HTML content for embedding videos
def generate_embed_html(video_links):
    html_content = "<div>"
    for video in video_links:
        html_content += f'<iframe width="560" height="315" src="{video}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    html_content += "</div>"
    return html_content

# Gradio interface function that handles image uploads and processes the data
def gradio_interface(image):
    dish_name = perform_inference(image)
    youtube_links = search_youtube_videos(dish_name)
    recipe_details = get_recipe_details(dish_name)
    youtube_html = generate_embed_html(youtube_links)
    return dish_name, recipe_details, youtube_html

iface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=[
        gr.Textbox(label="Predicted Dish"),
        gr.Textbox(label="Recipe Details"),
        gr.HTML(label= "YouTube Recipe Videos")  # Changed to gr.HTML
        
    ],

    title="Dish Prediction, Recipe Details, and Recipe Videos",
    description="Upload an image of food, and the app will predict the dish, provide YouTube links for recipes, and fetch detailed recipe instructions."
)

if __name__ == "__main__":
    iface.launch()
