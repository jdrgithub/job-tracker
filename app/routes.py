from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import logging
import os

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Get the current working directory
current_directory = os.getcwd()
print(f"CURRENT DIRECTORY: {current_directory}")

# Instantiate Flask
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate SQLAlchemy
db = SQLAlchemy(app)

# Define the JobApplication model to include all form fields
class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    salary = db.Column(db.Float, nullable=True)
    job_description = db.Column(db.Text, nullable=True)
    recruiter_name = db.Column(db.String(120), nullable=True)
    hiring_manager_name = db.Column(db.String(120), nullable=True)
    recruiting_company = db.Column(db.String(120), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    callback = db.Column(db.String(10), default="No")
    first_interview = db.Column(db.String(10), default="No")
    current_phase = db.Column(db.String(120), default='applied_for')
    completed_phases = db.Column(db.String(500), default='')  # Store as CSV

    # Method to advance the job to the next phase
    def advance_phase(self):
        phases = ['applied_for', 'called_back', 'first_interview', 'second_interview', 'test', 'hired']
        if self.current_phase in phases and self.current_phase != 'hired':
            self.completed_phases += f"{self.current_phase},"
            self.current_phase = phases[phases.index(self.current_phase) + 1]
        else:
            print("Cannot advance further.")

# Function to check if the database file exists and create the tables if not
def initialize_database():
    try:
        # Determine the database file location using pathlib
        db_path = Path(__file__).parent / 'job_applications.db'

        # Check if the database file exists
        if not db_path.exists():
            logging.info("Database not found, creating...")

            # Ensure database tables are created within an application context
            with app.app_context():
                db.create_all()  # Create the database and tables

            logging.info("Database and tables created successfully.")
        else:
            logging.info("Database exists, no need to create.")
    except Exception as e:
        logging.error(f"Error initializing database: {e}")

# Call the initialize_database function
initialize_database()

# Define the index route to show job applications
@app.route('/')
def index():
    job_applications = JobApplication.query.all()
    return render_template('index.html', job_applications=job_applications)

# Define the route to add a new job application
@app.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        # Safely retrieve form data to avoid BadRequestKeyError
        company = request.form.get('company_name')
        position = request.form.get('position')
        salary = request.form.get('salary')
        job_description = request.form.get('job_description')
        recruiter_name = request.form.get('recruiter_name')
        hiring_manager_name = request.form.get('hiring_manager_name')
        recruiting_company = request.form.get('recruiting_company')
        notes = request.form.get('notes')
        callback = request.form.get('callback', 'No')
        first_interview = request.form.get('first_interview', 'No')
        status = request.form.get('current_phase', 'applied_for')  # Default to 'applied_for' if not provided

        # Validate the required fields
        if not company or not position:
            flash("Company name and position are required.", "danger")
            return redirect(url_for('add_application'))

        # Add the new application to the database
        new_application = JobApplication(
            company_name=company,
            position=position,
            salary=salary,
            job_description=job_description,
            recruiter_name=recruiter_name,
            hiring_manager_name=hiring_manager_name,
            recruiting_company=recruiting_company,
            notes=notes,
            callback=callback,
            first_interview=first_interview,
            current_phase=status
        )
        db.session.add(new_application)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_application.html')

# Define the route to view the details of a specific job application
@app.route('/view/<int:job_id>')
def view_application(job_id):
    job = JobApplication.query.get_or_404(job_id)
    return render_template('view_application.html', job=job)

# Define the route for the enhanced results aggregation page
@app.route('/enhanced_results')
def enhanced_results():
    total_jobs = JobApplication.query.count()
    total_interviews = JobApplication.query.filter(JobApplication.current_phase.in_(['first_interview', 'second_interview'])).count()
    total_hired = JobApplication.query.filter_by(current_phase='hired').count()

    # Calculate phase distribution
    phase_counts = {
        'applied_for': JobApplication.query.filter_by(current_phase='applied_for').count(),
        'called_back': JobApplication.query.filter_by(current_phase='called_back').count(),
        'first_interview': JobApplication.query.filter_by(current_phase='first_interview').count(),
        'second_interview': JobApplication.query.filter_by(current_phase='second_interview').count(),
        'test': JobApplication.query.filter_by(current_phase='test').count(),
        'hired': JobApplication.query.filter_by(current_phase='hired').count(),
    }

    # Conversion rates
    conversion_to_interview = (total_interviews / total_jobs) * 100 if total_jobs > 0 else 0
    conversion_to_hire = (total_hired / total_jobs) * 100 if total_jobs > 0 else 0

    return render_template(
        'enhanced_results.html',
        total_jobs=total_jobs,
        total_interviews=total_interviews,
        total_hired=total_hired,
        phase_counts=phase_counts,
        conversion_to_interview=conversion_to_interview,
        conversion_to_hire=conversion_to_hire
    )

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
