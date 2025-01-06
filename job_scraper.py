import csv
import sys

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def read_career_pages(file_path):
    pages = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                org = row[0]
                url = row[1]
                pages.append([org, url])
            except IndexError:
                print("Error reading career pages csv file. Exiting")
                sys.exit(1)
    return pages

def read_keywords(file_path):
    keywords = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            keywords.append(row[0])
        return keywords

def scrape_jobs(pages, keywords):
    jobs = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for page_info in pages:
            org = page_info[0]
            url = page_info[1]

            print(f"Checking {org}")

            page.goto(url)
            page.wait_for_timeout(3000)
            content = page.content()

            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            
            matches = []

            for keyword in keywords:
                if keyword in text:
                    matches.append(keyword)

            if matches:        
                jobs.append([org, url, matches])
        
        browser.close()

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
