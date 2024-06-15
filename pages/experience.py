import streamlit as st


def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')


def experience():
    st.subheader("💼 Work History")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("<h4>🦊 ShadowFox</h4>", unsafe_allow_html=True)
    with col2:
        st.write("<h4>💡 Prodigy InfoTech</h4>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([7, 2, 7, 2])
    with col1:
        st.write("<h5><b>Python Developer Intern</b></h5>", unsafe_allow_html=True)
        st.write("📅 April '24 - May '24 ")
        st.write("📍 <i>Chennai, Tamil Nadu, India </i><br>&nbsp;&nbsp;&nbsp;<i>(Remote)</i>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <style>
                .vertical-line2 {
                    border-left: 6px solid orange;
                    height: 110px;
                    margin: auto;
                }
            </style>
            """, unsafe_allow_html=True)
        st.markdown('<div class="vertical-line2"></div>', unsafe_allow_html=True)

    with col3:
        st.write("<h5><b>Data Analyst Intern</b></h5>", unsafe_allow_html=True)
        st.write("📅 March '24 - April '24 ")
        st.write("📍 <i>Mumbai, Maharashtra, India</i><br>&nbsp;&nbsp;&nbsp;<i>(Remote)</i>", unsafe_allow_html=True)

    with col4:
        st.markdown(
            """
            <style>
                .vertical-line {
                    border-left: 6px solid yellow;
                    height: 110px;
                    margin: auto;
                }
            </style>
            """, unsafe_allow_html=True)
        st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

    # --- EXPERIENCE AND QUALIFICATIONS ---

    V_SPACE(1)
    V_SPACE(1)
    st.subheader("📖 Education")
    st.write("---")

    st.write(f"1) <h5><b>Bachelor's in Computer Science</b></h5>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4, 21, 3])
    with col1:
        st.image("assets/college.png")

    with col2:
        st.write(
            """
    - **P.E.S. Modern College of Arts, Science and Commerce**
    - 📍 <i>Pune, Maharashtra, India</i>
    - (2020-2023)
    """, unsafe_allow_html=True)
    with col3:
        st.write("8.57")

    st.write(f"2) <h5><b>Higher Secondary Education</b></h5>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4, 21, 3])
    with col1:
        st.image("assets/school.jpg")

    with col2:
        st.write(
            """
    - **Kendriya Vidyalaya No.2 AFS**
    - 📍 <i>Pune, Maharashtra, India</i>
    - (2018-2020)
    """, unsafe_allow_html=True)
    with col3:
        st.write("77.8%")
    ft = """
    <style>
    a:link , a:visited{
    color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
    background-color: transparent;
    text-decoration: none;
    }

    a:hover,  a:active {
    color: #0283C3; /* theme's primary color*/
    background-color: transparent;
    text-decoration: underline;
    }

    #page-container {
      position: relative;
      min-height: 10vh;
    }

    footer{
        visibility:hidden;
    }

    .footer {
    position: relative;
    left: 0;
    top:150px;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: #808080;
    text-align: left;
    }
    </style>

    <div id="page-container">

    <div class="footer">
    <p style='font-size: 1em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
    with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/kunal9960" target="_blank"> by Kunal</a>
    <a style='display: inline; text-align: left;'>© Copyright 2024</a></p>
    </div>

    </div>
    """
    st.write(ft, unsafe_allow_html=True)



