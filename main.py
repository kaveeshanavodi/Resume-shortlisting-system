#Smart Resume Shortlisting System 

import os
import re
import csv
import nltk
import PyPDF2
import pytesseract

from pdf2image import convert_from_path
from PIL import Image
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


#SET TESSERACT PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


#NLP Setup
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))


#Important Skills
SKILLS = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "nlp",
    "pandas",
    "numpy",
    "scikit",
    "tensorflow",
    "deep learning",
    "excel",
    "power bi",
    "git"
]


# Text Cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9+ ]", " ", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


#Enhanced PDF Extraction (Text + OCR fallback)
def extract_text_from_pdf(file_path):

    text = ""

    # Try normal extraction first
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted
    except:
        pass

    # If empty → use OCR
    if len(text.strip()) == 0:
        print(f"OCR processing for: {file_path}")
        images = convert_from_path(file_path)

        for image in images:
            text += pytesseract.image_to_string(image)

    return text


#Skill Score
def calculate_skill_score(resume_text, skills):
    score = 0
    for skill in skills:
        if skill in resume_text:
            score += 1
    return score


#Experience Detection
def extract_experience_years(resume_text):
    pattern = r"(\d+)\+?\s*(years|year|yrs)"
    matches = re.findall(pattern, resume_text)
    years = [int(match[0]) for match in matches]
    return max(years) if years else 0


#Ranking Function
def rank_resumes(job_description, resumes, skills):

    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )[0]

    final_scores = []

    for i, resume_text in enumerate(resumes):

        skill_score = calculate_skill_score(resume_text, skills)
        skill_bonus = skill_score * 0.05

        experience_years = extract_experience_years(resume_text)
        experience_bonus = experience_years * 0.02

        final_score = similarity_scores[i] + skill_bonus + experience_bonus
        final_scores.append(final_score)

    return final_scores


#Export CSV
def export_to_csv(top_candidates):
    with open("output.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Resume Name", "Match Score"])
        for rank, (name, score) in enumerate(top_candidates, start=1):
            writer.writerow([rank, name, round(score, 3)])


# Main Function
def main():

    TOP_N = 5

    with open("job_description.txt", "r", encoding="utf-8") as file:
        job_description = clean_text(file.read())

    resume_texts = []
    resume_names = []

    for file_name in os.listdir("resumes"):

        if file_name.endswith(".pdf"):

            file_path = os.path.join("resumes", file_name)

            raw_text = extract_text_from_pdf(file_path)
            cleaned_text = clean_text(raw_text)

            print(f"\nProcessed: {file_name}")
            print("Text length:", len(cleaned_text))

            resume_texts.append(cleaned_text)
            resume_names.append(file_name)

    if not resume_texts:
        print("No resumes found.")
        return

    scores = rank_resumes(job_description, resume_texts, SKILLS)

    ranked_resumes = sorted(
        zip(resume_names, scores),
        key=lambda x: x[1],
        reverse=True
    )

    top_candidates = ranked_resumes[:TOP_N]

    print(f"\nTop {TOP_N} Shortlisted Candidates\n")

    for rank, (name, score) in enumerate(top_candidates, start=1):
        print(f"{rank}. {name} - Match Score: {round(score, 3)}")

    export_to_csv(top_candidates)
    print("\nResults exported to output.csv")


if __name__ == "__main__":
    main()
