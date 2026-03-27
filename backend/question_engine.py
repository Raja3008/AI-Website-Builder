# question_engine.py

from question_dataset import WEBSITE_QUESTION_DATASET


def detect_website_type(user_input):
    user_input = user_input.lower()

    keywords = {
        "ecommerce": ["ecommerce", "shop", "store", "marketplace"],
        "portfolio": ["portfolio"],
        "blog": ["blog"],
        "saas": ["saas"],
        "corporate": ["corporate", "company", "business"],
        "social_media": ["social", "community"],
        "real_estate": ["real estate", "property"],
        "job_portal": ["job", "career"]
    }

    for website_type, words in keywords.items():
        for word in words:
            if word in user_input:
                return website_type

    return None


def get_questions_for_type(website_type):
    return WEBSITE_QUESTION_DATASET.get(website_type, [])


def get_next_question(session_data):
    questions = session_data["questions"]
    answers = session_data["answers"]

    for q in questions:
        if q["field"] not in answers:
            return q

    return None