import re
from collections import Counter

def clean_text(text):
    """Converts text to lowercase and removes punctuation."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
    return text

def get_keywords(text, stop_words=None):
    """Extracts unique words from text, optionally filtering stop words."""
    words = clean_text(text).split()
    if stop_words:
        words = [word for word in words if word not in stop_words]
    return set(words) # Use set for unique keywords

def score_resume(resume_text, job_keywords):
    """Calculates a relevance score based on job keywords found in the resume."""
    resume_words = clean_text(resume_text).split()
    score = 0
    matched_keywords = Counter()
    for keyword in job_keywords:
        # Count how many times each job keyword appears in the resume
        count = resume_words.count(keyword)
        score += count
        if count > 0:
            matched_keywords[keyword] = count
    return score, matched_keywords

def highlight_keywords(text, keywords_to_highlight):
    """Highlights specified keywords in the text with asterisks."""
    highlighted_text = text
    for keyword in keywords_to_highlight:
        # Use regex to find whole words and replace them, case-insensitively
        highlighted_text = re.sub(r'\b' + re.escape(keyword) + r'\b', f'***{keyword}***', highlighted_text, flags=re.IGNORECASE)
    return highlighted_text

# --- Main part of the script ---

# Example Job Description (simulates the job posting content)
job_description = """
We are looking for a highly motivated Software Engineer with strong Python skills.
The ideal candidate will have experience with web development, REST APIs, and database management (SQL).
Familiarity with cloud platforms (AWS, Azure) and Agile methodologies is a plus.
Excellent problem-solving and communication skills are essential.
Join our dynamic team to build innovative solutions.
"""

# Example Resume Text (simulates your resume content)
resume_text = """
Experienced Developer seeking challenging roles.
Proficient in Python, Java, and C++.
Skilled in web development using Flask and Django.
Developed and maintained RESTful APIs.
Strong background in SQL database design and optimization.
Familiar with Agile development practices.
Excellent problem-solving abilities and team player.
"""

# Define some common stop words to filter out less meaningful words
# This helps focus on more specific technical or role-related keywords.
stop_words = {
    "a", "an", "the", "is", "are", "and", "or", "with", "for", "of", "to", "in", "our", "we", "be", "have", "will",
    "this", "that", "it", "its", "from", "on", "at", "by", "as", "but", "not", "he", "she", "they", "i", "you", "me",
    "us", "him", "her", "them", "my", "your", "his", "her", "their", "mine", "yours", "hers", "theirs", "what", "where",
    "when", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "just", "don", "should", "now",
    "looking", "candidate", "skills", "experience", "solutions", "abilities", "practices", "design", "optimization",
    "using", "seeking", "roles", "background", "player", "team", "dynamic", "join", "build", "ideal", "highly",
    "motivated", "strong", "excellent", "essential", "plus", "familiarity", "proficient", "skilled", "developed",
    "maintained", "familiar", "developer", "engineer", "software", "management", "problem", "solving", "communication",
    "innovative", "challenging", "roles", "proficient", "skilled", "developed", "maintained", "strong", "background",
    "abilities", "player", "team", "dynamic", "join", "build", "innovative", "solutions", "ideal", "highly", "motivated",
    "excellent", "essential", "plus", "familiarity", "practices", "seeking", "roles", "flask", "django", "java", "c++"
}

print("--- Job Description ---")
print(job_description)

print("\n--- Your Resume ---")
print(resume_text)

# Extract keywords from the job description
# This simulates identifying key requirements from the job posting.
job_keywords = get_keywords(job_description, stop_words)
print("\n--- Extracted Job Keywords ---")
print(sorted(list(job_keywords)))

# Score the resume against the extracted keywords
# This demonstrates how well the resume aligns with the job's requirements.
relevance_score, matched_keywords_count = score_resume(resume_text, job_keywords)
print(f"\n--- Resume Relevance Score: {relevance_score} ---")
print("Matched keywords and their counts in resume:", dict(matched_keywords_count))

# Highlight matched keywords in the resume for visual inspection
# This helps visualize which parts of the resume are most relevant.
highlighted_resume = highlight_keywords(resume_text, matched_keywords_count.keys())
print("\n--- Your Resume (Keywords Highlighted) ---")
print(highlighted_resume)

print("\n--- How to Improve ---")
print("To increase your score, ensure your resume explicitly mentions more of the 'Extracted Job Keywords'.")
print("For example, if 'AWS' is a keyword and not in your resume, consider adding it if applicable.")
