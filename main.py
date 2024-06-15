import streamlit as st
import time
from pathlib import Path
from PIL import Image
from send_email import send_email
from streamlit_extras.let_it_rain import rain
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
from pages.home import frontpage as home_page
from pages.experience import experience as experience_
from pages.contact import contact as contact_
from pages.about import about as about_
from pages.projects import projects as project_


# Page setup

page_title = "Portfolio Website"
page_icon = "assets/favicon.ico"
st.set_page_config(page_title=page_title, page_icon=page_icon, initial_sidebar_state="collapsed", layout="wide")


# Navbar settings

pages = ["Home", "Projects", "Experience", "Contact", "About"]
styles = {
    "nav": {
        "background-color": "#262730",
    },
    "div": {
        "max-width": "37rem",
    },
    "span": {
        "border-radius": "0.4rem",
        "color": "white",
        "margin": "0 0.125rem",
        "padding": "0.4300rem 0.725rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(pages, styles=styles)

custom_css1 = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Mulish:wght@400;700&display=swap');

body, h1, h2, h3, h4, h6, p, a, span, h5 {
    font-family: 'Mulish', sans-serif;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css1, unsafe_allow_html=True)

import streamlit as st
from pathlib import Path

# Extra space function


def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')


def frontpage():

    # Path and variable settings

    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    resume_file = current_dir / "assets" / "resume.pdf"

    socials = (
        '<a href="https://www.linkedin.com/in/kunal-dalvi-0b273b2b4"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-linkedin-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
        '<a href="https://twitter.com/kunalfr_"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-twitter-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
        '<a href="https://github.com/kunal9960"><img src="https://raw.githubusercontent.com/kunal9960/kunal9960/main/github.png" width="62"/></a>',
        '<a href="mailto:kunald9960@gmail.com"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-gmail-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
        '<a href="https://discord.gg/bge3cXHuNC" class="no-margin"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-discord-social-media-justicon-lineal-color-justicon.png" width="60"/></a>'
    )

    socials_html = ''.join(socials)

    wave_animation_css = """
    <style>
      span.wave {
        animation-name: wave-animation;
        animation-duration: 2.8s;
        animation-iteration-count: infinite;
        transform-origin: 70% 70%;
        transform: scale(1); /* Adjust the scale value to increase the size */
        display: inline-block;
        margin-left: 8px; /* Adjust the left margin as needed */
      }
      
      @keyframes wave-animation {
        0% { transform: rotate(  0.0deg); }
        10% { transform: rotate(-10.0deg); }
        20% { transform: rotate( 12.0deg); }
        30% { transform: rotate(-10.0deg); }
        40% { transform: rotate(  9.0deg); }
        50% { transform: rotate(  0.0deg); }
        100% { transform: rotate(  0.0deg); }
      }
    </style>
    """

    # Inject the CSS into the Streamlit app
    st.markdown(wave_animation_css, unsafe_allow_html=True)
    # Read and display the resume

    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    # Hero page columns

    col1, col2 = st.columns([1.1, 2])
    with col1:
        animations = f"""
                <style>
                    .home-img img {{
                        width: 21em;
                        border: 3px solid white;
                        background-size: cover;
                        background-position: center center;
                        background-repeat: no-repeat;
                        border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                        position: relative;
                        animation: borderAnimation 8s ease-in-out infinite;
                        transition: all 1s ease-in-out;
                    }}
                    @keyframes borderAnimation {{
                        0% {{
                            border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                        }}

                        50% {{
                            border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
                        }}

                        100% {{
                            border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                        }}

                    }}
                </style>
            """
        st.markdown(animations, unsafe_allow_html=True)
        st.markdown(
            """
            <div class="home-img">
                <img src="https://raw.githubusercontent.com/kunal9960/portfolio/master/assets/profile-pic.png">
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.write(
            """
            <h2 style="display: flex; align-items: center;">
                Python Developer
                <span class="wave">👋🏼</span>
            </h2>
            """, unsafe_allow_html=True)
        V_SPACE(1)
        st.write("<h5>Hi, I'm Kunal Dalvi. A passionate Python developer with a keen interest in Data analysis, "
                 "based in Pune, Maharashtra. 📍</h5>", unsafe_allow_html=True)
        V_SPACE(1)
        styled_socials_html = f"""
            <style>
                .socials a {{
                    margin-right: 40px;
                }}
                .socials img {{
                    cursor: pointer;
                    transition: all .2s ease-in-out;
                }}
                .socials img:hover {{
                    transform: scale(1.2);
                }}
                .no-margin {{
                    margin-right: 0 !important;
                }}
            </style>

            <div class="socials">{socials_html}</div>
            """

        st.markdown(styled_socials_html, unsafe_allow_html=True)
        V_SPACE(1)
        st.download_button(
            label="📋 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )

    # --- SOCIAL LINKS ---

    st.divider()
    st.subheader("🛠️ Hard Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<b>Programming:</b>", unsafe_allow_html=True)
        st.markdown(
            "![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![C++ Badge](https://img.shields.io/badge/C%2B%2B-00599C?logo=cplusplus&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![JavaScript](https://img.shields.io/badge/JavaScript-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E)"
        )

        st.write("<b>Machine Learning/ Deep Learning:</b>", unsafe_allow_html=True)
        st.markdown(
            "![Keras Badge](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![NumPy Badge](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![pandas Badge](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![scikit-learn Badge](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=fff&style=flat)"
            "![TensorFlow Badge](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat&logo=Matplotlib&logoColor=black)&nbsp;&nbsp;"

        )

        st.write("<b>Frameworks and Libraries:</b>", unsafe_allow_html=True)
        st.markdown(
            "![Flask Badge](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)&nbsp;&nbsp;"
            "![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![FPDF](https://img.shields.io/badge/FPDF-%23FF0000.svg?style=flat&logo=Adobe%20Acrobat%20Reader&logoColor=white)&nbsp;&nbsp;"
            "![Pillow](https://img.shields.io/badge/Pillow-%230080FF.svg?style=flat&logo=python&logoColor=white)&nbsp;&nbsp;"
            "![Tkinter](https://img.shields.io/badge/Tkinter-%23646464.svg?style=flat&logo=python&logoColor=white)&nbsp;&nbsp;"
            "![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-%233776AB.svg?style=flat&logo=python&logoColor=white)&nbsp;&nbsp;"
        )

        st.write("<b>Databases:</b>", unsafe_allow_html=True)
        st.markdown(
            "![MySQL Badge](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![MongoDB Badge](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=fff&style=flat)&nbsp;&nbsp;"
        )

    with col2:
        st.image("assets/image.gif")
        st.write("<b>Miscellaneous:</b>", unsafe_allow_html=True)
        st.markdown(
            "![Microsoft Excel Badge](https://img.shields.io/badge/Microsoft%20Excel-217346?logo=microsoftexcel&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![Git Badge](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![PyCharm](https://img.shields.io/badge/pycharm-143?style=flat&logo=pycharm&logoColor=black&color=black&labelColor=green)&nbsp;"
            "![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=flat&logo=visual-studio-code&logoColor=white)&nbsp;&nbsp;"
            "![Replit Badge](https://img.shields.io/badge/Replit-F26207?logo=replit&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![Jupyter Badge](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=fff&style=flat)&nbsp;&nbsp;"
            "![Raspberry Pi](https://img.shields.io/badge/-Raspberry%20Pi-C51A4A?style=flat-square&logo=Raspberry-Pi)"
        )


# Dictionary to map page names to functions
page_functions = {
    "Home": frontpage,
    "Experience": experience_,
    "Contact": contact_,
    "About": about_,
    "Projects": project_
}

# Call the function for the selected page
page_functions[page]()
