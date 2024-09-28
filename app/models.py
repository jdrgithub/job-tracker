from app import db

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
    completed_phases = db.Column(db.String(500), nullable=True)

    def __init__(self, company_name, position, salary=None, job_description=None, recruiter_name=None,
                 hiring_manager_name=None, recruiting_company=None, notes=None):
        self.company_name = company_name
        self.position = position
        self.salary = salary
        self.job_description = job_description
        self.recruiter_name = recruiter_name
        self.hiring_manager_name = hiring_manager_name
        self.recruiting_company = recruiting_company
        self.notes = notes

    def advance_phase(self):
        phases = ['applied_for', 'called_back', 'first_interview', 'second_interview', 'test', 'hired']
        if self.current_phase in phases and self.current_phase != 'hired':
            self.completed_phases += f"{self.current_phase},"
            self.current_phase = phases[phases.index(self.current_phase) + 1]
        else:
            print("Cannot advance further.")
