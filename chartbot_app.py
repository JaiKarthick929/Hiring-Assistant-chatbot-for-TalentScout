import streamlit as st
import re # Using regex for basic email validation

# --- Simulation Functions (Replace with actual LLM calls in a real deployment) ---

def get_simulated_greeting():
    """Returns the initial greeting message."""
    return """
    Hello! I'm the TalentScout Hiring Assistant. I'm here to help with the initial screening process.
    I'll ask a few questions about your background, experience, and technical skills.
    You can type 'bye' or 'exit' anytime to end our conversation.
    Let's get started! What is your full name?
    """

def generate_simulated_technical_questions(tech_stack_list):
    """
    Simulates generating technical questions based on a list of technologies.
    In a real scenario, this would involve prompting an LLM.
    """
    questions = []
    if not tech_stack_list:
        return "It seems no technologies were listed. Let's move on for now."

    for tech in tech_stack_list:
        tech = tech.strip()
        # Basic simulation - replace with actual LLM-generated questions
        if "python" in tech.lower():
            questions.append(f"- Can you explain the difference between a list and a tuple in Python?")
            questions.append(f"- What are Python decorators and how are they used?")
            questions.append(f"- Describe the Global Interpreter Lock (GIL) in CPython.")
        elif "django" in tech.lower():
            questions.append(f"- What is the Django ORM and how does it work?")
            questions.append(f"- Explain the request/response cycle in Django.")
            questions.append(f"- How do you handle user authentication in Django?")
        elif "react" in tech.lower():
            questions.append(f"- What is the Virtual DOM in React?")
            questions.append(f"- Explain the concept of props vs. state in React.")
            questions.append(f"- What are React Hooks?")
        elif "aws" in tech.lower():
            questions.append(f"- What is the difference between EC2 and Lambda in AWS?")
            questions.append(f"- Explain the concept of an S3 bucket.")
            questions.append(f"- What is an AWS VPC?")
        elif "sql" in tech.lower() or "database" in tech.lower():
             questions.append(f"- What is the difference between an INNER JOIN and a LEFT JOIN?")
             questions.append(f"- Explain database normalization (e.g., 3NF).")
             questions.append(f"- What is an index in a database and why is it useful?")
        else:
            # Generic question for unrecognised tech
            questions.append(f"- Can you describe a challenging project where you used {tech}?")
            questions.append(f"- What are the core concepts of {tech}?")
            questions.append(f"- How would you rate your proficiency in {tech} on a scale of 1-5?")

    # Limit to max 3-5 questions *per technology listed* - this simulation is simpler
    # A real implementation would need more sophisticated logic or LLM prompting.
    # For this simulation, we'll just show a few generated ones.
    formatted_questions = "\n".join(questions[:5]) # Show up to 5 simulated questions total for brevity
    if formatted_questions:
      return f"Okay, based on your tech stack, here are a few technical questions:\n{formatted_questions}\n\nPlease take your time to answer. (In a real screening, your answers would be recorded)."
    else:
      return "I couldn't generate specific questions for the technologies listed. Can you tell me about a project you're proud of using your skills?"


def get_simulated_fallback():
    """Returns a fallback message for misunderstood input."""
    return "I'm sorry, I didn't quite understand that. Could you please rephrase or provide the information I asked for?"

def get_simulated_closing_message(name):
    """Returns the closing message."""
    user_name = name if name else "candidate"
    return f"Thank you for your time, {user_name}! We have your initial information. A TalentScout recruiter will review your details and be in touch regarding the next steps if your profile matches our current openings. Have a great day!"

# --- Streamlit App Logic ---

st.title(" TalentScout Hiring Assistant")
st.write("Welcome! Please interact with the chatbot below.")

# Initialize session state variables if they don't exist
if 'stage' not in st.session_state:
    st.session_state.stage = 'GREETING'
    st.session_state.messages = []
    st.session_state.candidate_info = {
        "Full Name": None,
        "Email Address": None,
        "Phone Number": None,
        "Years of Experience": None,
        "Desired Position(s)": None,
        "Current Location": None,
        "Tech Stack": None,
    }
    # Add initial greeting message from the assistant
    st.session_state.messages.append({"role": "assistant", "content": get_simulated_greeting()})


# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Your response..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Basic exit condition
    if prompt.lower() in ["bye", "exit", "quit"]:
        st.session_state.stage = "CLOSING"
        response = get_simulated_closing_message(st.session_state.candidate_info.get("Full Name"))
    else:
        current_stage = st.session_state.stage
        response = get_simulated_fallback() # Default response

        # --- Conversation Flow Logic ---
        try:
            if current_stage == 'GREETING':
                # User provided name in response to greeting
                st.session_state.candidate_info["Full Name"] = prompt
                st.session_state.stage = 'ASK_EMAIL'
                response = f"Nice to meet you, {prompt}! What is your email address?"

            elif current_stage == 'ASK_EMAIL':
                 # Basic email format check (not exhaustive)
                if re.match(r"[^@]+@[^@]+\.[^@]+", prompt):
                    st.session_state.candidate_info["Email Address"] = prompt
                    st.session_state.stage = 'ASK_PHONE'
                    response = "Got it. What is your phone number?"
                else:
                    response = "That doesn't look like a valid email address. Could you please provide a valid email?"
                    # Keep stage as ASK_EMAIL to re-ask

            elif current_stage == 'ASK_PHONE':
                # Basic check if it contains numbers (can be improved)
                if any(char.isdigit() for char in prompt):
                    st.session_state.candidate_info["Phone Number"] = prompt
                    st.session_state.stage = 'ASK_EXPERIENCE'
                    response = "Thanks. How many years of professional experience do you have?"
                else:
                    response = "Please enter a valid phone number."
                     # Keep stage as ASK_PHONE

            elif current_stage == 'ASK_EXPERIENCE':
                # Basic check if it's numeric (can be improved)
                try:
                    # Check if input can represent a number (int or float)
                    float(prompt)
                    st.session_state.candidate_info["Years of Experience"] = prompt
                    st.session_state.stage = 'ASK_POSITION'
                    response = "Understood. What position(s) are you interested in?"
                except ValueError:
                     response = "Please enter the number of years of experience (e.g., '5' or '2.5')."
                     # Keep stage as ASK_EXPERIENCE


            elif current_stage == 'ASK_POSITION':
                st.session_state.candidate_info["Desired Position(s)"] = prompt
                st.session_state.stage = 'ASK_LOCATION'
                response = "Okay. And what is your current location (City, Country)?"

            elif current_stage == 'ASK_LOCATION':
                st.session_state.candidate_info["Current Location"] = prompt
                st.session_state.stage = 'ASK_TECH_STACK'
                response = ("Great. Now, please list your primary technical skills. "
                            "Include programming languages, frameworks, databases, and tools you are proficient in "
                            "(e.g., Python, Django, React, PostgreSQL, AWS, Docker). Please separate them with commas.")

            elif current_stage == 'ASK_TECH_STACK':
                st.session_state.candidate_info["Tech Stack"] = prompt
                # Simple parsing - split by comma
                tech_stack_list = [tech.strip() for tech in prompt.split(',') if tech.strip()]
                st.session_state.stage = 'ASK_QUESTIONS'
                # Generate simulated questions based on the list
                response = generate_simulated_technical_questions(tech_stack_list)
                # If questions were generated, transition to waiting for answers (or closing)
                # For this simulation, we immediately transition to closing after showing questions.
                # In a real scenario, you might add a stage to collect answers.
                st.session_state.stage = "CLOSING_AFTER_QUESTIONS"


            elif current_stage == 'ASK_QUESTIONS':
                 # In this simulated version, we don't collect answers to the tech questions.
                 # We just showed them and now proceed to closing.
                 st.session_state.stage = "CLOSING"
                 response = get_simulated_closing_message(st.session_state.candidate_info.get("Full Name"))

            elif current_stage == "CLOSING_AFTER_QUESTIONS":
                 # User might respond something after seeing the questions, just proceed to close.
                 st.session_state.stage = "CLOSING"
                 response = get_simulated_closing_message(st.session_state.candidate_info.get("Full Name"))


            elif current_stage == 'CLOSING':
                # Conversation is already ending
                response = "The conversation has concluded. Thank you!"
                st.session_state.stage = 'DONE' # Prevent further processing

            elif current_stage == 'DONE':
                 response = "The session has ended. Please refresh to start over."


        except Exception as e:
            st.error(f"An error occurred: {e}") # Show error in UI
            response = get_simulated_fallback() # Fallback on error


    # Add assistant response to chat history and display it
    if st.session_state.stage != 'DONE': # Don't add more messages if done
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
