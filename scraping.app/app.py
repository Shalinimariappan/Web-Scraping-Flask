from flask import Flask, request, render_template, redirect, url_for, send_file
import os
import pandas as pd
from scraper import run_scraper
from email_service import send_email

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULTS_FILE = 'static/student_results.xlsx'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ✅ Create Uploads Folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            try:
                run_scraper(file_path, RESULTS_FILE)
                return redirect(url_for('results'))
            except Exception as e:
                return render_template('index.html', error=f"Failed to process: {e}")
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if os.path.exists(RESULTS_FILE):
        df = pd.read_excel(RESULTS_FILE)
        results = df.to_dict(orient='records')

        if request.method == 'POST':
            receiver_email = request.form['email']
            try:
                send_email(receiver_email, RESULTS_FILE)
                return render_template('results.html', results=results, success="Email sent successfully!")
            except Exception as e:
                return render_template('results.html', results=results, error=f"Failed to send email: {e}")

        return render_template('results.html', results=results)

    return redirect(url_for('upload_file'))

@app.route('/download')
def download():
    return send_file(RESULTS_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
