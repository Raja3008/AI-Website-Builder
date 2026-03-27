# terminal_chat.py

from question_engine import detect_website_type, get_questions_for_type, get_next_question
from session_manager import create_session, save_answer, get_session
from code_generator import generate_architecture, generate_full_code
from project_builder import save_blueprint, save_full_code
from project_validator import analyze_and_generate_execution_guide

def run_chat():

    print("🤖 AI Website Requirement Assistant")
    print("Type 'exit' anytime to stop.\n")

    user_input = input("You: ")

    if user_input.lower() == "exit":
        return

    website_type = detect_website_type(user_input)

    if not website_type:
        print("AI: Unsupported website type.")
        return

    questions = get_questions_for_type(website_type)

    session_id = create_session(user_input, website_type, questions)

    while True:

        session = get_session(session_id)

        next_q = get_next_question(session)

        if not next_q:
            break

        print("AI:", next_q["question"])
        answer = input("You: ")

        if answer.lower() == "exit":
            return

        save_answer(session_id, next_q["field"], answer)

    print("\n✅ Requirements collected successfully.")

    session_data = get_session(session_id)
    structured_data = {
        "website_type": session_data["website_type"],
        "initial_input": session_data["initial_input"],
        "requirements": session_data["answers"]
}

    print("Generating architecture...")
    architecture = generate_architecture(structured_data)

    blueprint_path = save_blueprint(architecture, session_id)

    print("Generating full project code...")
    full_code = generate_full_code(structured_data)

    code_path = save_full_code(full_code, session_id)
    
    print("Running AI validation and integration analysis...")
    execution_guide_path = analyze_and_generate_execution_guide(full_code, session_id)

    print("\n🎉 Project Generated Successfully!")
    print("Architecture saved at:", blueprint_path)
    print("Code saved at:", code_path)
    print("Execution Guide saved at:", execution_guide_path)

if __name__ == "__main__":
    run_chat()
