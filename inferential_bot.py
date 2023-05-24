import streamlit as st
import cohere
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="Generator", page_icon=":tada:", layout="wide")

# Set up Streamlit app
st.title("Generator")

# Initialize the cohere client
co = cohere.Client("hX3l9Xe2kEOrvaCFgdzIeUI20C5lr4GiYq0pTEiY")

# Website parser
def parse_website(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove image elements from the HTML
    for img in soup.find_all("img"):
        img.extract()

    # Extract text content from the remaining HTML
    text_content = soup.get_text(separator=" ")

    # Remove multiple whitespaces and newlines
    text_content = re.sub(r"\s+", " ", text_content)

    return text_content.strip()

# Website input
website_url = st.text_input("Enter the website URL:")

# Generate summary and poem
if st.button("Generate") and website_url:
    # Load the website and extract the summary
    website_content = parse_website(website_url)

    # Generate poem using cohere client
    response = co.generate(
        model="command-nightly",
        prompt=website_content,
        max_tokens=200,
        temperature=0.75
    )
    intro_paragraph = response.generations[0].text

    # Display the generated poem
    st.write(intro_paragraph)
