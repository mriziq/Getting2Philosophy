# Wikipedia to Philosophy Script

This script is designed to explore the "Wikipedia Philosophy" phenomenon, where clicking the first link in the main text of a Wikipedia article and repeating the process eventually leads to the Philosophy article.

## Script Overview

The script performs the following steps:

1. **Start from a Random Wikipedia Article**: It begins by opening a random Wikipedia article.
2. **Find the First Link**: It parses the HTML of the article to find the first link within the first paragraph.
3. **Traverse to the Linked Article**: It follows the link to the next article.
4. **Repeat Until Philosophy**: This process repeats until the script reaches the Wikipedia Philosophy article, encounters an article with no valid links, or detects a loop.

### Key Components

- **HTMLParser Subclass (LinkFinder)**: A custom HTML parser that identifies the first valid link in a Wikipedia article's first paragraph.
- **find_first_link(url)**: Function to fetch and parse a Wikipedia article, returning the first valid link.
- **get_to_philosophy()**: Main function to start the process from a random article and continue following the first link until a termination condition is met.

## Usage

Simply run the script in a Python environment. The script will print each visited URL, and notify when it reaches the Philosophy article, detects a loop, or finds no further links.

```python
python3 main.py
```

### Dependencies

- Python 3.x
- `urllib` and `html.parser` modules (included in the Python standard library)
A requirements.txt file is not necessary for this script as it only uses Python standard library modules (urllib, html.parser, time). No external dependencies are required.

### Note

The script includes a delay (`time.sleep(2)`) between requests to prevent overloading Wikipedia's servers.

### Author

@mriziq