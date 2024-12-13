import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://www.google.com/search?q=weather+forecast+nairobi&rlz=1C1JJTC_enKE1093KE1093&oq=weather+&gs_lcrp=EgZjaHJvbWUqCggCEAAYkgMYgAQyBggAEEUYOTINCAEQABixAxjJAxiABDIKCAIQABiSAxiABDINCAMQABiSAxiABBiKBTIKCAQQABixAxiABDIKCAUQABixAxiABDIKCAYQABixAxiABDIHCAcQABiABDIKCAgQABixAxiABDINCAkQABiDARixAxiABNIBCTE2MDYzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'

# Make a GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all HTML elements on the page
    all_elements = soup.find_all()

    # Print the text content of all elements (you can modify this part based on your needs)
    for element in all_elements:
        print(element.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

