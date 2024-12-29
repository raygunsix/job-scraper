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

def display_jobs(jobs):
    print()
    for job in jobs:
        print(f"{job[0]} jobs found:", *job[2], sep='\n- ')
        print()
    return None

if __name__ == "__main__":
    pages = read_career_pages('pages.csv')
    keywords = read_keywords('keywords.csv')
    jobs = scrape_jobs(pages, keywords)
    display_jobs(jobs)
