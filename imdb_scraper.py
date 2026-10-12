from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import re

def scrape_imdb_top_250():
    url = "https://www.imdb.com/chart/top/"
    print("Launching browser for urgent extraction...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, 
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        time.sleep(4)
        
        print("Scrolling to load all movies...")
        for _ in range(12):
            page.evaluate("window.scrollBy(0, 1000);")
            time.sleep(1)
        
        html_content = page.content()
        browser.close()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        titles, years, ratings = [], [], []
        
        seen = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if '/title/tt' in href and not any(x in href for x in ['/plotsummary', '/releaseinfo', '/fullcredits']):
                text = a_tag.get_text(strip=True)
                if text and len(text) > 1 and not text.isdigit() and text not in seen:
                    parent = a_tag.find_parent('li') or a_tag.find_parent('div')
                    parent_text = parent.get_text(separator=' ', strip=True) if parent else ""
                    
                    year_match = re.search(r'\b(19\d\d|20\d\d)\b', parent_text)
                    rating_match = re.search(r'\b([1-9]\.\d)\b', parent_text)
                    
                    if year_match:
                        seen.add(text)
                        titles.append(text)
                        years.append(year_match.group(1))
                        ratings.append(rating_match.group(1) if rating_match else "N/A")
                        
                        if len(titles) >= 250:
                            break

        print(f"Extracted {len(titles)} movies successfully.")

        df = pd.DataFrame({
            "Title": titles[:250],
            "Year": years[:250],
            "Rating": ratings[:250]
        })
        
        output_path = os.path.join(os.getcwd(), "imdb_top_250_movies.csv")
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        
        print(f"\nSUCCESS! CSV saved at:\n{output_path}")
        print(df.head(5))

if __name__ == "__main__":
    scrape_imdb_top_250()