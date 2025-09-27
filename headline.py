import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  # avoid blocks
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find headlines (depends on site structure, here <h2> used)
        headlines = soup.find_all("h2")

        with open(output_file, "w", encoding="utf-8") as f:
            for h in headlines:
                text = h.get_text(strip=True)
                if text:
                    f.write(text + "\n")

        print(f"✅ Headlines saved to {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Example: scraping BBC
scrape_headlines("https://www.bbc.com/news")
