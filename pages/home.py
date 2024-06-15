import streamlit as st
from pathlib import Path
from PIL import Image


def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')


def frontpage():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    resume_file = current_dir / "assets" / "resume.pdf"
    profile_pic = current_dir / "assets" / "profile-pic.png"

    name = "Python Developer"
    description = """ 
        Hi! I'm Kunal Dalvi, a Python enthusiast with a keen interest in data analysis. 
        I'm driven by curiosity and love taking on new challenges. 
        I'm dedicated to unravel insights from complex datasets through statistical methods and programming.
        """

    socials = (
        '<a href="https://www.linkedin.com/in/kunal-dalvi-0b273b2b4"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-linkedin-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
        '<a href="https://twitter.com/kunalfr_"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-twitter-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
        '<a href="https://github.com/kunal9960"><img src="https://raw.githubusercontent.com/kunal9960/kunal9960/main/github.png" width="62"/></a>',
        '<a href="mailto:kunald9960@gmail.com"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-gmail-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
        '<a href="https://discord.gg/bge3cXHuNC" class="no-margin"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-discord-social-media-justicon-lineal-color-justicon.png" width="60"/></a>'
    )

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(profile_pic, width=500)

    with col2:
        st.title(name)
        st.info(description)
        st.download_button(
            label="📝 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )

    # --- SOCIAL LINKS ---

    socials_html = ''.join(socials)

    styled_socials_html = f"""
            <style>
                .socials a {{
                    margin-right: 100px;
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

    st.subheader("🛠️ Hard Skills")
    st.write("---")
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
