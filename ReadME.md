# Remote Work Cafes Website

This is a simple web application built with **Flask**, **Jinja**, and **Bootstrap**.
The application allows users to view a list of cafes suitable for remote work in a particular area, displayed on an interactive map. Only the admin has permission to add or remove cafes from the list.

## Features
- **Homepage**: Displays a list of cafes with name, description, and location.
- **Google Maps Integration**: An interactive map showing the location of each cafe.
- **Admin Panel**: Only admins can add, remove, or update cafe details.
- **Responsive Design**: The website uses **Bootstrap** to ensure the site is mobile-friendly and looks great on all devices.

## Installation

### Requirements
- Python 3.x
- Flask
- Jinja
- Bootstrap (for frontend styling)

### Step 1: Clone the Repository
Clone this repository to your local machine (Git Bash):

- git clone https://github.com/yourusername/remote-work-cafes.git
- cd remote-work-cafes

# Step 2: Set Up a Virtual Environment (Optional but Recommended)

- python3 -m venv venv
- source venv/bin/activate  # For Linux/macOS
- venv\Scripts\activate     # For Windows

# Step 3: Install Dependencies
- pip install -r requirements.txt

# Step 4: Set Up the Database
This application uses SQLite as the database. 
If you need to set up the database, run the following command:

python3 app.py


# Step 5: Run the Application
Run the Flask development server:
- python app.py
- Access the application in your browser at: http://127.0.0.1:5000

# Usage
Viewing Cafes: Visitors can see the list of cafes on the homepage, along with their details and locations on the interactive map.

Admin Functions: Admin users can log in and add or remove cafes. Only authenticated admins have access to these features.

Admin Authentication
Admin credentials can be set in the application code. For simplicity, authentication is basic, but you can easily integrate a more secure authentication method using Flask-Login or other libraries.

# File Structure
/remote-work-cafes
    /static
        /css
        /js
    /templates
        base.html
        index.html
        admin_login.html
    /instances
        cafe.db
    main.py
    requirements.txt

- /static: Contains CSS and JavaScript files.

- /templates: Contains HTML templates using Jinja.

- /instances: Contains DB info for each Cafe and admin.

- main.py: Main application file.

- requirements.txt: Python dependencies.

**Contribution:**
Feel free to fork the repository and submit pull requests if you have any improvements or bug fixes.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.