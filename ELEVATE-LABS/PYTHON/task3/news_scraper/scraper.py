import requests
from bs4 import BeautifulSoup
import os

def fetch_headlines(url="https://www.bbc.com/news"):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all(["h2", "h3"])

        results = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []

def save_to_file(headlines, filename="headlines.txt"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")

def clear_headlines(filename="headlines.txt"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    if os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("")  
        print(f"🗑 Cleared contents of {filename}")
    else:
        print(f"⚠ {filename} does not exist.")

def menu():
    while True:
        print("\n=== 📰 News Scraper Menu ===")
        print("1. Fetch & Save Headlines")
        print("2. Clear Headlines File")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            news_headlines = fetch_headlines()
            if news_headlines:
                save_to_file(news_headlines)
                print(f"✅ Saved {len(news_headlines)} headlines to headlines.txt")
            else:
                print("⚠ No headlines found.")
        elif choice == "2":
            clear_headlines()
        elif choice == "3":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
