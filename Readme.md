# YouTube Subscriber Count Tracker

This Python project tracks and visualizes the subscriber count of a YouTube channel in real-time using the YouTube Data API. The project fetches subscriber count data at regular intervals and displays it dynamically using Matplotlib.

## Prerequisites

Before you begin, ensure that you have the following:

- Python 3.x installed on your machine.
- A YouTube API key. You can obtain one from the [Google Cloud Console](https://console.cloud.google.com/).
- The following Python libraries installed:
  
  ```bash
  pip install google-api-python-client matplotlib

## Libraries Used
* googleapiclient.discovery: This module helps to interact with the YouTube Data API. We use it to fetch subscriber count data from a specified channel.

* matplotlib: A library used for plotting graphs. We use this to create a dynamic plot of the YouTube subscriber count over time.

* time: Used to introduce delays between API calls to prevent exceeding the API's rate limits.

## Setup
### Step 1: Obtain Your YouTube API Key: 
* To get a YouTube API key, follow these steps:

1. Go to Google Cloud Console.
2. Create a new project.
3. Enable the YouTube Data API v3.
4. Create API credentials and copy your API key.

### Step 2: Add the API Key to the Script
1. Replace 'YOUR_YOUTUBE_API_KEY' in the Python script with the API key you obtained from Google Cloud.


## Usage
* Clone or download this repository to your local machine.

* Open the terminal or command prompt and navigate to the project folder.

* Run the Python script.

* The script will start fetching subscriber count data for the given channel and update the plot in real-time every 60 seconds.

## How It Works
1. API Setup: The script initializes the YouTube API client using the provided API key.

2. Channel ID Retrieval: It tries to retrieve the YouTube channel ID using the forUsername parameter. If that fails, it falls back to the id parameter.

3. Data Fetching: The script fetches the subscriber count at regular intervals.

4. Visualization: The subscriber count is plotted dynamically using Matplotlib, updating every 60 seconds.