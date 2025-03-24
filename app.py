import streamlit as st

st.title("Basic Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Buttons for operations
if st.button("Add"):
    st.write(f"Result: {num1 + num2}")

if st.button("Subtract"):
    st.write(f"Result: {num1 - num2}")

if st.button("Multiply"):
    st.write(f"Result: {num1 * num2}")

if st.button("Divide"):
    if num2 != 0:
        st.write(f"Result: {num1 / num2}")
    else:
        st.write("Error: Cannot divide by zero")
