
# Job Tracker Application

This is a Flask-based job tracking application. It allows users to add job applications, track their progress through different phases, view details of individual applications, and get aggregated statistics about their job search process.

## Features

- **Add Applications:** Easily add new job applications by providing the company name, position, salary, job description, recruiter name, and other details.
- **Track Phases:** Track job applications as they progress through different phases like `applied_for`, `called_back`, `first_interview`, `second_interview`, `test`, and `hired`.
- **View Applications:** View detailed information about individual applications, including salary, job description, recruiter information, and progress through phases.
- **Aggregation:** View aggregated statistics, such as the total number of jobs applied for, interviews attended, conversion rates, and phase distribution across your job applications.

## Prerequisites

Before running the application, ensure that you have the following installed on your machine:

- Python 3.8+
- pip (Python package manager)
- Docker (optional, if you want to run the application in a Docker container)

## Running the Application Locally

To run the application locally on your machine, follow these steps:

### Clone the Repository:

```bash
git clone https://github.com/your-username/job-tracker.git
cd job-tracker
```

### Set up a Virtual Environment:

```bash
python3 -m venv .venv
```

### Activate the Virtual Environment:

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Set up the Database:

The application uses SQLite for database management. The database will be automatically created when you run the application for the first time.

### Run the Application:

```bash
python app.py
```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Running the Application with Docker

To run the application using Docker:

### Build the Docker Image:

```bash
docker build -t job-tracker .
```

### Run the Docker Container:

```bash
docker run -p 5000:5000 job-tracker
```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

```
job-tracker/
│
├── app.py                 # Main application file with Flask routes and logic
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration for containerizing the app
├── README.md              # Project documentation
├── instance/              # SQLite database files are stored here
│   └── job_applications.db # SQLite database for job applications
├── static/                # Static files (CSS, JavaScript, images)
│   └── styles.css         # Main styles for the app
└── templates/             # HTML templates for the frontend
    ├── index.html         # Landing page showing all job applications
    ├── add_application.html  # Form to add a new job application
    ├── view_application.html # Detailed view of a single job application
    └── enhanced_results.html # Aggregated results and statistics
```

## I'd like to add a few features soon:

- **User Authentication:** Allow multiple users to track their job applications separately by implementing authentication and user sessions.
- **Edit/Delete Jobs:** Add functionality to edit or delete existing job applications.
- **Notifications:** Add a notification system that alerts users when a certain number of days have passed without a callback or when an important phase has been reached.
- **Data Visualization:** Use charting libraries like Plotly to visualize job application statistics and progress over time.
- **Search and Filter:** Implement search and filter functionality to help users easily find specific job applications by company, status, or other criteria.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
