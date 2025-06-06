import pandas as pd
import os
import requests
from urllib.parse import urlparse

# Load CSV
df = pd.read_csv('watches.csv')  # Replace with your actual file name

# Create output directory
output_dir = 'downloaded_images'
os.makedirs(output_dir, exist_ok=True)

# Download images
for idx, row in df.iterrows():
    url = row['images_links']
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        ext = os.path.splitext(urlparse(url).path)[1]
        filename = f"{output_dir}/image_{idx}{ext}"
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download image at index {idx}: {e}")
