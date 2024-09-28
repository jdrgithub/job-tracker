from app import db

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    current_phase = db.Column(db.String(120), default='applied_for')
    completed_phases = db.Column(db.String(500), default='')  # Store as CSV

    def advance_phase(self):
        phases = ['applied_for', 'called_back', 'first_interview', 'second_interview', 'test', 'hired']
        if self.current_phase in phases and self.current_phase != 'hired':
            self.completed_phases += f"{self.current_phase},"
            self.current_phase = phases[phases.index(self.current_phase) + 1]
        else:
            print("Cannot advance further.")
