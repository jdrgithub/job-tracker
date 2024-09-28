from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import JobApplication

# Landing page to show all job applications
@app.route('/')
def index():
    job_applications = JobApplication.query.all()
    return render_template('index.html', job_applications=job_applications)

# Page to add new job applications
@app.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        status = request.form['status']
        new_application = JobApplication(company_name=company, position=position, current_phase=status)
        db.session.add(new_application)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_application.html')

# Page to view the details of a specific job application
@app.route('/view/<int:job_id>')
def view_application(job_id):
    job = JobApplication.query.get_or_404(job_id)
    return render_template('view_application.html', job=job)

# Enhanced results aggregation
@app.route('/enhanced_results')
def enhanced_results():
    total_jobs = JobApplication.query.count()
    total_interviews = JobApplication.query.filter(JobApplication.current_phase.in_(['first_interview', 'second_interview'])).count()
    total_hired = JobApplication.query.filter_by(current_phase='hired').count()

    phase_counts = {
        phase: JobApplication.query.filter_by(current_phase=phase).count()
        for phase in JobApplication.PHASES
    }

    conversion_to_interview = (total_interviews / total_jobs) * 100 if total_jobs > 0 else 0
    conversion_to_hire = (total_hired / total_jobs) * 100 if total_jobs > 0 else 0

    return render_template('enhanced_results.html', total_jobs=total_jobs, total_interviews=total_interviews, total_hired=total_hired, phase_counts=phase_counts, conversion_to_interview=conversion_to_interview, conversion_to_hire=conversion_to_hire)
