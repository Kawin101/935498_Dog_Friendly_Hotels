# import requests
# from bs4 import BeautifulSoup

# r = requests.get("https://travel.trueid.net/detail/rDvYykOdorNR")
# # override encoding by real educated guess as provided by chardet
# r.encoding = r.apparent_encoding
# # access the data
# r.text


# print(r.text.encode('utf-8'))


import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the URL
url = "https://travel.trueid.net/detail/rDvYykOdorNR"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information from the page by selecting HTML elements
    # Example: Get the title of the page
    title = soup.find('title').text

    # Encode the title as UTF-8 before printing
    title = title.encode('utf-8', 'ignore').decode('utf-8')
    
    # Example: Get a specific element by class name
    specific_element = soup.find('div', class_='your-class-name')

    if specific_element is not None:
        # Encode the specific_element as UTF-8 before printing (if needed)
        specific_element = specific_element.encode('utf-8', 'ignore').decode('utf-8')
        print("Specific Element:", specific_element)
    else:
        print("Specific element not found.")
    
    # Print the title
    print("Title:", title)

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
