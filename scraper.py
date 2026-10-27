import requests
from bs4 import BeautifulSoup

url = input('Enter a URL [ex: example.com ]: ')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',}

res = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(res.text, 'html.parser')

tags = soup.find(['a', 'p', 'h1', 'h2', 'h3', 'h4'])

res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

for element in soup(["script", "style", "noscript", "svg"]):
        element.decompose()

text = soup.get_text(separator="\n", strip=True)

print(text)