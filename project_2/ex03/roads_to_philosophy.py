import requests
import sys
from bs4 import BeautifulSoup
import re
import time

WIKI_BASE_URL = "https://en.wikipedia.org"
TARGET_PAGE = "philosophy"
    
"""
Gets the first valid link from the Wikipedia page, ignoring links in italic font,
links within parentheses, and invalid Wikipedia links.

:param page_url: Full URL of the Wikipedia page to parse.
:return: The full URL of the first valid Wikipedia link or None if no valid link is found.
"""
def get_first_valid_link(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the main content of the page (ignores tables, info boxes, etc.)
    content_div = soup.find(id="mw-content-text")

    if content_div is None:
        return None

    main_content = content_div.find('div', class_="mw-parser-output")

    for element in main_content.find_all('p'):
        # Iterate through all the <a> tags
        for link in element.find_all("a", href=True):
            href = link['href']
            # Ignore links that are italicized
            if link.find_parent("i") or link.find_parent("em") or link.find_parent("table"):
                continue

            # Ignore links that do not point to other Wikipedia articles
            if not href.startswith("/wiki/") or ':' in href:
                continue

            # Get the full URL of the link
            return WIKI_BASE_URL + href
    return None

def get_page_title(page_url):
    """Extracts the title from a Wikipedia URL."""
    return page_url.split("/wiki/")[-1].replace("_", " ").lower()

def roads_to_philosophy(start_page):
    visited_pages = []
    current_url = WIKI_BASE_URL + "/wiki/" + start_page
    number_of_links = 0

    while True:
        title = get_page_title(current_url)
        print(title)

        if title == TARGET_PAGE:
            print(f'{number_of_links} roads from {start_page} to {TARGET_PAGE}!')
            break
        # Check if we already visited this page
        if current_url.lower() in visited_pages:
            print('It leads to an infinite loop!')
            break
        # Get the next valid link on the current page
        next_link = get_first_valid_link(current_url.lower())
        if not next_link:
            print("It leads to a dead end!")
            break
        visited_pages.append(current_url.lower())
        number_of_links += 1
        # Update the current URL to the next valid link for the next iteration
        current_url = next_link
        time.sleep(0.3)  # Be polite to Wikipedia servers


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3.10 roads_to_philosophy 'PAGE TITLE'")
        sys.exit(1)

    start_page = sys.argv[1].lower()
    roads_to_philosophy(start_page)
