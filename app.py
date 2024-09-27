from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Instantiate Flask
app = Flask(__name__)

# Configure the SQLAlchemy database URI (replace 'db' with the name of your database container)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate SQLAlchemy
db = SQLAlchemy(app)

# Define the JobApplication model
class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)

# Ensure database tables are created in an application context
with app.app_context():
    db.create_all()

# Define routes
@app.route('/')
def index():
    job_applications = JobApplication.query.all()
    return render_template('index.html', job_applications=job_applications)

@app.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        status = request.form['status']

        # Add the new application to the database
        new_application = JobApplication(company_name=company, position=position, status=status)
        db.session.add(new_application)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_application.html')

if __name__ == '__main__':
    app.run(debug=True)
