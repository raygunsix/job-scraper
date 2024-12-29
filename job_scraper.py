import csv
import requests

from bs4 import BeautifulSoup

def read_career_pages(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)

def read_keywords(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)

def scrape_jobs(pages, keywords):
    jobs = []
    for page in pages:
        org = page[0]
        url = page[1]

        print(f"Checking {org}")

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        findings = soup.find_all(string=keywords)
        
        if findings:
            jobs.append([org, url, findings])

    return jobs

if __name__ == "__main__":
    pages = read_career_pages('pages.csv')
    keywords = read_keywords('keywords.csv')
    jobs = scrape_jobs(pages, keywords)
    print(jobs)
