from scrapers.indeed_scraper import search_indeed

def main():
    print("Buscando trabajos en Indeed...\n")

    jobs = search_indeed("risk analyst", "germany")

    print(f"Trabajos encontrados: {len(jobs)}\n")

    for job in jobs[:5]:
        print(job)

if __name__ == "__main__":
    main()
