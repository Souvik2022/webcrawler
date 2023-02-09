import requests
import csv
from bs4 import BeautifulSoup

#function starts here

def crawl_urls(primary_category, secondary_category, geography, date_range):
    base_url = "https://www.google.com/search?q="
    search_query = primary_category + "+" + secondary_category + "+" + geography + "+" + date_range
    url = base_url + search_query

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    urls = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith("/url?q="):
            url = href[7:]
            urls.append(url)

    with open("urls.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["URL"])
        for url in urls:
            writer.writerow([url])

# exampler data given
crawl_urls("Medical Journal", "Orthopedic", "India", "2022-23")
