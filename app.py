from flask import Flask, render_template, request

app = Flask(__name__)


def get_answer(question):
    q = question.lower().strip()

    if q in ["hi", "hello", "hey"]:
        return "Hello! Welcome to our College Chatbot!"

    elif "course" in question or "courses" in question:
    answer = (
        "KVG College of Engineering, Sullia offers these "
        "undergraduate engineering branches:\n"
        "1. Computer Science and Engineering (CSE)\n"
        "2. Computer Science and Engineering (AI & ML)\n"
        "3. Computer Engineering\n"
        "4. Electronics and Communication Engineering (ECE)\n"
        "5. Civil Engineering\n"
        "6. Mechanical Engineering\n\n"
        "Please contact the college office to confirm "
        "the currently available courses."

    elif any(word in q for word in ["admission", "eligibility"]):
        return "For admission details, please contact the college admission office."

    elif "fee" in question or "fees" in question:
            answer = (
                "KVG College of Engineering, Sullia - Admission Fees\n\n"
                "The fees depend on the course and admission category.\n"
                "For the exact current fee structure, please contact "
                "the college admission office.\n"
                "Ask the office about tuition fees, admission fees, "
                "and other applicable charges."
            )

        elif "admission" in question:
            answer = (
                "Welcome to KVG College of Engineering, Sullia!\n"
                "For admission details, eligibility, required "
                "documents, and the admission process, please "
                "contact the college admission office."
            )

    elif any(word in q for word in ["timing", "timings", "hours"]):
        return "Please contact the college office to confirm college timings."

    elif any(word in q for word in ["location", "address"]):
        return "Please enter your college address to display the correct location."

    elif any(word in q for word in ["contact", "phone", "email"]):
        return "Please contact the college office for official contact details."

    elif "thank" in q:
        return "You're welcome! Ask me another question."
    elif "hod" in question or "head of department" in question:
            answer = (
                "HOD Name: Ravishankar Bhat. He is the Head of the Department of Computer Science and Engineering. "
            )

        elif "class teacher" in question or "class tutor" in question:
            answer = (
                "Class Teacher Name: Mrs.Premalatha.b. She is the class teacher for the Computer Science and Engineering department."    

    else:
        return (
            "I can help with courses, admissions, fees, timings, "
            "location, and contact details. Please try asking about these topics."
        )


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "")
        answer = get_answer(question)

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=False)


if __name__ == "__main__":
    app.run(debug=False)
