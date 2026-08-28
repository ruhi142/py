import csv
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "job_listings.csv"


def fetch_page(url):
    
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_jobs(html):
    """Parse job cards from the HTML and return a list of job dicts."""
    soup = BeautifulSoup(html, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []
    for card in job_cards:
        title_tag = card.find("h2", class_="title")
        company_tag = card.find("h3", class_="subtitle")
        location_tag = card.find("p", class_="location")
        links = card.find_all("a")

        job_title = title_tag.get_text(strip=True) if title_tag else "N/A"
        company = company_tag.get_text(strip=True) if company_tag else "N/A"
        location = location_tag.get_text(strip=True) if location_tag else "N/A"

        # the second <a> tag is the "Apply" link to job detail page
        job_url = links[1]["href"] if len(links) > 1 else "N/A"

        jobs.append({
            "job_title": job_title,
            "company": company,
            "location": location,
            "job_url": job_url,
        })

    return jobs


def save_to_csv(jobs, filename):
    if not jobs:
        print("No job data to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=jobs[0].keys())
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Saved {len(jobs)} job listings to '{filename}'.")


def main():
    print(f"Fetching job listings from {URL} ...")
    html = fetch_page(URL)
    jobs = parse_jobs(html)
    save_to_csv(jobs, OUTPUT_FILE)


if __name__ == "__main__":
    main()

