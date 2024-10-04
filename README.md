Instagram Content Downloader
Project Overview
Hello everyone! This project automates the process of downloading and saving videos from saved Instagram posts on your local machine. The script interacts with the Instagram interface via simulated mouse clicks and captures the screen, saving videos in a specified folder.

How It Works
Goal: To download all the saved content from your Instagram account and store them on your computer.
Setup: Open Instagram in your browser and position the window on the left half of your desktop. Place the Python code execution on the right half of the desktop.
Automation: The code utilizes the pyautogui library to simulate mouse clicks, capturing the screen for each video or image. It stores these captured files in a folder called videos.
Features
PyAutoGUI Integration: Simulates mouse clicks to interact with saved items on Instagram.
Video Recording: Uses OpenCV to capture and record each video or image found in your saved items for 20 seconds.
Dynamic Video Storage: Every recorded video or image is saved in the videos folder created by the script.
Important Note
The coordinates for mouse clicks depend on your screen resolution. Therefore, you will need to adjust the mouse positions in the code according to your screen setup.
Running the Project
Open Instagram on the left half of your screen.
Run the Python code on the right half of your screen.
The script will automatically start clicking saved items and record each for 20 seconds.
You will find the videos and images in the videos folder in your main directory.
Next Steps
This script saves all content, but duplicates may appear (for instance, a 20-second video of a static image). To clean up duplicates and optimize the captured content, another Python script (located in a separate repository)
will handle the video/image comparison to filter out unnecessary duplicates.
