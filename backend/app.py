from flask import Flask, request, jsonify
import subprocess
import json

# Initialize Flask app
app = Flask(__name__)

# Define the endpoint for generating bedtime stories
@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    character = data.get("character")
    theme = data.get("theme")
    age_group = data.get("age_group")
    
    # Ensure all required parameters are provided
    if not character or not theme or not age_group:
        return jsonify({"error": "Missing required parameters"}), 400

    # Define the prompt
    prompt = f"Write a short bedtime story for a {age_group}-year-old. The story should include {character} and be about {theme}."

    try:
        # Call ollama CLI to generate the story using llama3
        result = subprocess.run(
            ["ollama", "generate", "llama3", "--prompt", prompt],
            capture_output=True,
            text=True,
            check=True
        )

        # Parse and return the generated story
        story = result.stdout.strip()
        return jsonify({"story": story})

    except subprocess.CalledProcessError as e:
        # Handle errors from the ollama command
        return jsonify({"error": "Failed to generate story", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
