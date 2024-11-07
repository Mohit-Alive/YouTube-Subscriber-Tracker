import time
import matplotlib.pyplot as plt
from googleapiclient.discovery import build

# API Configuration
API_KEY = 'YOUR-API-KEY'
CHANNEL_ID = 'YOUR-CHANNEL-ID'  # Replace with the channel's ID

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)


# Function to get subscriber count
def get_subscriber_count():
    request = youtube.channels().list(part='statistics', id=CHANNEL_ID)
    response = request.execute()
    return int(response['items'][0]['statistics']['subscriberCount'])

# Data storage
timestamps = []
subscriber_counts = []

# Data collection loop
try:
    while True:
        current_time = time.strftime("%H:%M:%S")
        sub_count = get_subscriber_count()
        
        # Append to data lists
        timestamps.append(current_time)
        subscriber_counts.append(sub_count)
        
        print(f"{current_time} - Subscribers: {sub_count}")
        
        # Plot the data
        plt.clf()
        plt.plot(timestamps, subscriber_counts, label='Subscribers', color='b', marker='o')
        plt.xlabel('Time')
        plt.ylabel('Subscriber Count')
        plt.title('YouTube Subscriber Count Over Time')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(60)  # Update every 60 seconds
except KeyboardInterrupt:
    print("Tracking stopped.")

plt.show()
