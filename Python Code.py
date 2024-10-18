import datetime
import time
import os 

source_folder = 'folder1'          # YOUR_ROOT_FOLDER
destination_folder = 'folder2'     # THE_STORE_FOLDER

def is_time_between(start_time, end_time):
    # Get the current time
    current_time = datetime.datetime.now().time()
    # Check if current time is between start_time and end_time
    if start_time < end_time:
        return start_time <= current_time <= end_time
    else:
        return start_time <= current_time or current_time <= end_time

start_time = datetime.time(16, 50)  # Start time for moving files
end_time = datetime.time(16, 51)    # End time for moving files

while True:
    if is_time_between(start_time, end_time):
        # Move files from source_folder to destination_folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            os.rename(source_path, destination_path)
        print(f"All files moved from {source_folder} to {destination_folder}")
    else:
        # Move files back from destination_folder to source_folder
        for filename in os.listdir(destination_folder):
            source_path = os.path.join(destination_folder, filename)
            destination_path = os.path.join(source_folder, filename)
            os.rename(destination_path, source_path)
        print(f"All files moved back from {destination_folder} to {source_folder}")
        break

    print("Waiting for the next check...")
    time.sleep(60)  # Wait for 60 seconds before checking again


