from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    personal_info_status = db.Column(db.String(50))
    education_status = db.Column(db.String(50))
    experience_status = db.Column(db.String(50))
    skills_status = db.Column(db.String(50))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    mobile_number = request.form['mobile_number']
    email = request.form['email']
    password = request.form['password']
    new_user = User(first_name=first_name, last_name=last_name, mobile_number=mobile_number, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    flash("Registration successful!", "success")
    return redirect(url_for('index'))

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    file = request.files['resume']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Assuming user is logged in and their user_id is stored in session
        user_id = 1  # Replace with the actual user ID from the session

        new_resume = Resume(user_id=user_id, filename=filename, personal_info_status="Complete", education_status="Complete", experience_status="Incomplete", skills_status="Complete")
        db.session.add(new_resume)
        db.session.commit()

        flash('Resume uploaded successfully!', 'success')
        return redirect(url_for('view_result', filename=filename))
    else:
        flash('File not allowed', 'error')
        return redirect(request.url)

@app.route('/view_result/<filename>')
def view_result(filename):
    resume = Resume.query.filter_by(filename=filename).first()
    if resume:
        result = {
            "Personal Information": resume.personal_info_status,
            "Education": resume.education_status,
            "Experience": resume.experience_status,
            "Skills": resume.skills_status
        }
        return render_template('view_result.html', filename=filename, result=result)
    else:
        flash('Resume not found', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
