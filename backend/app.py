from flask import Flask, request

app = Flask(__name__)

# Minimal HTML template with file upload form
UPLOAD_FORM = """
<!DOCTYPE html>

<html>
<head>
    <title>Resonance - Resume Analyzer</title>
    <!-- '!DOCTYPE html' declares HTML5 so the browser uses standards mode -->
</head>
<body>
    <h1>Resonance</h1>
    <h2>Upload Your Resume</h2>

    <!-- 'form' defines a form the user can submit -->
    <!-- action="/upload" → sends the form data to our Flask '/upload' route -->
    <!-- method="post" → use HTTP POST (sends data to server, unlike GET) -->
    <!-- enctype="multipart/form-data" → required for sending files -->

    <form action="/upload" method="post" enctype="multipart/form-data">

        <!-- File picker -->
        <!-- type="file" gives the user a "choose file" button -->
        <!-- name="resume" → the key Flask looks for inside request.files -->
        <!-- accept=".pdf,.doc,.docx" restricts allowed file types -->
        <!-- required → browser won’t let you submit with no file -->
        <input type="file" name="resume" accept=".pdf,.docx" required>

        <br><br>

        <!-- Submit button -->
        <!-- When clicked, the browser packages the form data and sends it to /upload -->
        <button type="submit">Upload Resume</button>
    </form>
</body>
</html>
"""

# Flask route decorator that maps root path to function home()
@app.route('/')
def home():
    return UPLOAD_FORM


# This route handles file uploads via HTTP POST requests.
# The decorator tells Flask:
# - When a request comes in at '/upload'
# - AND the method is POST
# -> Run the function defined below
@app.route('/upload', methods=['POST'])
def upload_file():
    # 'request' is a Flask object representing the incoming HTTP request.
    # 'request.files' holds uploaded files, keyed by the <input name="..."> in the form.
    if 'resume' not in request.files:
        return "No file uploaded!"
    
    file = request.files['resume']
    if file.filename == '':
        return "No file selected!"
    
    # For now: just return file info (name + size in bytes)
    file_check = f"""
    <h2>File uploaded successfully!</h2>
    <p>Filename: {file.filename}</p>
    <p>Size: {len(file.read())} bytes</p>
    """
    file.seek(0) # reset file pointer back to start so file can be read again later
    return file_check

# so that the file will only run when it is called from the terminal not when imported
if __name__ == '__main__':
    app.run(debug=True, port=5000)