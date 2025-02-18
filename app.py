from flask import Flask, render_template, request, redirect, url_for, flash
from models import calculate_cgpa

app = Flask(__name__)
app.secret_key = "hello"

# List of subjects and their respective credits
SUBJECTS = [
    {"name": "Computational Thinking", "credits": 4, "category": "Foundation"},
    {"name": "English I", "credits": 4, "category": "Foundation"},
    {"name": "Mathematics for Data Science I", "credits": 4, "category": "Foundation"},
    {"name": "Statistics for Data Science I", "credits": 4, "category": "Foundation"},
    {"name": "Programming in Python", "credits": 4, "category": "Foundation"},
    {"name": "English II", "credits": 4, "category": "Foundation"},
    {"name": "Mathematics for Data Science II", "credits": 4, "category": "Foundation"},
    {"name": "Statistics for Data Science II", "credits": 4, "category": "Foundation"},
    {"name": "Database Management Systems", "credits": 4, "category": "Diploma in Prog"},
    {"name": "Mordern Application Development - I", "credits": 4, "category": "Diploma in Prog"},
    {"name": "Mordern Application Development - II", "credits": 4, "category": "Diploma in Prog"},
    {"name": "System Commands", "credits": 3, "category": "Diploma in Prog"},
    {"name": "Programming Concepts using Java", "credits": 4, "category": "Diploma in Prog"},
    {"name": "Programming, Data Structures and Algorithms using Python", "credits": 4, "category": "Diploma in Prog"},
    {"name": "Mordern Application Development - I [PROJECT]", "credits": 2, "category": "Diploma in Prog"},
    {"name": "Mordern Application Development - II [PROJECT]", "credits": 2, "category": "Diploma in Prog"},
    {"name": "Machine Learning Foundations", "credits": 4, "category": "Diploma in Data"},
    {"name": "Business Data Management", "credits": 4, "category": "Diploma in Data"},
    {"name": "Machine Learning Techniques", "credits": 4, "category": "Diploma in Data"},
    {"name": "Machine Learning Practice", "credits": 4, "category": "Diploma in Data"},
    {"name": "Business Analytics", "credits": 4, "category": "Diploma in Data"},
    {"name": "Tools in Data Science", "credits": 3, "category": "Diploma in Data"},
    {"name": "Business Data Management [PROJECT]", "credits": 2, "category": "Diploma in Data"},
    {"name": "Machine Learning Practice [PROJECT]", "credits": 2, "category": "Diploma in Data"},
    
]

@app.route("/")
def home():
    result = request.args.get("result", None)
    return render_template("index.html", subjects=SUBJECTS, result=result)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        # Fetch selected subjects and grades from the form
        selected_subjects = request.form.getlist("subject")
        grades = request.form.getlist("grade")

        if not selected_subjects:
            flash("Please select at least one subject.", "error")
            return redirect(url_for("home"))

        # Filter grades corresponding to selected subjects
        filtered_grades = [grades[i] for i, subject in enumerate(SUBJECTS) if subject["name"] in selected_subjects]
        print(filtered_grades)

        # Ensure all selected subjects have valid grades
        if len(filtered_grades) != len(selected_subjects) or "" in filtered_grades:
            flash("Please assign a valid grade for each selected subject.", "error")
            return redirect(url_for("home"))

        # Collect credits for selected subjects
        credits = [subject["credits"] for subject in SUBJECTS if subject["name"] in selected_subjects]

        # Calculate CGPA
        result = calculate_cgpa(filtered_grades, credits)
        return redirect(url_for("home", result = result))
    except Exception as e:
        flash(f"Error: {e}", "error")
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
