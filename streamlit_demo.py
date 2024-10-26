import streamlit as st
from datetime import date

st.set_page_config(layout="wide")


st.title("Hello Warzo")
col1, col2, col3  = st.columns(3) 
with st.expander(" see more "):

    st.selectbox(
        "Select a topic of your interest",
        ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home",
         "insider", "magazine", "movies", "nyregion", "obituaries", "opinion", "politics",
         "realestate", "science", "sports", "sundayreview", "technology", "theater", "t-magazine",
         "travel", "upshot", "us", "world"]
    )

st.title("Sum Odd numbers")
#st.title("_Streamlit_ is :blue[cool] :sunglasses:")
#number = st.number_input("Insert a number")
#number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
number = st.number_input("Insert a number", min_value=1, max_value=100, value="min") 
#st.write("The current number is ", number)
i=1; n=1; s=0;
while i<=number:
#    print(n)
    s=s+n
    n=n+2
    i=i+1
st.write("Sum of 1st 10 odd numbers ", s)

total=0
for k in range(0,number):
    total=total+2*k+1
st.write("Sum of 1st 10 odd numbers ", total)

st.write("Sum of 1st 10 odd numbers ",number*number)


st.title("Calculate Age")
minDate = date(1900,1,1)
maxDate = date(2120,1,1)

d = st.date_input("When's your birthday",date.today(),minDate,maxDate)
st.write("Your birthday is:", d)
def age_calculator(d):
    today = date.today()
    #st.write(today)
    days = (today - d).days
    months = 0
    years = 0
    while days >= 365.25:
        days -= 365.25
        years += 1
    while days >= 30.55:
        days -= 30.55
        months += 1
    return f'You are {years} years, {months} months and {int(days)} days old.'

age = age_calculator(d)
st.write("You are now ",age)  
