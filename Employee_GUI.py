import streamlit as st
from Employee_View import EmployeeManager

employee_instance = EmployeeManager()
tab1, tab2 = st.tabs(["ADD","VIEW"])
with (tab1):
    st.title("Add New Employee")
    name = st.text_input("Enter The Name")
    place = st.text_input("Enter The Place")
    mobile = st.text_input("Enter The Mobile Number")
    email = st.text_input("Enter The Email")
    department = st.text_input("Enter The Department")
    salary = st.text_input("Enter The Salary")
    joining_date = st.text_input("Enter The Joined Date (YYYY-MM-DD)")
    if st.button("Add New Employee"):
        employee_instance.post(name=name,place=place,mobile=mobile,email=email,department=department,salary=salary,joining_date=joining_date)
        st.success("Employee Added Successfully")
with tab2:
    st.title("View Employee Details")
    record = employee_instance.get()
    if record:
        st.table(record)
    else:
        st.warning("No Data Found")