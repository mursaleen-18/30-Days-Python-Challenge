import requests
from bs4 import BeautifulSoup

# Step 1: Target URL
url = "https://www.bbc.com/news"

# Step 2: Send HTTP GET request
response = requests.get(url)

# Step 3: Parse HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines - usually in <h3> tags with specific classes
# We'll use class-based search to get more accurate results
headlines = soup.find_all("h3")

# Step 5: Display top 10 headlines
print("📰 Top 10 BBC News Headlines:\n")
count = 1
for headline in headlines:
    text = headline.get_text(strip=True)
    if text:
        print(f"{count}. {text}")
        count += 1
    if count > 10:
        break
