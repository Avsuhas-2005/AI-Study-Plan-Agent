from datetime import datetime, timedelta

# ============================================================
# AI STUDY PLAN AGENT
# ============================================================

# ------------------------------------------------------------
# 1. SUBJECTS AND TOPICS
# ------------------------------------------------------------

subjects = {

    "DBMS": [
        "Introduction to DBMS",
        "Database Architecture",
        "Data Models",
        "ER Model and ER Diagrams",
        "Relational Model",
        "SQL Commands",
        "SQL Constraints",
        "Aggregate Functions",
        "Functional Dependencies",
        "Inference Rules",
        "Normalization - 1NF",
        "Normalization - 2NF",
        "Normalization - 3NF",
        "BCNF",
        "Transactions",
        "Concurrency Control"
    ],

    "JAVA": [
        "Introduction to Java",
        "Data Types and Variables",
        "Operators and Control Statements",
        "Classes and Objects",
        "Constructors",
        "Inheritance",
        "Polymorphism",
        "Abstraction",
        "Interfaces",
        "Exception Handling",
        "Strings",
        "Arrays",
        "Collections Framework",
        "ArrayList, HashSet and TreeSet",
        "HashMap and TreeMap",
        "JDBC"
    ],

    "PYTHON": [
        "Introduction to Python",
        "Variables and Data Types",
        "Operators",
        "Conditional Statements",
        "Loops",
        "Functions",
        "Lists",
        "Tuples",
        "Sets",
        "Dictionaries",
        "Strings",
        "File Handling",
        "Exception Handling",
        "Object Oriented Programming",
        "Modules and Packages"
    ],

    "DSA": [
        "Introduction to Data Structures",
        "Arrays",
        "Strings",
        "Linked Lists",
        "Stacks",
        "Queues",
        "Recursion",
        "Trees",
        "Binary Search Trees",
        "Heaps",
        "Graphs",
        "Searching",
        "Sorting",
        "Hashing",
        "Time and Space Complexity"
    ],

    "COMPUTER NETWORKS": [
        "Introduction to Computer Networks",
        "Network Topologies",
        "OSI Model",
        "TCP/IP Model",
        "Physical Layer",
        "Data Link Layer",
        "Error Detection",
        "Flow Control",
        "Network Layer",
        "IP Addressing",
        "Routing",
        "Transport Layer",
        "TCP and UDP",
        "Application Layer",
        "HTTP, FTP and DNS"
    ],

    "OPERATING SYSTEM": [
        "Introduction to Operating Systems",
        "OS Services",
        "Process Management",
        "Process Scheduling",
        "Threads",
        "CPU Scheduling",
        "Synchronization",
        "Deadlocks",
        "Memory Management",
        "Paging",
        "Segmentation",
        "Virtual Memory",
        "File Systems",
        "Disk Scheduling",
        "Protection and Security"
    ]
}


# ------------------------------------------------------------
# 2. TIME FUNCTIONS
# ------------------------------------------------------------

