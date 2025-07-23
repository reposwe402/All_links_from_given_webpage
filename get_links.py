from input_handler import get_url
from data_fetcher import fetch_data
from html_parser import parse_html
from file_writer import save_links

from utils import save_links

url = get_url()
data = fetch_data(url)
links = parse_html(data.text)
save_links(links)
