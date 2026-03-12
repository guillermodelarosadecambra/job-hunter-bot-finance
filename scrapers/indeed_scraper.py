from playwright.sync_api import sync_playwright


def search_indeed(query="risk analyst", location="germany"):
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = f"https://www.indeed.com/jobs?q={query}&l={location}"
        page.goto(url, timeout=60000)
        page.wait_for_timeout(3000)

        job_cards = page.locator("div.job_seen_beacon")
        count = job_cards.count()

        for i in range(min(count, 10)):
            job = job_cards.nth(i)

            title = job.locator("h2").inner_text() if job.locator("h2").count() > 0 else "N/A"
            company = job.locator('[data-testid="company-name"]').inner_text() if job.locator('[data-testid="company-name"]').count() > 0 else "N/A"
            job_location = job.locator('[data-testid="text-location"]').inner_text() if job.locator('[data-testid="text-location"]').count() > 0 else "N/A"

            jobs.append({
                "title": title,
                "company": company,
                "location": job_location
            })

        browser.close()

    return jobs
