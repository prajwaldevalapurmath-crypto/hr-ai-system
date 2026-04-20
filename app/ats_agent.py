def calculate_score(resume: str, jd: str) -> int:
    resume = resume.lower()
    jd = jd.lower()

    resume_words = set(resume.split())
    jd_words = set(jd.split())

    matched = resume_words.intersection(jd_words)

    if len(jd_words) == 0:
        return 0

    return int((len(matched) / len(jd_words)) * 100)