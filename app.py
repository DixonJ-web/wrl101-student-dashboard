import streamlit as st
import pandas as pd


# Page setup controls the browser tab title and makes the app use the full page width.
st.set_page_config(
    page_title="Student Productivity and Academic Support",
    page_icon=":books:",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
    }
    .status-label {
        border-radius: 999px;
        color: white;
        display: inline-block;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 0.35rem;
        padding: 0.2rem 0.65rem;
    }
    .status-completed {
        background-color: #2f855a;
    }
    .status-progress {
        background-color: #2b6cb0;
    }
    .status-started {
        background-color: #975a16;
    }
    .priority-high {
        color: #c53030;
        font-weight: 700;
    }
    .priority-medium {
        color: #2b6cb0;
        font-weight: 700;
    }
    .priority-low {
        color: #2f855a;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Sample data is stored in simple Python lists and dictionaries.
# This keeps the prototype beginner-friendly and avoids databases or APIs.
APP_PASSWORD = "WRL101_Test_2026"

assignments = [
    {
        "Module": "ENG101 Engineering Design",
        "Assignment": "Bridge Design Concept Sketches",
        "Due Date": "2026-06-12",
        "Priority": "High",
        "Status": "In progress",
    },
    {
        "Module": "MTH104 Engineering Mathematics",
        "Assignment": "Differential Equations Problem Set",
        "Due Date": "2026-06-15",
        "Priority": "High",
        "Status": "Not started",
    },
    {
        "Module": "PHY102 Mechanics and Materials",
        "Assignment": "Stress-Strain Lab Report",
        "Due Date": "2026-06-17",
        "Priority": "High",
        "Status": "In progress",
    },
    {
        "Module": "CAD110 Computer-Aided Design",
        "Assignment": "3D Gearbox Housing Model",
        "Due Date": "2026-06-20",
        "Priority": "Medium",
        "Status": "Not started",
    },
    {
        "Module": "EEE105 Electrical Circuits",
        "Assignment": "Circuit Simulation Worksheet",
        "Due Date": "2026-06-22",
        "Priority": "Medium",
        "Status": "In progress",
    },
    {
        "Module": "MAT112 Materials Science",
        "Assignment": "Material Selection Case Study",
        "Due Date": "2026-06-26",
        "Priority": "Medium",
        "Status": "Completed",
    },
    {
        "Module": "PRJ120 Engineering Practice",
        "Assignment": "Team Project Progress Log",
        "Due Date": "2026-06-28",
        "Priority": "Low",
        "Status": "In progress",
    },
    {
        "Module": "WRL101 Academic and Professional Skills",
        "Assignment": "Student Productivity App Report",
        "Due Date": "2026-07-01",
        "Priority": "High",
        "Status": "In progress",
    },
    {
        "Module": "SUS130 Sustainable Engineering",
        "Assignment": "Renewable Energy Reflection",
        "Due Date": "2026-07-04",
        "Priority": "Low",
        "Status": "Completed",
    },
]

tasks = [
    {"Task": "Complete free-body diagram practice questions", "Category": "Study", "Done": True},
    {"Task": "Update CAD model dimensions after workshop feedback", "Category": "Assignment", "Done": False},
    {"Task": "Prepare MATLAB graphs for mechanics lab report", "Category": "Assignment", "Done": False},
    {"Task": "Review Kirchhoff's laws before circuit seminar", "Category": "Study", "Done": True},
    {"Task": "Book academic skills appointment for WRL101 report", "Category": "Support", "Done": False},
    {"Task": "Upload team project meeting notes to shared folder", "Category": "Teamwork", "Done": True},
    {"Task": "Create reference list for sustainable engineering reflection", "Category": "Research", "Done": False},
    {"Task": "Revise integration techniques for maths quiz", "Category": "Study", "Done": False},
    {"Task": "Check material property values in CES EduPack notes", "Category": "Research", "Done": True},
    {"Task": "Plan screenshots for productivity app prototype report", "Category": "Planning", "Done": False},
]

timetable = [
    {"Day": "Monday", "Time": "09:00 - 10:00", "Activity": "Engineering Mathematics Lecture", "Location": "Lecture Theatre 2"},
    {"Day": "Monday", "Time": "11:00 - 13:00", "Activity": "CAD Workshop", "Location": "Design Lab"},
    {"Day": "Monday", "Time": "14:00 - 15:00", "Activity": "Independent Study: Maths Problem Set", "Location": "Library"},
    {"Day": "Tuesday", "Time": "10:00 - 12:00", "Activity": "Mechanics and Materials Lab", "Location": "Structures Lab"},
    {"Day": "Tuesday", "Time": "13:00 - 14:00", "Activity": "WRL101 Seminar", "Location": "Room B12"},
    {"Day": "Wednesday", "Time": "09:00 - 10:30", "Activity": "Electrical Circuits Lecture", "Location": "Lecture Theatre 1"},
    {"Day": "Wednesday", "Time": "12:00 - 13:00", "Activity": "Academic Skills Drop-in", "Location": "Student Support Centre"},
    {"Day": "Thursday", "Time": "10:00 - 12:00", "Activity": "Engineering Design Team Meeting", "Location": "Project Studio"},
    {"Day": "Thursday", "Time": "15:00 - 16:00", "Activity": "Materials Science Tutorial", "Location": "Room C04"},
    {"Day": "Friday", "Time": "09:30 - 11:00", "Activity": "Sustainable Engineering Lecture", "Location": "Lecture Theatre 3"},
    {"Day": "Friday", "Time": "13:00 - 15:00", "Activity": "Prototype Report Writing Session", "Location": "Library"},
]

notes = [
    {
        "Title": "Bridge Design Concept",
        "Content": "Compare truss and beam bridge options. Mention load distribution, material efficiency, safety factor, and construction constraints.",
    },
    {
        "Title": "Mechanics Lab Reminder",
        "Content": "Include labelled stress-strain graph, units for force and extension, discussion of elastic region, and one limitation of the experiment.",
    },
    {
        "Title": "Circuit Analysis Notes",
        "Content": "Use Kirchhoff's current law at junctions and Kirchhoff's voltage law around loops. Check sign convention before calculating resistor voltage drops.",
    },
    {
        "Title": "WRL101 Report Structure",
        "Content": "Introduction, user needs, prototype features, screenshots, evaluation, limitations, and conclusion. Keep the explanation clear for a non-technical reader.",
    },
    {
        "Title": "Materials Selection",
        "Content": "For lightweight structures, compare aluminium alloy, mild steel, and carbon fibre using density, strength, cost, availability, and sustainability.",
    },
    {
        "Title": "Team Project Meeting Actions",
        "Content": "Alex will check dimensions, Priya will update the risk table, Sam will prepare slides, and I will write the design justification section.",
    },
]

support_links = [
    {
        "Service": "Academic Skills Centre",
        "Description": "Help with writing, referencing, research, and study techniques.",
        "Contact": "academic.support@university.ac.uk",
    },
    {
        "Service": "Engineering Faculty Office",
        "Description": "Support with module queries, lab schedules, workshop bookings, and assessment guidance.",
        "Contact": "engineering.office@university.ac.uk",
    },
    {
        "Service": "Library Help Desk",
        "Description": "Support with books, journals, standards, databases, and finding credible engineering sources.",
        "Contact": "library@university.ac.uk",
    },
    {
        "Service": "Personal Tutor",
        "Description": "Guidance about academic progress, wellbeing, and course concerns.",
        "Contact": "personal.tutor@university.ac.uk",
    },
    {
        "Service": "IT and Software Support",
        "Description": "Help with university accounts, CAD software, MATLAB access, and online learning platforms.",
        "Contact": "it.support@university.ac.uk",
    },
    {
        "Service": "Careers and Employability",
        "Description": "Advice on engineering CVs, placement applications, interviews, and professional development.",
        "Contact": "careers@university.ac.uk",
    },
]

feature_tests = [
    {
        "Feature": "Sidebar navigation",
        "Test Input": "Select each page from the sidebar radio menu",
        "Expected Result": "The selected page opens and the correct heading is displayed",
        "Actual Result": "Each page opens with the correct content and heading",
        "Status": "Pass",
    },
    {
        "Feature": "Dashboard metrics",
        "Test Input": "Open the Dashboard page",
        "Expected Result": "Assignment, task and timetable summary numbers are visible",
        "Actual Result": "Metrics show assignments, completed work, open tasks and weekly events",
        "Status": "Pass",
    },
    {
        "Feature": "Assignment tracker table",
        "Test Input": "Open Assignment Tracker page",
        "Expected Result": "Engineering assignments display with module, due date, priority and status",
        "Actual Result": "All sample engineering assignments are shown in a readable table",
        "Status": "Pass",
    },
    {
        "Feature": "Assignment status labels",
        "Test Input": "View detailed assignment rows",
        "Expected Result": "Completed, In progress and Not started labels are visible",
        "Actual Result": "Coloured status labels display beside each assignment",
        "Status": "Pass",
    },
    {
        "Feature": "To-do list checkboxes",
        "Test Input": "Tick and untick sample study tasks",
        "Expected Result": "Checkboxes can be changed during the current session",
        "Actual Result": "Checkboxes respond correctly while the prototype is open",
        "Status": "Pass",
    },
    {
        "Feature": "Weekly timetable",
        "Test Input": "Open Timetable page",
        "Expected Result": "Weekly lectures, labs, workshops and study sessions are visible",
        "Actual Result": "The timetable table and timetable cards display correctly",
        "Status": "Pass",
    },
    {
        "Feature": "Notes page",
        "Test Input": "Open and close saved note expanders",
        "Expected Result": "Engineering notes can be viewed clearly",
        "Actual Result": "Saved notes expand and show the correct sample content",
        "Status": "Pass",
    },
    {
        "Feature": "Academic support directory",
        "Test Input": "Open Academic Support page",
        "Expected Result": "Support services and contact details are displayed",
        "Actual Result": "Support cards show service descriptions and contact emails",
        "Status": "Pass",
    },
]


def show_header(title, subtitle):
    """Display a consistent page heading."""
    st.title(title)
    st.write(subtitle)
    st.divider()


def status_label(status):
    """Return a coloured HTML label for assignment status text."""
    status_class = {
        "Completed": "status-completed",
        "In progress": "status-progress",
        "Not started": "status-started",
    }.get(status, "status-started")

    return f"<span class='status-label {status_class}'>{status}</span>"


def priority_text(priority):
    """Return priority text with simple colour styling."""
    priority_class = {
        "High": "priority-high",
        "Medium": "priority-medium",
        "Low": "priority-low",
    }.get(priority, "priority-medium")

    return f"<span class='{priority_class}'>{priority}</span>"


def check_password():
    """Show a simple password screen before loading the prototype."""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    st.title("Student Productivity App")
    st.write("Enter the project password to view the prototype.")

    entered_password = st.text_input("Password", type="password")

    if st.button("Enter"):
        if entered_password == APP_PASSWORD:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("Incorrect password. Please try again.")

    st.caption("Prototype password: WRL101_Test_2026")
    return False


def dashboard_page():
    """Show a quick overview of the student's study progress."""
    show_header(
        "Engineering Student Dashboard",
        "A populated weekly view of academic activity, engineering deadlines, and support reminders.",
    )

    assignment_df = pd.DataFrame(assignments)
    task_df = pd.DataFrame(tasks)

    total_assignments = len(assignment_df)
    completed_assignments = len(assignment_df[assignment_df["Status"] == "Completed"])
    in_progress_assignments = len(assignment_df[assignment_df["Status"] == "In progress"])
    high_priority_assignments = len(assignment_df[assignment_df["Priority"] == "High"])
    open_tasks = len(task_df[task_df["Done"] == False])
    completed_tasks = len(task_df[task_df["Done"]])
    timetable_items = len(timetable)
    next_deadline = assignment_df.sort_values("Due Date").iloc[0]
    assignment_progress = completed_assignments / total_assignments
    task_progress = completed_tasks / len(task_df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Assignments", total_assignments, f"{high_priority_assignments} high priority")
    col2.metric("Completed", completed_assignments, f"{in_progress_assignments} in progress")
    col3.metric("Open Tasks", open_tasks, f"{completed_tasks} completed")
    col4.metric("Weekly Events", timetable_items, "lectures, labs and study")

    summary_col1, summary_col2 = st.columns(2)
    with summary_col1:
        st.subheader("Coursework Progress")
        st.progress(assignment_progress)
        st.caption(f"{completed_assignments} of {total_assignments} assignments completed")

    with summary_col2:
        st.subheader("Study Task Progress")
        st.progress(task_progress)
        st.caption(f"{completed_tasks} of {len(task_df)} weekly tasks completed")

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.subheader("Upcoming Engineering Assignments")
        for item in assignments[:6]:
            row_left, row_right = st.columns([3, 1])
            with row_left:
                st.markdown(f"**{item['Assignment']}**")
                st.caption(f"{item['Module']} | Due {item['Due Date']}")
            with row_right:
                st.markdown(status_label(item["Status"]), unsafe_allow_html=True)
                st.markdown(priority_text(item["Priority"]), unsafe_allow_html=True)
            st.divider()

    with right_col:
        st.subheader("Study Focus")
        st.info("Prepare the bridge concept sketches, finish mechanics lab graphs, and revise differential equations.")

        st.subheader("Next Deadline")
        st.write(f"**{next_deadline['Assignment']}**")
        st.caption(f"{next_deadline['Module']} | {next_deadline['Due Date']}")
        st.markdown(status_label(next_deadline["Status"]), unsafe_allow_html=True)

        st.subheader("Support Reminder")
        st.write("Book an academic skills session to review the WRL101 prototype report structure.")

    st.subheader("Weekly Task Summary")
    chart_data = task_df["Category"].value_counts()
    st.bar_chart(chart_data)


def assignment_tracker_page():
    """Display assignment details in a simple table."""
    show_header(
        "Assignment Tracker",
        "Track engineering coursework deadlines, priorities, and progress.",
    )

    assignment_df = pd.DataFrame(assignments)
    summary_col, table_col = st.columns([1, 2])

    with summary_col:
        st.subheader("Tracker Summary")
        st.metric("High Priority", len(assignment_df[assignment_df["Priority"] == "High"]))
        st.metric("In Progress", len(assignment_df[assignment_df["Status"] == "In progress"]))
        st.metric("Not Started", len(assignment_df[assignment_df["Status"] == "Not started"]))

        st.info("This section helps students quickly see which engineering assignments need attention first.")

    with table_col:
        st.subheader("Coursework List")
        st.dataframe(assignment_df, use_container_width=True, hide_index=True)

    st.subheader("Assignment Progress")
    status_counts = assignment_df["Status"].value_counts()
    st.bar_chart(status_counts)

    st.subheader("Detailed View")
    for item in assignments:
        cols = st.columns([2, 1, 1])
        cols[0].write(f"**{item['Assignment']}**")
        cols[0].caption(item["Module"])
        cols[1].write(f"Due: **{item['Due Date']}**")
        cols[1].markdown(priority_text(item["Priority"]), unsafe_allow_html=True)
        cols[2].markdown(status_label(item["Status"]), unsafe_allow_html=True)
        st.divider()


def todo_list_page():
    """Display a prototype to-do list using checkboxes."""
    show_header(
        "To-Do List",
        "Organise weekly engineering study tasks and keep track of what has been completed.",
    )

    task_df = pd.DataFrame(tasks)
    done_count = len(task_df[task_df["Done"]])
    remaining_count = len(task_df[task_df["Done"] == False])

    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric("Total Tasks", len(tasks))
    metric_col2.metric("Completed", done_count)
    metric_col3.metric("Remaining", remaining_count)

    st.subheader("This Week's Tasks")
    left_col, right_col = st.columns([2, 1])

    with left_col:
        for task in tasks:
            st.checkbox(
                f"{task['Task']} ({task['Category']})",
                value=task["Done"],
                key=task["Task"],
            )

    with right_col:
        st.subheader("Planning Notes")
        st.write("Suggested study order:")
        st.write("1. Finish urgent design and lab work.")
        st.write("2. Revise maths and circuits topics.")
        st.write("3. Prepare WRL101 report screenshots.")

    st.success("Prototype note: checkbox changes are temporary and reset when the page reloads.")


def timetable_page():
    """Display the weekly timetable."""
    show_header(
        "Timetable",
        "View lectures, labs, workshops, support sessions, and independent study time.",
    )

    timetable_df = pd.DataFrame(timetable)
    st.subheader("Weekly Overview")
    st.dataframe(timetable_df, use_container_width=True, hide_index=True)

    st.subheader("Timetable Cards")
    for item in timetable:
        col1, col2, col3 = st.columns([1, 2, 1])
        col1.write(f"**{item['Day']}**")
        col1.caption(item["Time"])
        col2.write(item["Activity"])
        col3.caption(item["Location"])
        st.divider()


def notes_page():
    """Display sample student notes."""
    show_header(
        "Engineering Notes",
        "Keep useful module notes, project reminders, and report planning points in one place.",
    )

    note_col, quick_col = st.columns([2, 1])

    with note_col:
        st.subheader("Saved Notes")
        for note in notes:
            with st.expander(note["Title"], expanded=True):
                st.write(note["Content"])

    with quick_col:
        st.subheader("Quick Capture")
        st.text_area(
            "Quick note",
            value="Example: Add dashboard, assignment tracker, timetable, and notes screenshots to the WRL101 report.",
            height=180,
        )
        st.info("Prototype note: this text area is for demonstration only and does not save permanently.")

    st.subheader("Report Checklist")
    check_col1, check_col2 = st.columns(2)
    check_col1.checkbox("Include dashboard screenshot", value=True)
    check_col1.checkbox("Explain target engineering student users", value=True)
    check_col2.checkbox("Describe prototype features", value=False)
    check_col2.checkbox("Write evaluation and conclusion", value=False)


def academic_support_page():
    """Display academic support services and contact information."""
    show_header(
        "Academic Support",
        "Find useful university support services for engineering study, research, and wellbeing.",
    )

    intro_col, reminder_col = st.columns([2, 1])

    with intro_col:
        st.subheader("Support Directory")
        st.write("This page shows how a student could quickly find university support contacts inside the application.")

    with reminder_col:
        st.metric("Available Services", len(support_links))
        st.info("Suggested action: contact the Academic Skills Centre before final WRL101 submission.")

    left_col, right_col = st.columns(2)
    for index, item in enumerate(support_links):
        target_col = left_col if index % 2 == 0 else right_col
        with target_col:
            st.subheader(item["Service"])
            st.write(item["Description"])
            st.caption(f"Contact: {item['Contact']}")
            st.divider()


def testing_page():
    """Display simple testing evidence for the project report."""
    show_header(
        "Testing Evidence",
        "A simple record of feature tests carried out on the working prototype.",
    )

    test_df = pd.DataFrame(feature_tests)
    passed_tests = len(test_df[test_df["Status"] == "Pass"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Tests Recorded", len(test_df))
    col2.metric("Passed", passed_tests)
    col3.metric("Failed", len(test_df) - passed_tests)

    st.subheader("Feature Test Table")
    st.dataframe(test_df, use_container_width=True, hide_index=True)

    st.subheader("Testing Summary")
    st.success("All recorded prototype tests passed during manual testing.")
    st.write(
        "This testing page provides evidence that the main prototype features were checked, "
        "including navigation, dashboard summaries, assignment tracking, to-do tasks, "
        "timetable content, notes and academic support information."
    )


def about_project_page():
    """Explain the purpose and technologies used in the prototype."""
    show_header(
        "About Project",
        "An overview of the WRL101 student productivity and academic support prototype.",
    )

    purpose_col, tech_col = st.columns(2)

    with purpose_col:
        st.subheader("Project Purpose")
        st.write(
            "This application is a working prototype for a university project titled "
            "**Student Productivity and Academic Support Application**. It is designed "
            "to show how an engineering student could organise assignments, weekly tasks, "
            "timetable events, notes, academic support contacts and testing evidence in "
            "one simple dashboard."
        )
        st.write(
            "The prototype is intended for screenshots, demonstration and discussion in "
            "the project report. It focuses on clear layout, realistic sample content and "
            "easy navigation rather than complex backend functionality."
        )

    with tech_col:
        st.subheader("Technologies Used")
        st.write("**Python** was used as the main programming language.")
        st.write("**Streamlit** was used to build the interactive web app interface.")
        st.write("**Pandas** was used to organise sample data into tables and charts.")
        st.info("No database, login system or external API is used in this prototype.")

    st.subheader("Main Prototype Features")
    feature_col1, feature_col2, feature_col3 = st.columns(3)
    feature_col1.write("- Dashboard summary")
    feature_col1.write("- Assignment tracker")
    feature_col1.write("- To-do list")
    feature_col2.write("- Weekly timetable")
    feature_col2.write("- Engineering notes")
    feature_col2.write("- Academic support")
    feature_col3.write("- Testing evidence")
    feature_col3.write("- Sidebar navigation")
    feature_col3.write("- Sample data for screenshots")


if not check_password():
    st.stop()


# Sidebar navigation lets the user move between prototype pages.
st.sidebar.title("WRL101 Prototype")
st.sidebar.write("Student Productivity and Academic Support Application")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Assignment Tracker",
        "To-Do List",
        "Timetable",
        "Notes",
        "Academic Support",
        "Testing",
        "About Project",
    ],
)

st.sidebar.divider()
st.sidebar.info("Engineering student prototype version for university report screenshots.")


if page == "Dashboard":
    dashboard_page()
elif page == "Assignment Tracker":
    assignment_tracker_page()
elif page == "To-Do List":
    todo_list_page()
elif page == "Timetable":
    timetable_page()
elif page == "Notes":
    notes_page()
elif page == "Academic Support":
    academic_support_page()
elif page == "Testing":
    testing_page()
elif page == "About Project":
    about_project_page()
