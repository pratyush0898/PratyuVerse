import requests
from bs4 import BeautifulSoup

def load_personal_data(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_urls(urls_path):
    with open(urls_path, 'r', encoding='utf-8') as f:
        return [url.strip() for url in f.readlines()]

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def gather_data():
    personal_data = load_personal_data("../data/data.txt")
    urls = load_urls("../data/domains.txt")

    # Save personal data to text file
    with open("../data/collected_data.txt", 'w', encoding='utf-8') as f:
        f.write(personal_data + "\n\n")

    # Scrape website data and append it
    for url in urls:
        scraped_data = scrape_website(url)
        with open("../data/collected_data.txt", 'a', encoding='utf-8') as f:
            f.write(scraped_data + "\n\n")

if __name__ == "__main__":
    gather_data()
