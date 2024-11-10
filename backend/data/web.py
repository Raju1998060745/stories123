#import pandas as pd

#df = pd.read_csv("hf://datasets/FareedKhan/1k_stories_100_genre/1k_stories_100_genre.csv") #data set for genre

#print (df.head())
import requests
from bs4 import BeautifulSoup

def get_disney_princesses(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    princesses = []
    
    # Find the section with official princesses
    official_princesses_section = soup.find('span', {'id': 'Official_Princesses'})
    if official_princesses_section:
        parent_element = official_princesses_section.find_parent('h2')
        if parent_element:
            next_element = parent_element.find_next_sibling()
            while next_element and next_element.name != 'h2':
                if next_element.name == 'p' and next_element.find('b'):
                    princess_name = next_element.find('b').get_text(strip=True)
                    description = ""
                    # Collect all the description paragraphs
                    description_element = next_element.find_next_sibling('p')
                    while description_element and description_element.name == 'p':
                        description += description_element.get_text(strip=True) + " "
                        description_element = description_element.find_next_sibling('p')
                    princesses.append({'name': princess_name, 'description': description.strip()})
                next_element = next_element.find_next_sibling()
    
    return princesses

def save_to_text(princesses, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for princess in princesses:
            file.write(f"Name: {princess['name']}\n")
            file.write(f"Description: {princess['description']}\n")
            file.write("\n")


def main():
    url = 'https://disneyprincess.fandom.com/wiki/List_of_Disney_Princesses'
    princesses = get_disney_princesses(url)
    
    if princesses:
        save_to_text(princesses, 'disney_princesses.txt')
        print('Data saved to disney_princesses.txt')
    else:
        print('No data found.')

if __name__ == '__main__':
    main()

