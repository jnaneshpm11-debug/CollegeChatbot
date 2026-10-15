from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form["question"].lower()

        if "hello" in question or "hi" in question:
            answer = "Hello! Welcome to our college chatbot."
        elif "timing" in question or "time" in question:
            answer = "Our college timings are 9 AM to 4 PM. Please confirm with the college office."
        elif "principal" in question:
            answer = "Please contact the college office for the principal's details."
        elif "course" in question:
            answer = "Please contact the college office for available courses."
        elif "admission" in question:
            answer = "Please contact the college office for admission details."
        elif "fee" in question:
            answer = "Please contact the college office for fee details."
        else:
            answer = "Sorry, I don't know that yet. Please ask another question."

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=False)
