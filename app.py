
import streamlit as st
from datetime import date

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Absence Management System",
    page_icon="📅",
    layout="wide"
)

# ------------------------------------------------------
# HEADER
# ------------------------------------------------------
st.title("📅 Absence Management System")
st.caption("Submit a leave request")

# ------------------------------------------------------
# EMPLOYEE INFORMATION
# ------------------------------------------------------
st.subheader("Employee Information")

col1, col2 = st.columns(2)

with col1:
    employee_name = st.text_input(
        "Employee Name",
        placeholder="John Doe"
    )

with col2:
    employee_email = st.text_input(
        "Email",
        placeholder="john.doe@company.com"
    )

# ------------------------------------------------------
# ORGANIZATION INFORMATION
# ------------------------------------------------------
st.subheader("Organization")

col1, col2, col3 = st.columns(3)

with col1:
    division = st.selectbox(
        "Division",
        ["", "Community Services Division", "Administrative Services", "IT Division"]
    )

with col2:
    branch = st.selectbox(
        "Branch",
        ["", "Community Operations Branch", "HR Branch", "Finance Branch"]
    )

with col3:
    section = st.selectbox(
        "Section",
        ["", "South 1 & 2", "South 3 & 4", "FHA South", "North 1 & 2"]
    )

# ------------------------------------------------------
# LEAVE DETAILS
# ------------------------------------------------------
st.subheader("Leave Request")

col1, col2 = st.columns(2)

with col1:
    leave_type = st.selectbox(
        "Leave Type",
        [
            "Vacation",
            "Sick Leave",
            "Annual Leave",
            "Holiday Credit",
            "Administrative Time Off",
            "Other"
        ]
    )

with col2:
    request_type = st.selectbox(
        "Request Type",
        [
            "Full Day",
            "Partial Day",
            "Multiple Days (Consecutive)"
        ]
    )

# ------------------------------------------------------
# DATE SELECTION
# ------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(
        "Start Date",
        value=date.today()
    )

with col2:
    end_date = st.date_input(
        "End Date",
        value=date.today()
    )

# ------------------------------------------------------
# PARTIAL DAY OPTIONS
# ------------------------------------------------------
if request_type == "Partial Day":

    st.info("Enter the hours requested.")

    col1, col2 = st.columns(2)

    with col1:
        start_time = st.time_input("Start Time")

    with col2:
        end_time = st.time_input("End Time")

# ------------------------------------------------------
# COMMENTS
# ------------------------------------------------------
comments = st.text_area(
    "Comments",
    placeholder="Provide additional information..."
)

# ------------------------------------------------------
# APPROVERS
# ------------------------------------------------------
st.subheader("Approval Information")

col1, col2 = st.columns(2)

with col1:
    manager = st.text_input(
        "Manager",
        placeholder="manager@company.com"
    )

with col2:
    alternate_manager = st.text_input(
        "Alternate Manager (Optional)",
        placeholder="alternate.manager@company.com"
    )

# ------------------------------------------------------
# SUMMARY
# ------------------------------------------------------
st.subheader("Request Summary")

duration_days = (end_date - start_date).days + 1

st.write(f"**Employee:** {employee_name}")
st.write(f"**Leave Type:** {leave_type}")
st.write(f"**Request Type:** {request_type}")
st.write(f"**Dates:** {start_date} to {end_date}")

if request_type != "Partial Day":
    st.write(f"**Duration:** {duration_days} day(s)")

# ------------------------------------------------------
# SUBMIT
# ------------------------------------------------------
if st.button("Submit Leave Request", type="primary"):

    st.success("✅ Leave request submitted successfully!")

    request_data = {
        "Employee": employee_name,
        "Email": employee_email,
        "Division": division,
        "Branch": branch,
        "Section": section,
        "Leave Type": leave_type,
        "Request Type": request_type,
        "Start Date": str(start_date),
        "End Date": str(end_date),
        "Manager": manager,
        "Alternate Manager": alternate_manager,
        "Comments": comments
    }

    with st.expander("Submitted Data"):
        st.json(request_data)
