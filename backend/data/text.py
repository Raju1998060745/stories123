import re

# Function to format the content
def format_princess_content(content):
    # Split content by Main article indicators which seem to denote new sections
    sections = re.split(r'Main article:', content)
    formatted_sections = []

    for section in sections:
        if section.strip():
            # Attempt to extract the name and format the rest of the section
            name_match = re.match(r'(\w+\s\w+)', section)
            if name_match:
                name = name_match.group(1)
                rest_of_section = section[len(name):].strip()
                formatted_section = f"Name: {name}\nDescription: {rest_of_section}\n\n"
                formatted_sections.append(formatted_section)

    return ''.join(formatted_sections)

# Read the content from the text file
with open('disney_princesses.txt', 'r') as file:
    content = file.read()

# Format the content
formatted_content = format_princess_content(content)

# Write the formatted content to a new text file
with open('formatted_disney_princesses.txt', 'w') as file:
    file.write(formatted_content)

print("The content has been formatted and saved to 'formatted_disney_princesses.txt'")
