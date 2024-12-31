import os
import re
import requests
from bs4 import BeautifulSoup

def extract_and_save_chapters(html_url, output_dir):
    """
    Downloads the HTML content, extracts chapters, and saves each chapter as a separate .txt file.
    """
    # Fetch the HTML content
    response = requests.get(html_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate chapter markers (e.g., "Book", "Chapter")
    chapter_markers = soup.find_all(['h2', 'h3'], string=re.compile(r"Chapter|Book", re.IGNORECASE))

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not chapter_markers:
        raise ValueError("No chapters found in the HTML content. Check the structure of the page.")

    # Process each chapter
    for i, marker in enumerate(chapter_markers, start=1):
        chapter_title = marker.get_text(strip=True)
        chapter_content = []

        # Extract all text under the chapter until the next chapter marker
        sibling = marker.find_next_sibling()
        while sibling and sibling.name == 'p':
            chapter_content.append(sibling.get_text(strip=True))
            sibling = sibling.find_next_sibling()

        # Save the chapter as a .txt file
        file_name = f"Chapter_{i}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"{chapter_title}\n\n{'\n\n'.join(chapter_content)}")
        print(f"Saved: {file_path}")

def main():
    """
    Main function to extract chapters from a provided HTML page URL.
    """
    # Input: URL of the HTML page
    html_url = "https://www.gutenberg.org/cache/epub/26073/pg26073-images.html"
    output_dir = "The_Metamorphoses"

    # Extract and save chapters
    print(f"Extracting chapters from: {html_url}")
    try:
        extract_and_save_chapters(html_url, output_dir)
        print(f"All chapters have been successfully saved in the folder: {output_dir}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
