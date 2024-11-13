import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.llms.ollama import Ollama  # Directly import Ollama
from indexing import retrieve_query

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the Ollama model once at startup
model = Ollama(model="tinyllama")

# Define the endpoint for generating bedtime stories
@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    character = data.get("character")
    theme = data.get("theme")
    age_group = data.get("age_group")
    store= retrieve_query(character,k=2)
    

    
    # Ensure all required parameters are provided
    if not character or not theme or not age_group:
        return jsonify({"error": "Missing required parameters"}), 400

    # Define the prompt
    prompt = f"Write a short bedtime story for a {age_group}-year-old. The story should include {character} and be about {theme}. Only based on description of the character {store}"
    app.logger.debug("Generated prompt: %s", prompt)

    try:
        # Generate the story using the Ollama model
        response_text = model.invoke(prompt)
        return jsonify({"story": response_text.strip()})

    except Exception as e:
        # Handle errors from Ollama model invocation
        app.logger.error("Error generating story: %s", str(e))
        return jsonify({"error": "Failed to generate story", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
