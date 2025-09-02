import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_search_url(keyword):
    if not keyword:
        raise ValueError("Keyword cannot be empty. Please provide a valid search term.")
    else:
        keyword = keyword.strip().lower().replace(" ", "-")
        return f"https://remoteok.com/remote-{keyword}-jobs"

def scrape_jobs(search_term):
    url = get_search_url(search_term)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch data. Check the keyword or try again later.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    job_rows = soup.find_all("tr", class_="job")
    jobs = []
    for job in job_rows:
        company = job.get("data-company")
        position = job.find("td", class_="company_and_position").select("a > h2[itemprop='title']")[0].text.strip()
        date = job.find("td", class_="time").select("time")[0]["datetime"].strip() 
        date = pd.to_datetime(date).strftime("%Y-%m-%d")
        tags = [tag.text.strip() for tag in job.find("td", class_="tags").select("a") if tag.text.strip()]
        link = job.get("data-url")
        jobs.append({
            "Company": company,
            "Position": position,
            "Date Posted": date,
            "Tags": tags[:5],
            "Link": f"https://remoteok.com{link}"
        })

    return jobs

def main():
    search_input = input("Enter the job role or technology to search (e.g., Python, React, DevOps):")
    if not search_input.strip():
        print("No search term provided. Exiting.")
        return

    job_list = scrape_jobs(search_input)
    if job_list:
        df = pd.DataFrame(job_list)
        filename = f"remoteok_{search_input.lower().replace(' ', '_')}_jobs.csv"
        df.to_csv(filename, index=False)
        print(f"{len(df)} jobs found for {search_input}. Saved to {filename}")
    else:
        print("No jobs found or an error occurred.")

if __name__ == "__main__":
    main()