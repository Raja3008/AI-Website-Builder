# session_manager.py

import uuid

sessions = {}


def create_session(initial_input, website_type, questions):

    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        "website_type": website_type,
        "initial_input": initial_input,
        "questions": questions,
        "answers": {}
    }

    return session_id


def save_answer(session_id, field, answer):
    sessions[session_id]["answers"][field] = answer


def get_session(session_id):
    return sessions.get(session_id)
