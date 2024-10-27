import requests
from django.shortcuts import render
from .forms import StoryForm

def generate_story(request):
    story = ""
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            data = {
                'age_group': form.cleaned_data['age_group'],
                'character': form.cleaned_data['character'],
                'theme': form.cleaned_data['theme']
            }
            # Send the data to the Flask app
            response = requests.post('http://localhost:5000/generate_story', json=data)
            if response.status_code == 200:
                story = response.json().get('story', 'No story found')
            else:
                story = "Error generating story."
    else:
        form = StoryForm()
    
    return render(request, 'story/generate_story.html', {'form': form, 'story': story})
