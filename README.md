# Web-Scraper-for-News-Headlines

This is a Python script that scrapes headlines from a news website using the requests and BeautifulSoup libraries. It will fetch the HTML content, parse it to find headline tags, and save the headlines to a text file.



==> requests.get(url): This function sends a GET request to the specified URL to retrieve the webpage's HTML content. Theheaders dictionary with a User-Agent is included to mimic a web browser, which can help prevent the server from blocking the request.

==> BeautifulSoup(response.text, 'html.parser'): This creates a BeautifulSoup object (often called soup) that parses the raw HTML text from the response, making it easier to navigate and search for specific elements.

==> soup.find_all('h2'): This method searches the entire HTML document (the soup object) and returns a list of all elements that are "h2" tags.

==> .get_text(strip=True): This extracts the text content from a BeautifulSoup element. The strip=True argument removes any leading or trailing whitespace from the text.

==> try-except block: This is used to handle potential errors, such as a network issue or an invalid URL, ensuring the script doesn't crash. It helps to gracefully handle exceptions that may occur during the process.

==> File Handling: The code opens a file named headlines.txt in write mode ('w') and iterates through the list of headlines, writing each one on a new line.
