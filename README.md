# Website Summary Generator

This is a Streamlit app that generates a summary of a website based on its content. It utilizes web scraping techniques to parse the HTML of the website and extract the text. The extracted text is then used as a prompt for the Cohere API to generate a summary.

## Installation

To run this app locally, you need to follow these steps:

1. Clone this repository:

   ```shell
   git clone https://github.com/your_username/your_repository.git

2. Change to the project directory: 

   ```shell
   cd your_repository
   ```
   
3. Install the required dependencies:
   
   ```shell
   pip install -r requirements.txt
   ```
   
4. Run the app:
   
   ```shell
   streamlit run app.py
   ```

# Usage

Link to Cohere: 
https://cohere.com/

Copy and paste your API_KEY 

Open the Streamlit app in your web browser.

Enter the URL of the website you want to generate a summary from in the provided text input.

Click on the "Generate" button.

The app will load the website content, extract the text, and generate a summary using the Cohere API.

The generated summary will be displayed below the button.

# Code Explanation
The main code of this app is written in Python and uses the following libraries:

streamlit: Used to create the web interface and handle user input and display.
cohere: A Python client for the Cohere API, which is used to generate the summary.
requests: Used to make HTTP requests to retrieve the website content.
beautifulsoup4 (imported as BeautifulSoup): Used to parse the HTML content of the website and extract the text.
re: Used for regular expression operations to clean up the text content.
The app starts by setting up the Streamlit configuration, including the page title.

The parse_website function takes a URL as input and retrieves the HTML content of the website. It then uses BeautifulSoup to remove unwanted elements (like images) from the HTML and extract the text content. The text is cleaned by removing multiple whitespaces and newlines before being returned.

The app prompts the user to enter a website URL using the text_input function.

When the user clicks on the "Generate" button, the app calls the parse_website function to load the website content and extract the text. It then uses the Cohere client to generate a summary based on the extracted text. The generated summary is displayed using the write function from Streamlit.

Please note that you may need to replace the Cohere API key in the code with your own API key to use the app.

Feel free to explore and modify the code according to your needs!