def parse_start_time(time_string):

    formats = [
        "%I:%M %p",
        "%I %p",
        "%H:%M"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(time_string.upper(), fmt)
        except ValueError:
            pass

    return None


def format_time(time):

    return time.strftime("%I:%M %p")


def add_minutes(time, minutes):

    return time + timedelta(minutes=minutes)


# ------------------------------------------------------------
# 3. NORMAL STUDY DAY
# ------------------------------------------------------------

def create_study_day(day_number, topics, study_hours, start_time):

    print("\n" + "=" * 70)
    print(f"DAY {day_number}")
    print("=" * 70)

    current_time = start_time

    total_study_minutes = int(study_hours * 60)

    # 30 minutes reserved for daily revision
    revision_minutes = 30

    topic_minutes = int(
        (total_study_minutes - revision_minutes) / len(topics)
    )

    # Make sure topic time is reasonable
    if topic_minutes < 10:
        topic_minutes = 10

    for i, topic in enumerate(topics):

        end_time = add_minutes(
            current_time,
            topic_minutes
        )

        print(
            f"{format_time(current_time)} - "
            f"{format_time(end_time)} : "
            f"Study - {topic}"
        )

        current_time = end_time

        # Break after topic
        if i < len(topics) - 1:

            break_end = add_minutes(
                current_time,
                10
            )

            print(
                f"{format_time(current_time)} - "
                f"{format_time(break_end)} : "
                "BREAK"
            )

            current_time = break_end

    # Daily revision
    revision_end = add_minutes(
        current_time,
        revision_minutes
    )

    print(
        f"{format_time(current_time)} - "
        f"{format_time(revision_end)} : "
        "DAILY REVISION + RECALL"
    )

    print("\nRevision task:")
    print("- Recall today's topics")
    print("- Review important definitions")
    print("- Solve a few questions")
    print("- Write down difficult topics")


# ------------------------------------------------------------
# 4. FINAL REVISION DAY
# ------------------------------------------------------------

def create_final_day(day_number, subject, study_hours, start_time):

    print("\n" + "=" * 70)
    print(f"DAY {day_number} - COMPLETE REVISION")
    print("=" * 70)

    current_time = start_time

    total_minutes = int(study_hours * 60)

    # Divide final day into revision sections
    complete_revision = int(total_minutes * 0.35)
    important_topics = int(total_minutes * 0.25)
    question_practice = int(total_minutes * 0.25)
    quick_revision = (
        total_minutes
        - complete_revision
        - important_topics
        - question_practice
    )

    # --------------------------------------------------------
    # COMPLETE REVISION
    # --------------------------------------------------------

    end_time = add_minutes(
        current_time,
        complete_revision
    )

    print(
        f"{format_time(current_time)} - "
        f"{format_time(end_time)} : "
        "Complete Subject Revision"
    )

    current_time = end_time

    # Break
    break_end = add_minutes(current_time, 15)

    print(
        f"{format_time(current_time)} - "
        f"{format_time(break_end)} : BREAK"
    )

    current_time = break_end

    # --------------------------------------------------------
    # IMPORTANT TOPICS
    # --------------------------------------------------------

    end_time = add_minutes(
        current_time,
        important_topics
    )

    print(
        f"{format_time(current_time)} - "
        f"{format_time(end_time)} : "
        "Important Topics + Difficult Concepts"
    )

    current_time = end_time

    # Break
    break_end = add_minutes(current_time, 15)

    print(
        f"{format_time(current_time)} - "
        f"{format_time(break_end)} : BREAK"
    )

    current_time = break_end

    # --------------------------------------------------------
    # QUESTION PRACTICE
    # --------------------------------------------------------

    end_time = add_minutes(
        current_time,
        question_practice
    )

    print(
        f"{format_time(current_time)} - "
        f"{format_time(end_time)} : "
        "Important Questions + Previous Year Questions"
    )

    current_time = end_time

    # --------------------------------------------------------
    # FINAL QUICK REVISION
    # --------------------------------------------------------

    end_time = add_minutes(
        current_time,
        quick_revision
    )

    print(
        f"{format_time(current_time)} - "
        f"{format_time(end_time)} : "
        "Final Quick Revision"
    )

    print("\nFinal Day Checklist:")
    print("- Revise the entire subject")
    print("- Review difficult topics")
    print("- Practice important questions")
    print("- Review formulas / definitions")
    print("- Do not start completely new topics")


# ------------------------------------------------------------
# 5. MAIN AGENT
# ------------------------------------------------------------

print("\n")
print("*" * 70)
print("                 AI STUDY PLAN AGENT")
print("*" * 70)


# ------------------------------------------------------------
# INPUT 1 - NAME
# ------------------------------------------------------------

name = input("\nEnter your name: ")


# ------------------------------------------------------------
# INPUT 2 - NUMBER OF DAYS
# ------------------------------------------------------------

while True:

    try:

        days = int(
            input("How many days do you have to study? ")
        )

        if days >= 1:
            break

        print("Please enter at least 1 day.")

    except ValueError:

        print("Please enter a valid number.")


# ------------------------------------------------------------
# INPUT 3 - SUBJECT
# ------------------------------------------------------------

print("\nAvailable Subjects:")

for subject in subjects.keys():

    print("  -", subject)


while True:

    subject = input(
        "\nWhich subject do you want to study? "
    ).upper().strip()

    if subject in subjects:
        break

    print("\nSubject not available.")
    print("Please choose from the available subjects.")


# ------------------------------------------------------------
# INPUT 4 - HOURS PER DAY
# ------------------------------------------------------------

while True:

    try:

        study_hours = float(
            input(
                "How many hours can you study per day? "
            )
        )

        if study_hours > 0:

            break

        print("Please enter a positive number.")

    except ValueError:

        print("Please enter a valid number.")


# ------------------------------------------------------------
# INPUT 5 - STARTING TIME
# ------------------------------------------------------------

while True:

    time_input = input(
        "What time do you want to start studying? "
        "(Example: 8:00 AM): "
    )

    start_time = parse_start_time(time_input)

    if start_time is not None:
        break

    print(
        "Invalid time format."
        "\nExample: 8:00 AM or 10:30 AM"
    )


# ------------------------------------------------------------
# GET TOPICS
# ------------------------------------------------------------

all_topics = subjects[subject]


# ------------------------------------------------------------
# DISPLAY PLAN INFORMATION
# ------------------------------------------------------------

print("\n")
print("*" * 70)
print("                  YOUR STUDY PLAN")
print("*" * 70)

print(f"\nStudent Name    : {name}")
print(f"Subject         : {subject}")
print(f"Number of Days  : {days}")
print(f"Study Hours/day : {study_hours}")
print(f"Starting Time   : {format_time(start_time)}")
print(f"Total Topics    : {len(all_topics)}")


# ------------------------------------------------------------
# ONE DAY CASE
# ------------------------------------------------------------

if days == 1:

    print(
        "\nSince you have only one day, "
        "the entire day is dedicated to revision."
    )

    create_final_day(
        1,
        subject,
        study_hours,
        start_time
    )


# ------------------------------------------------------------
# MULTIPLE DAYS
# ------------------------------------------------------------

else:

    # Last day is reserved for complete revision
    study_days = days - 1

    # Divide topics among study days
    topics_per_day = len(all_topics) // study_days

    extra_topics = len(all_topics) % study_days

    start_index = 0


    # --------------------------------------------------------
    # CREATE STUDY DAYS
    # --------------------------------------------------------

    for day in range(1, days):

        number_of_topics = topics_per_day

        # Distribute remaining topics
        if day <= extra_topics:

            number_of_topics += 1


        day_topics = all_topics[
            start_index:
            start_index + number_of_topics
        ]


        create_study_day(
            day,
            day_topics,
            study_hours,
            start_time
        )


        start_index += number_of_topics


    # --------------------------------------------------------
    # FINAL REVISION DAY
    # --------------------------------------------------------

    create_final_day(
        days,
        subject,
        study_hours,
        start_time
    )


# ------------------------------------------------------------
# FINISHED
# ------------------------------------------------------------

print("\n")
print("*" * 70)
print("              STUDY PLAN CREATED SUCCESSFULLY")
print("*" * 70)

print(
    f"\nGood luck, {name}! "
    "Follow the schedule consistently."
)

print("\nRemember:")
print("1. Take the scheduled breaks.")
print("2. Revise every day.")
print("3. Practice questions after studying.")
print("4. Use the final day only for revision.")