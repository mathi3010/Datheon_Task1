# Datheon Internship Task 1
## Structured LLM Prompt Pipeline & JSON Extractor

### Project Overview
This project extracts structured information from resume text using Google's Gemini API and validates the extracted data using Pydantic.

### Features
- Reads resume text from a file.
- Uses Gemini to extract resume information.
- Validates extracted data using Pydantic.
- Extracts name, job title, skills, and years of experience.
- Saves the result as a JSON file.

### Technologies Used
- Python
- Google Gemini API
- Google GenAI SDK
- Pydantic
- JSON
- python-dotenv

### Project Structure
```text
Datheon_Task1/
├── main.py
├── prompts.py
├── schemas.py
├── resume.txt
├── output.json
├── test_connection.py
├── .env
├── .gitignore
└── README.md
```

### Setup Instructions

1. Install Python 3.13.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment on Windows:

```powershell
venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install google-genai pydantic python-dotenv
```

5. Create a `.env` file and configure your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

### Run the Project

```bash
python main.py
```

### Output

The extracted resume data is saved in `output.json`.

Example:

```json
{
  "name": "Shanmathi S",
  "job_title": "Machine Vision Engineer",
  "skills": ["Python", "OpenCV", "YOLO", "FastAPI", "SQL"],
  "experience_years": 1.5
}
```

### Testing

Run the Gemini API connection test:

```bash
python test_connection.py
```

### Conclusion
This project demonstrates structured information extraction from resume text using an LLM, schema validation, and JSON output generation.
