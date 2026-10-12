from flask import Flask, render_template, request

app = Flask(__name__)

# Available subjects and their topics
subjects = {
    "Python": [
        "Introduction to Python",
        "Variables and Data Types",
        "Conditional Statements",
        "Loops",
        "Functions",
        "Lists and Tuples",
        "Dictionaries and Sets",
        "Object-Oriented Programming",
        "File Handling",
        "Exception Handling"
    ],

    "Java": [
        "Introduction to Java",
        "Data Types and Variables",
        "Operators",
        "Conditional Statements",
        "Loops",
        "Classes and Objects",
        "Inheritance",
        "Polymorphism",
        "Exception Handling",
        "Collections Framework"
    ],

    "DBMS": [
        "Introduction to DBMS",
        "ER Model",
        "Relational Model",
        "SQL Queries",
        "Functional Dependencies",
        "Normalization",
        "Transactions",
        "Concurrency Control",
        "Serializability",
        "Database Recovery"
    ],

    "DSA": [
        "Arrays",
        "Strings",
        "Linked Lists",
        "Stacks",
        "Queues",
        "Searching",
        "Sorting",
        "Recursion",
        "Trees",
        "Graphs"
    ],

    "Computer Networks": [
        "Introduction to Networks",
        "Network Topologies",
        "OSI Model",
        "TCP/IP Model",
        "IP Addressing",
        "Routing",
        "Transport Layer",
        "Application Layer",
        "Network Security",
        "Network Protocols"
    ],

    "Operating Systems": [
        "Introduction to Operating Systems",
        "Process Management",
        "Threads",
        "CPU Scheduling",
        "Process Synchronization",
        "Deadlocks",
        "Memory Management",
        "Virtual Memory",
        "File Systems",
        "Disk Scheduling"
    ]
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    name = request.form.get("name", "").strip()
    days_text = request.form.get("days", "")
    subject = request.form.get("subject", "")
    hours_text = request.form.get("hours", "")
    start_time = request.form.get("start_time", "")

    # Validate input
    if not name or not days_text or not subject or not hours_text or not start_time:
        return "Please fill in all fields.", 400

    try:
        days = int(days_text)
        hours = float(hours_text)
    except ValueError:
        return "Enter valid numbers for days and study hours.", 400

    if days < 1 or days > 30:
        return "Choose between 1 and 30 study days.", 400

    if hours < 1 or hours > 12:
        return "Choose between 1 and 12 study hours per day.", 400

    if subject not in subjects:
        return "Please select a valid subject.", 400

    topics = subjects[subject]
    timetable = []

    # Spread the topics across the selected days.
    topic_count = len(topics)
    start_minutes = int(start_time[:2]) * 60 + int(start_time[3:])

    # Reserve part of each day for revision.
    study_minutes = int(hours * 60)
    revision_minutes = min(30, study_minutes // 4)
    learning_minutes = study_minutes - revision_minutes

    for day in range(1, days + 1):
        sessions = []
        day_start = start_minutes

        if day == days:
            # Final day: revise the complete subject.
            session_length = max(1, study_minutes // 4)
            sessions.append({
                "time": "Final revision",
                "topic": "Revise all topics: " + ", ".join(topics),
                "duration": study_minutes
            })

        else:
            # Assign a portion of the syllabus to this day.
            first_topic = (day - 1) * topic_count // days
            last_topic = day * topic_count // days
            daily_topics = topics[first_topic:last_topic]

            if not daily_topics:
                daily_topics = [topics[(day - 1) % topic_count]]

            minutes_per_topic = max(
                15, learning_minutes // len(daily_topics)
            )

            for index, topic in enumerate(daily_topics):
                start = day_start
                end = start + minutes_per_topic

                sessions.append({
                    "time": (
                        f"{start // 60:02d}:{start % 60:02d} - "
                        f"{end // 60:02d}:{end % 60:02d}"
                    ),
                    "topic": topic,
                    "duration": minutes_per_topic
                })

                day_start = end + 10  # 10-minute break

            sessions.append({
                "time": "Last session",
                "topic": "Revise today's topics",
                "duration": revision_minutes
            })

        timetable.append({
            "day": day,
            "sessions": sessions
        })

    return render_template(
        "result.html",
        name=name,
        subject=subject,
        days=days,
        hours=hours,
        timetable=timetable
    )


if __name__ == "__main__":
    app.run(debug=True)