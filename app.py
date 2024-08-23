from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for job applications (you might want to use a database later)
job_applications = []

@app.route('/')
def index():
    return render_template('index.html', job_applications=job_applications)

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




