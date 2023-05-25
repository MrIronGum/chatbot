# Website Summary Generator
The Website Summary Generator is a Streamlit app that generates a summary of a website by scraping its HTML content and using the Cohere API for text summarization. Here's how you can install and use the app:

# Installation:
1. Clone the repository: `git clone https://github.com/your_username/your_repository.git`
2. Navigate to the project directory: `cd your_repository`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`

# Configuration:
Before running the app, you need to configure it with your own API key:
1. Sign up for an account on the Cohere website (https://cohere.ai) if you haven't already.
2. Obtain your API key from the Cohere dashboard or API settings page.
3. Open the `inferential_bot.py` file in a text editor or IDE.
4. Locate the following line of code: `co = cohere.Client("YOUR_API_KEY")`
5. Replace `"YOUR_API_KEY"` with your actual API key.

# Usage:
1. Open the Streamlit app in your web browser.
2. Enter the URL of the website you want to generate a summary from in the provided text input.
3. Click on the "Generate" button.
The app will load the website content, extract the text, and generate a summary using the Cohere API.
The generated summary will be displayed below the button.
The code for the app is written in Python and utilizes the following libraries: Streamlit for creating the web interface and handling user input and display, Cohere for accessing the Cohere API for text summarization, requests for making HTTP requests to retrieve website content, BeautifulSoup (imported as BeautifulSoup4) for parsing the HTML and extracting text, and re for performing regular expression operations to clean up the text content.

Please note that you need to replace "YOUR_API_KEY" in the code with your actual Cohere API key in order to use the app effectively. Feel free to explore and modify the code according to your requirements.
