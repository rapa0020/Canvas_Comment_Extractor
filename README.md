# Comment_DL
A simple GUI application to fetch comments from Canvas and save them to a CSV file.

Features
	•	Fetch comments from Canvas for a specified course.
	•	Save comments to a CSV file with a timestamped filename.
	•	User-friendly GUI.

Requirements
	•	Python 3.x
	•	canvasapi library

Installation Instructions
To install the Canvas Comments Downloader, follow these steps:
	1	Download the ZIP file containing the application code from here.
	2	Extract the ZIP file to a desired location on your computer.
	3	Run the Executable:
			On Windows: Double-click the .exe file in the extracted folder.
			On macOS/Linux: Open a terminal, navigate to the directory, and run:
			./canvas_comments

Note: You may have to give your computer permission to run the program.

Running the Program
To run the Canvas Comments Downloader, follow these steps:
	1	Open a terminal window.
	2	Navigate to the program's directory: cd /path/to/MathCEP Comments Downloader
	3	Run the script: python canvas_comments.py
	4	Or run the executable in the /dist folder: canvas_comments 
Usage
	1	Enter your API Key and Course ID into the respective fields.
	2	Click the Fetch Comments button to start downloading comments.
	3	The comments will be saved in a CSV file named [COURSE_ID] Comments - [MMYY].csv to you user directory (the username under which you are logged in).
