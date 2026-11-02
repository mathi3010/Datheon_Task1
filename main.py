
import os
from dotenv import load_dotenv
from google import genai
import json
from schemas import ResumeData
from prompts import RESUME_PROMPT
import time
# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key missing in .env")

# Initialize Gemini
client = genai.Client(api_key=api_key)



def extract_resume_data(resume_text):

    prompt = RESUME_PROMPT.format(
        resume_text=resume_text
    )

    print("Connecting to Gemini...", flush=True)

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": ResumeData.model_json_schema()
        }
    )

    print("Gemini response received!", flush=True)

    result = ResumeData.model_validate_json(
        interaction.output_text
    )

    return result.model_dump()


# if __name__ == "__main__":

#     print("Starting Gemini Resume Extractor...", flush=True)

#     resume_text = """
#     Shanmathi is a Machine Vision Engineer.
#     She has 1.5 years of experience.
#     Skills: Python, OpenCV, YOLO.
#     """

#     print("Sending request to Gemini...", flush=True)

#     result = extract_resume_data(resume_text)

#     if result:
#         with open("output.json", "w", encoding="utf-8") as file:
#             json.dump(result, file, indent=4)

#         print("JSON saved successfully!")
#         print(result)



def read_resume_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        resume_text = file.read()

    return resume_text


if __name__ == "__main__":

    print("Starting Resume Extractor...", flush=True)

    resume_text = read_resume_file("resume.txt")

    print("Resume file loaded successfully!", flush=True)

    for attempt in range(3):

        try:
            result = extract_resume_data(resume_text)

            with open("output.json", "w", encoding="utf-8") as file:
                json.dump(result, file, indent=4)

            print("\nResume extraction completed!")
            print("JSON saved successfully!")
            print(result)

            break

        except Exception as error:

            print(f"Attempt {attempt + 1} failed: {error}")

            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)

            else:
                print("All attempts failed.")