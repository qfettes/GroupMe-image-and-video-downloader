# Groupme Video/Image Downloader
## Author: Quintin Fettes
This tools can be used in combination with searchme.co to automatically download all images, gifs, and videos from
groups on the GroupMe app

Requirements: 
* Python 

Usage:
1. Go to [searchme.co](https://searchme.co)
2. Log in
3. Select the group you're interested in
4. Wait for all messages to finish loading
5. Click the "Filter Messages" tab
6. Optional: Select a start date and end data
7. Select "Attachments". In the dropdown list select "Images" AND "Videos"
8. Scroll to the bottom of the page: Click "Download Group Transcript"
9. Select "Download Filtered Messages" in the dialog box
10. Click "Download"
11. Run the command: python extract.py --data /path/to/downloaded/data.txt --destination /folder/to/dump/downloaded/attachments/
Note: the defaults are --data ./data/data.txt --destination ./dump