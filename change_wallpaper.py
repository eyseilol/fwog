import os
import requests
import ctypes  # For setting wallpaper

# URL of the PNG image (replace with your direct image URL)
image_url = 'https://i.postimg.cc/k5NBsqDn/z9u7en1p0om51-1.png'  # Use a valid direct link to the PNG image

# Define the path where the image will be temporarily saved
image_path = os.path.join(os.path.expanduser("~"), "Downloads", "wallpaper.png")  # Change extension to .png

# Step 1: Download the image
try:
    response = requests.get(image_url)
    response.raise_for_status()  # Raise an error for bad responses
    with open(image_path, 'wb') as file:
        file.write(response.content)
    print("Image downloaded successfully.")
except Exception as e:
    print(f"Failed to download image: {e}")
    exit()

# Step 2: Set the downloaded image as wallpaper
try:
    # 0 for wallpaper, 2 for fill, 10 for stretch, etc.
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    print("Wallpaper set successfully.")
except Exception as e:
    print(f"Failed to set wallpaper: {e}")
