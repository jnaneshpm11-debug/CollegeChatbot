from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form["question"].lower()

        if "hello" in question or "hi" in question:
            answer = "Hello! Welcome to our college chatbot."

        elif "course" in question or "branch" in question:
            answer = (
                "We can provide information about courses such as "
                "Computer Science Engineering (CSE), "
                "Artificial Intelligence and Machine Learning (AI & ML), "
                "Information Science (ISE), and Electronics and "
                "Communication Engineering (ECE). "
                "Please confirm the actual courses offered by your college."
            )

        elif "admission" in question:
            answer = "Please contact the college admission office for details."

        elif "fee" in question:
            answer = "Please contact the college office for accurate fee details."

        elif "timing" in question:
            answer = "Please check your college timetable for working hours."

        else:
            answer = "Sorry, I don't know that yet. Please ask about courses, admissions, fees, or timings."

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=False)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=False)
