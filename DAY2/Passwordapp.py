import streamlit as st

st.title("password analyser")

password=st.text_input("enter the password",type="password")

#st.button("validate")
if st.button("validate"):
    upper=lower=digit=special=False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True
    if len(password)>=8 and upper and lower and special:
        st.success("strong password..thank you")
    else:
        st.error("invaild password")
        
        if len(password)<8:
          st.write("password must cotain at least 8 or more characters")
        if not upper:
          st.write("must contain a uppercase")
        if not lower:
            st.write("must contain a lowercase")
        if not digit:
            st.write("must contain a digit")
        if not special:
            st.write("must contain a special character")


