import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uploads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    filename = db.Column(db.String())
    data = db.Column(db.LargeBinary)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        picture = request.files['file']
        filename = picture.filename
        file_data = picture.read()
        
        new_file = Upload(description=description, filename=filename, data=file_data)
        db.session.add(new_file)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html')

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
    
#     # Save form data to database or file
#     return render_template('success.html')

if __name__ == '__main__':
    
    app.run(debug=True)