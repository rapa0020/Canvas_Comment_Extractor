import tkinter as tk
from tkinter import ttk, messagebox
from canvasapi import Canvas
import csv
import time
import os
from datetime import datetime

# Function to fetch comments based on user input
def fetch_comments():
    API_URL = 'https://umn.instructure.com'  # Your Canvas URL
    API_KEY = api_key_entry.get()  # Get API key from entry
    COURSE_ID = course_id_entry.get()  # Get Course ID from entry

    # Validate Course ID is an integer
    try:
        COURSE_ID = int(COURSE_ID)
    except ValueError:
        messagebox.showerror("Invalid Input", "Course ID must be an integer.")
        return

    # Initialize a new Canvas object
    canvas = Canvas(API_URL, API_KEY)
    
    try:
        # Get a course object for this course
        course = canvas.get_course(COURSE_ID)

        # Get Students
        enrollments = course.get_enrollments()
        # Build a map of student ID to their name
        idToName = {e.user_id: e.user['name'] for e in enrollments}

        # Store comments in a list
        comments_data = []

        # For all comments in submissions of all assignments:
        for a in course.get_assignments():
            for s in a.get_submissions(include=['submission_comments']):
                for c in s.submission_comments:
                    studentName = idToName[s.user_id]
                    # Append assignment name, student name, and comment to the list
                    comments_data.append([a.name, studentName, c['comment']])

        # Call the function to save to CSV, passing the COURSE_ID
        save_comments_to_csv(comments_data, COURSE_ID)
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

#Function to save comments to CSV
def save_comments_to_csv(comments_data, COURSE_ID):
    # Get the current date (MMYY format)
    current_date = datetime.now().strftime('%m%y')

    # Create a unique filename using the COURSE_ID and current date
    filename = f'{COURSE_ID}_Comments_{current_date}.csv'
    
    # Check if file already exists (optional, to avoid further overwriting)
    if os.path.exists(filename):
        messagebox.showerror("Error", "A file with this name already exists.")
        return

    # Save the comments to the CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['Assignment Name', 'Student Name', 'Comment'])
        # Write all comments data
        csv_writer.writerows(comments_data)
    
    messagebox.showinfo("Success", f"Comments have been saved to {filename}.")

# Main function to run the application
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Canvas Comments Fetcher")
    
    # Set fixed window size (width x height)
    root.geometry('400x300')

    # Create a label and entry for API key
    tk.Label(root, text="API Key:").pack(pady=5)
    global api_key_entry  # Declare api_key_entry as global to access in fetch_comments
    api_key_entry = tk.Entry(root, width=50)
    api_key_entry.pack(pady=5)

    # Create a label and entry for Course ID
    tk.Label(root, text="Course ID:").pack(pady=5)
    global course_id_entry  # Declare course_id_entry as global to access in fetch_comments
    course_id_entry = tk.Entry(root, width=50)
    course_id_entry.pack(pady=5)

    # Create a ttk button to fetch comments
    fetch_button = ttk.Button(root, text="Fetch Comments", command=fetch_comments)
    fetch_button.pack(pady=20)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()