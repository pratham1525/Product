import streamlit as st

def calculate_price(outer_diameter, inner_diameter, length, rate):
    weight = (0.00000675*(length)*(((outer_diameter)**2)-((inner_diameter)**2)))
    price = weight * rate
    return price

st.title("Product Price Calculator")

outer_diameter = st.number_input("Enter outer diameter (mm)", step=0.01)
inner_diameter = st.number_input("Enter inner diameter (mm)", step=0.01)
length = st.number_input("Enter length (mm)", step=0.01)
rate = st.number_input("Enter rate per kg", step=0.01)

if st.button("Calculate Price"):
    price = calculate_price(outer_diameter, inner_diameter, length, rate)
    weight =(0.00000675*(length)*(((outer_diameter)**2)-((inner_diameter)**2)))
    st.success(f"Weight of product is: {weight} kg")
    st.success(f"Price of product is: **₹{price}**")
