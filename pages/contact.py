import streamlit as st

def contact():
    st.subheader("🔭 Contact Me ")
    st.write("---")

    col1, col2 = st.columns(2)
    with (col1):
        with st.form(key="email_form"):
            user_email = st.text_input("Your email address")
            raw_message = st.text_area("Your message")
            message = f"""\
Subject: New email from {user_email}
From: {user_email}
{raw_message}
"""
            button = st.form_submit_button("Submit")
            if button:
                send_email(message)
                st.info("Your email was sent successfully!")
                st.balloons()

    with col2:
        st.image(
            "https://steamuserimages-a.akamaihd.net/ugc/1696157019707375037/BD6E6F9F1065D25D25E63DADF820A406B28032BA/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false")
        st.write("<i>\"Sometimes the greatest dishes come from the most unlikely ingredients\"</i> - Po",
                 unsafe_allow_html=True)
        st.markdown(
            "[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F&label=WEBSITE%20VIEWS&labelColor=%23333333&countColor=%23cbc3e3&labelStyle=upper)](https://visitorbadge.io/status?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F)")