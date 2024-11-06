import gdown

# Google Drive folder ID
folder_id = "1wlsPIIIbsox-Sq8R-030vkYQhNbLI7JG"
# Your local output directory
output_dir = "D:\\Arun\\SSN\\sem-7\\cheat"

# Download the entire folder
gdown.download_folder(f"https://drive.google.com/drive/folders/{folder_id}", output_dir, quiet=False, use_cookies=False)
