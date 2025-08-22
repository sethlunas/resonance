# Dependencies – Project Resonance

This file documents the packages explicitly used in `requirements.txt`.  
(Does not list Flask’s transitive dependencies.)

---

## Web Framework
- **Flask==3.1.1**  
  Lightweight Python web framework. Powers the backend server, routing (`@app.route`), and request handling.

## Document Parsing
- **pypdf ~= 6.0**  
  Library for working with PDF files (extracting text, metadata, splitting/merging).  
  Used for parsing resumes in `.pdf` format.

- **python-docx ~= 1.2**  
  Library for creating and parsing Microsoft Word `.docx` files.  
  Used for parsing resumes in Word format.

---

## Notes
- Only packages pinned in `requirements.txt` are tracked here.  
- Update this file alongside `requirements.txt` whenever a new dependency is added.
