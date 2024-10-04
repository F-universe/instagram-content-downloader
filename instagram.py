import pyautogui
import cv2
import numpy as np
import time
import os

# Function to get the next progressive video number
def get_next_video_number(videos_folder):
    existing_videos = [f for f in os.listdir(videos_folder) if f.startswith('video') and f.endswith('.avi')]
    if not existing_videos:
        return 1
    else:
        # Find the highest number in existing files
        existing_numbers = [int(f.replace('video', '').replace('.avi', '')) for f in existing_videos]
        return max(existing_numbers) + 1

# Function to perform a click and then start recording
def click_and_record(x, y, duration, output_path):
    # Click at the specified position
    pyautogui.moveTo(x, y)
    pyautogui.click()

    # Screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Create the video writer to save the video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (screen_width, screen_height))

    # Start recording immediately after the click
    start_time = time.time()

    while True:
        # Capture a screenshot of the entire screen
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Save the frame to the video
        out.write(frame)

        # Stop recording after the specified duration
        if time.time() - start_time > duration:
            break

    # Release the video writer
    out.release()

# Main function to perform the sequence of clicks and recordings
def perform_sequence(base_x, base_y, duration, videos_folder):
    video_number = get_next_video_number(videos_folder)

    # Perform the first click and record the first video
    output_video_path1 = os.path.join(videos_folder, f'video{video_number}.avi')
    click_and_record(base_x, base_y, duration, output_video_path1)
    print(f"Video {video_number} successfully recorded in {output_video_path1}")
    video_number += 1

    # Click at coordinates (524, 201)
    x2, y2 = 524, 201
    pyautogui.moveTo(x2, y2)
    pyautogui.click()

    # Click at coordinates (522, 392) and record the second video
    output_video_path2 = os.path.join(videos_folder, f'video{video_number}.avi')
    click_and_record(522, 392, duration, output_video_path2)
    print(f"Video {video_number} successfully recorded in {output_video_path2}")
    video_number += 1

    # Click again at coordinates (524, 201)
    pyautogui.moveTo(x2, y2)
    pyautogui.click()

    # Click at coordinates (822, 392) and record the third video
    output_video_path3 = os.path.join(videos_folder, f'video{video_number}.avi')
    click_and_record(822, 392, duration, output_video_path3)
    print(f"Video {video_number} successfully recorded in {output_video_path3}")

    # After the third video, click at (524, 201)
    pyautogui.moveTo(x2, y2)
    pyautogui.click()

    # Move back to coordinates (522, 392) without clicking
    pyautogui.moveTo(522, 392)

    # Scroll the page 290px down (without moving the mouse)
    pyautogui.scroll(-55)

# Main directory
main_folder = r"C:\Users\fabio\OneDrive\Desktop\instagram(1)"
# Create a subfolder 'videos' to save the videos
videos_folder = os.path.join(main_folder, 'videos')

# Create the videos folder if it doesn't exist
if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)

# Coordinates for the first click and video duration
base_x, base_y = 230, 400
video_duration = 20  # Duration of each video in seconds

# Infinite loop to repeat the sequence
while True:
    perform_sequence(base_x, base_y, video_duration, videos_folder)
