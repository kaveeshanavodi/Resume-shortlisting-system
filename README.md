\# Smart Resume Shortlisting System (OCR Enabled)



This project is an automated resume screening system built using Python and basic NLP techniques. The system ranks resumes based on how well they match a given job description.

I built this project to practice Natural Language Processing (NLP), text similarity, and real-world document processing.





\## Project Overview



The system reads multiple resumes in PDF format and compares them with a job description. It calculates a similarity score and ranks candidates from highest to lowest.

The system also supports scanned or Canva-based resumes using OCR (Optical Character Recognition).







\## Features



\- Extracts text from PDF resumes

\- Supports scanned/image-based resumes using OCR

\- Cleans and preprocesses text using NLP techniques

\- Uses TF-IDF vectorization

\- Calculates cosine similarity between resumes and job description

\- Boosts scores based on important skill matches

\- Boosts scores based on detected years of experience

\- Shortlists Top-N candidates

\- Exports ranked results to a CSV file







\## Technologies Used



\- Python

\- NLTK

\- Scikit-learn

\- PyPDF2

\- pytesseract (OCR)

\- pdf2image

\- Regular Expressions (Regex)







\## How the System Works



1\. The program reads the job description from `job\_description.txt`.

2\. It extracts text from all PDF resumes inside the `resumes` folder.

3\. If a resume is scanned, it uses OCR to convert the image to text.

4\. It cleans and preprocesses the text (lowercase conversion, removing stopwords, removing special characters).

5\. It converts the text into TF-IDF vectors.

6\. It calculates cosine similarity between each resume and the job description.

7\. It adds bonus points for skill matches.

8\. It adds bonus points based on years of experience detected.

9\. It ranks candidates and selects the top results.

10\. It exports the final ranking to `output.csv`.







\## Installation



1\. Install Python (version 3.9 or higher recommended).



2\. Install required Python libraries:

pip install nltk scikit-learn PyPDF2 pytesseract pdf2image pillow



3\. Install Tesseract OCR:

https://github.com/UB-Mannheim/tesseract/wiki



4\. Install Poppler for Windows:

https://github.com/oschwartz10612/poppler-windows/releases/



5\. Make sure Tesseract and Poppler are added to your system PATH or specified inside the code.







\## How to Run



1\. Place your resume PDF files inside the `resumes` folder.

2\. Edit the `job\_description.txt` file with your desired job description.

3\. Run the program:

4\. View ranked results in the terminal.

5\. Open `output.csv` to see the shortlisted candidates.







\## What I Learned



\- Basic Natural Language Processing

\- Text cleaning and preprocessing

\- TF-IDF vectorization

\- Cosine similarity scoring

\- OCR integration for scanned documents

\- Handling real-world PDF processing challenges

\- Using Git and GitHub for version control







\## Resume Description



Developed an OCR-enabled resume screening system using Python and NLP techniques to rank candidates based on job description matching using TF-IDF and cosine similarity.



