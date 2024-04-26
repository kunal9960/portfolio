from pathlib import Path
import streamlit as st
from PIL import Image
from send_email import send_email
from st_on_hover_tabs import on_hover_tabs


# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---


PAGE_TITLE = "Digital CV | Kunal Dalvi"
PAGE_ICON = "assets/favicon.ico"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

NAME = "PORTFOLIO WEBSITE"
DESCRIPTION = """ 
Hi! I'm Kunal Dalvi, a Python enthusiast with a keen interest in data analysis. 
I'm driven by curiosity and love taking on new challenges. 
I'm dedicated to unravel insights from complex datasets through statistical methods and programming.
"""

SOCIALS = (
    '<a href="https://www.linkedin.com/in/kunal-dalvi-0b273b2b4"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-linkedin-social-media-justicon-lineal-color-justicon.png" width="60" /></a>',
    '&nbsp;',
    '<a href="https://twitter.com/kunalfr_"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-twitter-social-media-justicon-lineal-color-justicon.png" width="60" /></a>',
    '&nbsp;',
    '<a href="https://github.com/kunal9960"><img src="https://raw.githubusercontent.com/kunal9960/kunal9960/main/github.png" width="62" /></a>',
    '&nbsp;',
    '<a href="mailto:kunald9960@gmail.com"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-gmail-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
    '&nbsp;',
    '<a href="https://discord.gg/bge3cXHuNC"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-discord-social-media-justicon-lineal-color-justicon.png" width="60" /></a>'
)

st.markdown(
    """
    <style>
    img {
        cursor: pointer;
        transition: all .2s ease-in-out;
    }
    img:hover {
        transform: scale(1.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --- LOAD CSS, PDF & PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- LOAD SIDEBAR CSS ---

st.markdown('<style>' + open('styles/main.css').read() + '</style>', unsafe_allow_html=True)
with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Projects', 'About'],
                         iconName=['home', 'work', 'economy'],
                         styles={'navtab': {'background-color': '#111',
                                            'color': '#818181',
                                            'font-size': '20px',
                                            'transition': '.1s',
                                            'white-space': 'nowrap',
                                            'text-transform': 'uppercase',
                                            'font': 'consolas'},
                                 'tabOptionsStyle': {':hover :hover': {'color': '#CBC3E3',
                                                                       'cursor': 'pointer'}},
                                 'iconStyle': {'position': 'fixed',
                                               'left': '7.5px',
                                               'text-align': 'left'},
                                 'tabStyle': {'list-style-type': 'none',
                                              'margin-bottom': '30px',
                                              'padding-left': '30px'}},
                         key="1")


# --- PAGE 1 ---

if tabs == 'Home':

    # --- HERO ---

    col1, col2 = st.columns([5, 6])
    with col1:
        st.image(profile_pic, width=320)

    with col2:
        st.title(NAME)
        st.info(DESCRIPTION)
        st.download_button(
            label="📝 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )

    # --- SOCIAL LINKS ---

    st.write("#")

    cols = st.columns(len(SOCIALS))
    for index, links in enumerate(SOCIALS):
        cols[index].markdown(links, unsafe_allow_html=True)

    # --- HARD SKILLS ---

    st.write("#")
    st.write("#")
    st.subheader("🛠️ Hard Skills")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<b>Programming</b>", unsafe_allow_html=True)
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
            "![Jupyter Badge](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=fff&style=flat)"
        )

    # --- WORK HISTORY ---

    st.write("#")
    st.write("#")
    st.subheader("💼 Work History")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("<h4>🦊 ShadowFox</h4>", unsafe_allow_html=True)
    with col2:
        st.write("<h4>💡 Prodigy InfoTech</h4>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([7, 2, 7, 2])
    with col1:
        st.write("<h5><b>Python Developer Intern<b></h5>", unsafe_allow_html=True)
        st.write("📅 April '24 - May '24 ")
        st.write("📍 <i>Chennai, Tamil Nadu, India </i><br>&nbsp;&nbsp;&nbsp;<i>(Remote)</i>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <style>
                .vertical-line2 {
                    border-left: 6px solid orange;
                    height: 107px;
                    margin: auto;
                }
            </style>
            """
            , unsafe_allow_html=True
        )
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
                    height: 107px;
                    margin: auto;
                }
            </style>
            """
            , unsafe_allow_html=True
        )
        st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

    # --- EXPERIENCE AND QUALIFICATIONS

    st.write("#")
    st.write("#")
    st.subheader("📖 Education")
    st.write("---")

    st.write("1) **Bachelor of Computer Science**")

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

    st.write("2) **Higher Secondary Education**")

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

    # --- CONNECT WITH ME

    st.write("#")
    st.write("#")
    st.subheader("🔭 Contact Me ")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
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

    # --- FOOTER ---

    st.write("#")
    st.write("#")
    footer_html = """
    <style>
    .footer {
        width: 100%;
        background-color: #262730;
        color: white;
        text-align: center;
        padding: 2px;
    }
    </style>
    <div class="footer">
        <br>
        <p><b>Developed with ❤️ by Kunal Dalvi</b></a></p>
        <p><b>Thank you for visiting!</b></a></p>
    </div>
    """

    with st.container():
        st.markdown(footer_html, unsafe_allow_html=True)


# --- PAGE 2 ----

elif tabs == 'Projects':
    st.title("Paper")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'About':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))

