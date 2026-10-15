from flask import Flask, render_template, request

app = Flask(__name__)


def get_answer(question):
    q = question.lower().strip()

    if q in ["hi", "hello", "hey"]:
        return "Hello! Welcome to our College Chatbot!"

    elif any(word in q for word in ["course", "courses", "branch"]):
        return "Please contact the college office for the official list of courses."

    elif any(word in q for word in ["admission", "eligibility"]):
        return "For admission details, please contact the college admission office."

    elif any(word in q for word in ["fee", "fees", "payment"]):
        return "Please contact the college office for accurate fee details."

    elif any(word in q for word in ["timing", "timings", "hours"]):
        return "Please contact the college office to confirm college timings."

    elif any(word in q for word in ["location", "address"]):
        return "Please enter your college address to display the correct location."

    elif any(word in q for word in ["contact", "phone", "email"]):
        return "Please contact the college office for official contact details."

    elif "thank" in q:
        return "You're welcome! Ask me another question."

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
