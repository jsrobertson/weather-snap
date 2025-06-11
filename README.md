# Weather Snap - A Python Weather script for Raspberry Pi

This Python mini-project fetches the current temperature for a specified city, renders it into an HTML template, and takes a screenshot of the rendered page using a headless Chrome browser.

This could then be used to display weather information on an e-ink display or similar device connected to a Raspberry Pi.

## Features

- Fetches live weather data from [OpenWeatherMap](https://openweathermap.org/).
- Renders the temperature into a customizable HTML template (Jinja).
- Uses Selenium and headless Chrome to generate a screenshot of the HTML page.
- Environment variables for City and OpenWeather API key.

## Requirements

- Python 3.7+
- [Chromium](https://www.chromium.org/) browser
- [Chromium Chromedriver](https://chromedriver.chromium.org/) (ensure it matches your Chromium version)
- The Python packages listed in `requirements.txt`

## Installation (Raspberry Pi)

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/jsrobertson/weather-snap.git
    cd weather-snap
    ```

2.  **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

    Copy `.env.example` to `.env` and add your OpenWeatherMap API key:

    ```
    cp .env.example .env
    ```

    Edit `.env` and set your City and OpenWeather API Key:

    ```env
    CITY=City
    OPENWEATHER_API_KEY=your_OPENWEATHER_API_KEY_here
    ```

4.  **Install Chromium and Chromedriver:**

    ```sh
    sudo apt update
    sudo apt install -y chromium-browser chromium-chromedriver
    ```

> On some Raspberry Pi OS versions, the packages may be named `chromium` and `chromium-driver`.

6.  **Check the paths:**

- Chromium binary is usually at `/usr/bin/chromium-browser` or `/usr/bin/chromium`
- Chromedriver is usually at `/usr/lib/chromium-browser/chromedriver` or `/usr/bin/chromedriver`

  Update `weather.py` if necessary to match these paths.

## Usage

Run the script:

```sh
python weather.py
```

The script will fetch the weather, render `templates/index.jinja` with the temperature, and save a screenshot as `output/screenshot.png`.

## To Do

- [ ] Add support for more weather data (humidity, wind speed, etc.).
- [ ] Create a nicer HTML template with styling.
- [ ] Who knows?
