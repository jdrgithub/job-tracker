
# Job Tracker Application

This is a Flask-based job tracking application. It allows users to add job applications, track their progress through different phases, view details of individual applications, and get aggregated statistics about their job search process.

## Features

- **Add Applications**: Easily add new job applications by providing the company name, position, and status.
- **Track Phases**: Track job applications as they progress through different phases like `applied_for`, `called_back`, `first_interview`, `second_interview`, `test`, and `hired`.
- **View Applications**: View details of individual applications and their current phase.
- **Aggregation**: View aggregated statistics such as the total number of jobs applied for, interviews attended, and conversion rates.

## Prerequisites

Before you can run the application, make sure you have the following installed on your machine:

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** (optional, if you want to run the application in a Docker container)

## Running the Application Locally

To run the application locally on your machine, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/job-tracker.git
   cd job-tracker
   ```

2. Set up a virtual environment:

   ```
   python3 -m venv .venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:

     ```
     source .venv/bin/activate
     ```

   - On Windows:

     ```
     .venv\Scripts\activate
     ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Set up the database:

   The application uses SQLite for database management. The database will be automatically created when you run the application for the first time.

6. Run the application:

   ```
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Running the Application with Docker

To run the application using Docker:

1. Build the Docker image:

   ```
   docker build -t job-tracker .
   ```

2. Run the Docker container:

   ```
   docker run -p 5000:5000 job-tracker
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Project Structure

```
job-tracker/
│
├── app.py               # Main application file with Flask routes and logic
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration for containerizing the app
├── README.md            # This file
└── templates/           # HTML templates for the frontend
    ├── index.html       # Landing page showing all job applications
    ├── add_application.html # Form to add a new job application
    ├── view_application.html # Detailed view of a single job application
    └── enhanced_results.html # Aggregated results and statistics
```

## Future Enhancements

- **User Authentication**: Allow multiple users to track their job applications separately by implementing authentication and user sessions.
- **Edit/Delete Jobs**: Add functionality to edit or delete existing job applications.
- **Notifications**: Add a notification system that alerts users when a certain number of days have passed without a callback or when an important phase has been reached.
- **Data Visualization**: Use charting libraries like Plotly or Chart.js to visualize job application statistics and progress over time.
- **Search and Filter**: Implement search and filter functionality to help users easily find specific job applications by company, status, or other criteria.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
