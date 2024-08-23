from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Instantiate Flask
app = Flask(__name__)

# Configure the SQLAlchemy database URI (replace 'db' with the name of your database container)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@db/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate SQLAlchemy
db = SQLAlchemy(app)

# In-memory storage for job applications (you might want to use a database later)
job_applications = []

@app.route('/')
def index():
    return render_template('index.html', job_applications=job_applications)

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)

@app.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        status = request.form['status']

        # Add the new application to the list
        job_applications.append({
            'company': company,
            'position': position,
            'status': status
        })

        return redirect(url_for('index'))

    return render_template('add_application.html')

if __name__ == '__main__':
    app.run(debug=True)




