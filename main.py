import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_TOKEN = os.environ.get('AIRTABLE_TOKEN')
BASE_ID = os.environ.get('BASE_ID')
TABLE_NAME = os.environ.get('TABLE_NAME')


def scrape_jobs():
    url = "https://remoteok.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    results = []
    for job in jobs:
        title = job.find("h2")
        company = job.find("h3")
        link = job.get("data-href")
        if title and company:
            results.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
                "link": f"https://remoteok.com{link}"
            })
    return results

def post_to_airtable(job):
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "fields": {
            "Title": job["title"],
            "Company": job["company"],
            "Link": job["link"],
            "Tags": "Python"
        }
    }
    requests.post(url, json=data, headers=headers)

if __name__ == "__main__":
    jobs = scrape_jobs()
    for job in jobs[:5]:
        post_to_airtable(job)
