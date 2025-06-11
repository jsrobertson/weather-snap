import os
import requests
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import tempfile

# Load environment variables from .env file
load_dotenv()

# Configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Sheffield")
OUTPUT_DIR = "output"
SCREENSHOT_FILE = os.path.join(OUTPUT_DIR, "screenshot.png")


def get_weather():
    """Fetch weather data from OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    print(f"Fetching weather data for {CITY}.")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    """Main function to fetch weather data, render HTML, and take a screenshot."""

    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY is not set in the environment variables.")
        return

    # Set up Jinja2 environment and load template
    env = Environment(loader=FileSystemLoader("templates"))
    index_template = env.get_template("index.jinja")

    # Chrome options for headless operation
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=800,600")
    chrome_options.binary_location = "/usr/bin/chromium"

    # Use a temporary user data directory for Chrome
    with tempfile.TemporaryDirectory() as user_data_dir:
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            weather_data = get_weather()

            if weather_data:
                temp = weather_data["main"]["temp"]
                output_from_template = index_template.render(temp=temp)

                # Write HTML output
                if not os.path.exists("output"):
                    os.makedirs(OUTPUT_DIR)
                html_path = os.path.join(user_data_dir, "index.html")
                with open(html_path, "w") as file:
                    file.write(output_from_template)
                    print(f"HTML file generated at {html_path}.")

                # Open HTML file and take screenshot
                driver.get("file://" + html_path)
                driver.save_screenshot(SCREENSHOT_FILE)
                print(f"Screenshot saved to '{SCREENSHOT_FILE}'.")
        finally:
            driver.quit()
            print("Temporary user data directory cleaned up.")


if __name__ == "__main__":
    main()
