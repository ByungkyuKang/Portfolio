from bs4 import BeautifulSoup
import requests
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_url = "https://n.news.naver.com/mnews/article/001/0015687802?rc-N&ntype-RANKING"
response = requests.get(target_url)
html_context = response.text
soup = BeautifulSoup(html_context, "html.parser")
print(soup)

# title_element = soup.select_one('h2.media_end_head_headline') or \
#     soup.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
# title = title_element.get_text(strip=True) if title_element else None
# print(title)