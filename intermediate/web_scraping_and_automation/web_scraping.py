from bs4 import BeautifulSoup
import requests
import pprint as pp

site = "https://news.ycombinator.com/news"
robots = "https://news.ycombinator.com/robots.txt"

# pp.pprint(requests.get(robots).text)
yc_web_page = requests.get(url=site).text
soup = BeautifulSoup(yc_web_page, "html.parser")

all_title_spans = soup.find_all(name="span", class_="titleline")
all_title_anchor_tags = []
for span in all_title_spans:
    all_title_anchor_tags.append(span.find(name="a"))

all_article_upvote_spans = soup.find_all(name="span", class_="score")
all_article_upvote_elements = []
for span in all_article_upvote_spans:
    all_article_upvote_elements.append(span.get_text())

titles_list, links_list, upvote_list = [], [], []
for tag in all_title_anchor_tags:
    titles_list.append(tag.getText())
    links_list.append(tag.get("href"))

for upvote in all_article_upvote_elements:
    up = int(upvote.split()[0])
    upvote_list.append(up)

result = list(zip(titles_list, links_list, upvote_list))
result.sort(key=lambda x: x[2], reverse=True)
pp.pprint(result)