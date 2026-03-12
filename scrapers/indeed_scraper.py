import requests
from bs4 import BeautifulSoup


def search_indeed(query="risk analyst", location="germany"):
    url = "https://www.indeed.com/jobs"
    params = {
        "q": query,
        "l": location
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error al acceder a Indeed: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_card in soup.find_all("div", class_="job_seen_beacon"):
        title_tag = job_card.find("h2")
        company_tag = job_card.find("span", attrs={"data-testid": "company-name"})
        location_tag = job_card.find("div", attrs={"data-testid": "text-location"})

        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        company = company_tag.get_text(strip=True) if company_tag else "N/A"
        location = location_tag.get_text(strip=True) if location_tag else "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })

    return jobs
