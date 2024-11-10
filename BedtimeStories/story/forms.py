from django import forms

class StoryForm(forms.Form):
    age_group = forms.ChoiceField(choices=[('3-5', '3-5'), ('6-8', '6-8'), ('9-12', '9-12')], label="Age Group")
    character = forms.CharField(max_length=100, label="Character")
    theme = forms.CharField(max_length=100, label="Theme")
