from fastapi import FastAPI
from session_manager import create_session, add_message, get_history
from gemini_engine import generate_next_question, extract_structured_requirements
from code_generator import generate_architecture, generate_full_code
from project_builder import save_blueprint, save_full_code
import schemas

app = FastAPI(title="AI Website Generator")


@app.get("/")
def home():
    return {"message": "AI Website Generator Running"}


# STEP 1 — Start Requirement Flow
@app.post("/start")
def start_flow(request: schemas.InitialRequest):

    session_id = create_session(request.user_input)

    history = get_history(session_id)

    question = generate_next_question(history)

    add_message(session_id, "assistant", question)

    return {
        "session_id": session_id,
        "question": question
    }


# STEP 1 — Continue Questions
@app.post("/next")
def next_question(request: schemas.ChatInput):

    add_message(request.session_id, "user", request.message)

    history = get_history(request.session_id)

    question = generate_next_question(history)

    if question.strip() == "REQUIREMENTS_COMPLETE":

        structured_json = extract_structured_requirements(history)

        architecture = generate_architecture(structured_json)
        blueprint_path = save_blueprint(architecture, request.session_id)

        full_code = generate_full_code(structured_json)
        code_path = save_full_code(full_code, request.session_id)

        return {
            "status": "completed",
            "blueprint_path": blueprint_path,
            "code_path": code_path
        }

    add_message(request.session_id, "assistant", question)

    return {
        "status": "in_progress",
        "question": question
    }