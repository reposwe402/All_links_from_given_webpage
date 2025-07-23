from bs4 import BeautifulSoup

def parse_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))
    return links
