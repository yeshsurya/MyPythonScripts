import requests
from bs4 import BeautifulSoup
from collections import deque

# URL of the website to scrape
url = "https://www.example.com"

# Maximum depth for breadth-first traversal
max_depth = 2

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Initialize a queue for breadth-first traversal
queue = deque([(url, 0)])  # (url, depth)

# Initialize a set to store visited URLs
visited = set()

# Initialize a dictionary to store scraped content
scraped_content = {}

# Perform breadth-first traversal
while queue:
    current_url, depth = queue.popleft()

    # Skip URLs beyond the maximum depth
    if depth > max_depth:
        continue

    # Skip already visited URLs
    if current_url in visited:
        continue

    # Send a GET request to the current URL
    response = requests.get(current_url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the desired content on the webpage
    content = soup.get_text()

    # Add the content to the dictionary using the URL as the key
    scraped_content[current_url] = content

    # Mark the current URL as visited
    visited.add(current_url)

    # Find all hyperlinks on the webpage
    links = soup.find_all("a")

    # Enqueue the hyperlinks with incremented depth
    for link in links:
        href = link.get("href")

        # Skip external links or links with empty href
        if href and href.startswith("http") and href not in visited:
            queue.append((href, depth + 1))

# Save the scraped content into a single text file
with open("scraped_content.txt", "w", encoding="utf-8") as file:
    for url, content in scraped_content.items():
        file.write(f"URL: {url}\n\n")
        file.write(content)
        file.write("\n\n---\n\n")

print("Web scraping and saving complete.")
