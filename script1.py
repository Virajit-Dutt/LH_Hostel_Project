import streamlit as st
import datetime

# Create file accept widget
file1 = st.file_uploader("Upload file for mess", type=("xlsx","csv"))

# take multiple files as input with file_uploade

file2 = st.file_uploader("Upload files for attendance", type=("xlsx","csv"),accept_multiple_files=True)

# Enter button
btn = st.button("Submit")

# print after clicking the button
if btn:
    mess_absentees = 10
    total_students = 50

    # Create a card-like layout with three columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Mess")
        st.write("Mess 1")
        st.write("Mess 2")
        st.write("Mess 3")
        st.write("Mess 4")

    # Display the data in the columns
    with col2:
        st.write("Absentees")
        st.write(10)
        st.write(15)
        st.write(20)
        st.write(30)

    with col3:
        st.write("Total Students")
        st.write(100)
        st.write(130)
        st.write(140)
        st.write(160)

