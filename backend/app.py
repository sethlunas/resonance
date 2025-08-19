from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with file upload form
UPLOAD_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Resonance - Resume Analyzer</title>
</head>
<body>
    <h1>Resonance</h1>
    <h2>Upload Your Resume</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="resume" accept=".pdf,.doc,.docx" required>
        <br><br>
        <button type="submit">Upload Resume</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return UPLOAD_FORM

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return "No file uploaded!"
    file = request.files['resume']
    if file.filename == '':
        return "No file selected!"
    
    # For now, we just show file info
    file_check = f"""
    <h2>File uploaded successfully!</h2>
    <p>Filename: {file.filename}</p>
    <p>Size: {len(file.read())} bytes</p>
    """
    return file_check

if __name__ == '__main__':
    app.run(debug=True, port=5000)