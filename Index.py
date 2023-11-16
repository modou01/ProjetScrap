import requests
from bs4 import BeautifulSoup
import csv

# Fonction pour extraire les liens d'une page
def extract_links(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        return links
    else:
        print(f"Échec de la requête. Code d'état: {response.status_code}")
        return None

# Fonction pour nettoyer les liens
def clean_links(links):
    cleaned_links = []
    for link in links:
        cleaned_links.append({
            'text': link.get_text(),
            'href': link.get('href')
        })
    return cleaned_links

# Fonction pour enregistrer les données dans un fichier CSV
def save_to_csv(data, filename='extracted_data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['text', 'href']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"Les données ont été enregistrées dans {filename}")

# URL de la page à scraper
url_to_scrape = 'https://www.lidl.fr/'

# 1. Extraction des liens
links = extract_links(url_to_scrape)

if links is not None:
    # 2. Nettoyage des liens
    cleaned_links = clean_links(links)

    # 3. Enregistrement des données dans un fichier CSV
    save_to_csv(cleaned_links)
