import streamlit as st
import time
import streamlit.components.v1 as components

from pathlib import Path
from PIL import Image
from send_email import send_email
from st_on_hover_tabs import on_hover_tabs
from streamlit_extras.let_it_rain import rain
from streamlit_option_menu import option_menu


# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---


def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')


PAGE_TITLE = "Digital CV | Kunal Dalvi"
PAGE_ICON = "assets/favicon.ico"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# This is for scrolling at top
js = ''' 
<script>
    var body = window.parent.document.querySelector(".main"); 
    console.log(body);
    body.scrollTop = 0;
</script>
'''

NAME = "PORTFOLIO WEBSITE"
DESCRIPTION = """ 
Hi! I'm Kunal Dalvi, a Python enthusiast with a keen interest in data analysis. 
I'm driven by curiosity and love taking on new challenges. 
I'm dedicated to unravel insights from complex datasets through statistical methods and programming.
"""


SOCIALS = (
    '<a href="https://www.linkedin.com/in/kunal-dalvi-0b273b2b4"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-linkedin-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
    '<a href="https://twitter.com/kunalfr_"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-twitter-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
    '<a href="https://github.com/kunal9960"><img src="https://raw.githubusercontent.com/kunal9960/kunal9960/main/github.png" width="62"/></a>',
    '<a href="mailto:kunald9960@gmail.com"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-gmail-social-media-justicon-lineal-color-justicon.png" width="60"/></a>',
    '<a href="https://discord.gg/bge3cXHuNC" class="no-margin"><img src="https://img.icons8.com/external-justicon-lineal-color-justicon/344/external-discord-social-media-justicon-lineal-color-justicon.png" width="60"/></a>'
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
                         key="1", default_choice=0)


# --- PAGE 1 ---

if tabs == 'Home':
    temp = st.empty()
    with temp:
        st.components.v1.html(js)
        time.sleep(.1)
    temp.empty()
    st.markdown(
        """
        <script>
            window.onload = function() {
                setTimeout(function() {
                    window.scrollTo(0, 0);
                }, 100);
            }
        </script>
        """,
        unsafe_allow_html=True
    )

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

    V_SPACE(1)
    socials_html = ''.join(SOCIALS)

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

    # --- HARD SKILLS ---

    V_SPACE(1)
    V_SPACE(1)
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

    V_SPACE(1)
    V_SPACE(1)
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

    # --- CONNECT WITH ME

    V_SPACE(1)
    V_SPACE(1)
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
        st.markdown("[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F&label=WEBSITE%20VIEWS&labelColor=%23333333&countColor=%23cbc3e3&labelStyle=upper)](https://visitorbadge.io/status?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F)")


# --- PAGE 2 ---

if tabs == 'Projects':
    temp = st.empty()
    with temp:
        st.components.v1.html(js)
        time.sleep(.1)
    temp.empty()

    st.markdown("<h1  style='text-align: center;'>🚀 My Project Showcase</h1>", unsafe_allow_html=True)
    V_SPACE(1)
    selected = option_menu(None, ["Python Projects", "Data Science", 'AI/ ML Projects'],
                           icons=['filetype-py', 'clipboard-data-fill', "robot"],
                           menu_icon="cast", default_index=0, orientation="horizontal",
                           styles={
                               "container": {"padding": "0!important", "background-color": "#111111"},
                               "icon": {"color": "#CBC3E3", "font-size": "17px"},
                               "nav-link": {"font-family": "consolas", "font-size": "17px", "text-align": "left",
                                            "margin": "0px",
                                            "--hover-color": "#555"},
                               "nav-link-selected": {"font-family": "consolas", "background-color": "#333333",
                                                     "font-size": "17px", "font-weight": "normal",
                                                     "border": "0.5px solid white"},
                           })

    if selected == "Python Projects":

        animation_css = """
                <style>
                    @keyframes fadeIn {
                        from {
                            opacity: 0;
                        }
                        to {
                            opacity: 1;
                        }
                    }
                
                    .project-card {
                        animation: fadeIn 0.5s ease-in-out;
                    }
                </style>

            """

        st.markdown(animation_css, unsafe_allow_html=True)

        css = """
                <style>
                    .project-card {
                        border: 2px solid;
                        border-radius: 15px;
                        padding: 10px;
                        transition: transform 0.3s ease-in-out;
                        margin-bottom: 20px;
                    }
                    .project-card:hover {
                        transform: scale(1.05);
                    }
                </style>
                """

        st.markdown(css, unsafe_allow_html=True)

        project_details = [
            {"name": "Positive News API",
             "description": "This Python script fetches the latest news articles from TechCrunch using the News API and sends them via email.",
             "image": "https://raw.githubusercontent.com/kunal9960/positive-news-api/master/Example.png",
             "github_link": "https://github.com/kunal9960/positive-news-api",
             "height": 152},
            {"name": "Invoice Generator",
             "description": "Automate PDF invoice generation from Excel files with ease using pandas and fpdf libraries in Python.",
             "image": "https://raw.githubusercontent.com/kunal9960/invoice-generator/master/Example.png",
             "github_link": "https://github.com/kunal9960/invoice-generator",
             "height": 152},
            {"name": "PDF Template",
             "description": "Generate PDF documents from CSV data using Python with Pandas and FPDF.",
             "image": "https://raw.githubusercontent.com/kunal9960/pdf-template/master/Image.png",
             "github_link": "https://github.com/kunal9960/pdf-template",
             "height": 170},
            {"name": "Todo-App (GUI)",
             "description": "A task management tool offering both GUI and CLI functionality.",
             "image": "https://raw.githubusercontent.com/kunal9960/todo-gui-app/master/Todo%20GUI.png",
             "github_link": "https://github.com/kunal9960/todo-gui-app",
             "height": 170},

        ]

        with st.container():
            col1, col2 = st.columns(2)

            for i, project in enumerate(project_details):
                project_name = project["name"]
                project_description = project["description"]
                project_image = project["image"]
                project_github_link = project["github_link"]
                project_height = project["height"]

                if i % 2 == 0:
                    column = col1
                else:
                    column = col2

                with column:
                    st.markdown(
                        f"""
                            <div style="border: 2px solid; border-radius: 15px; padding: 10px;" class="project-card">
                                <img src="{project_image}" width="{320}" height="{project_height}">
                                <h3>{project_name}</h3>
                                <p>{project_description}</p>
                                <a href="{project_github_link}" target="_blank">
                                    <img src="https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue?logo=github">
                                </a>
                            </div>
                            """,
                        unsafe_allow_html=True
                    )

    if selected == "Data Science":
        animation_css2 = """
                        <style>
                            @keyframes fadeIn {
                                from {
                                    opacity: 0;
                                }
                                to {
                                    opacity: 1;
                                }
                            }

                            .project-card2 {
                                animation: fadeIn 0.6s ease-in-out;
                            }
                        </style>

                    """

        st.markdown(animation_css2, unsafe_allow_html=True)

        css2 = """
                <style>
                    .project-card2 {
                        border: 2px solid;
                        border-radius: 15px;
                        padding: 10px;
                        transition: transform 0.3s ease-in-out;
                        margin-bottom: 20px;
                    }
                    .project-card2:hover {
                        transform: scale(1.05);
                    }
                </style>
                """

        st.markdown(css2, unsafe_allow_html=True)

        project_details = [
            {"name": "Store Data Analysis",
             "description": "Excel-based store data analysis tool harnessing advanced features for insights and business optimization.",
             "image": "https://raw.githubusercontent.com/kunal9960/store-data-analysis/main/Dashboard.png",
             "github_link": "https://github.com/kunal9960/store-data-analysis",
             "height": 152},
            {"name": "Sales Dashboard Excel",
             "description": "Excel-based sales analysis tool offering insights into performance, product trends and revenue maximization",
             "image": "https://raw.githubusercontent.com/kunal9960/sales-dashboard-excel/main/Dashboard.png",
             "github_link": "https://github.com/kunal9960/sales-dashboard-excel",
             "height": 152},
            {"name": "Road Accident Data Analysis",
             "description": "Excel-based road accident analysis tool providing insights on trends, contributing factors, and interventions to enhance road safety.",
             "image": "https://raw.githubusercontent.com/kunal9960/accidents-data-analysis/main/Dashboard.png",
             "github_link": "https://github.com/kunal9960/accidents-data-analysis",
             "height": 160},
            {"name": "Titanic dataset Analysis",
             "description": "This script uses the Titanic dataset, detailing passenger information such as age, gender, class, fare, and survival status.",
             "image": "https://raw.githubusercontent.com/kunal9960/PRODIGY_DS_02/master/Gender.png",
             "github_link": "https://github.com/kunal9960/PRODIGY_DS_02",
             "height": 160},
        ]

        with st.container():
            col1, col2 = st.columns(2)

            for i, project in enumerate(project_details):
                project_name = project["name"]
                project_description = project["description"]
                project_image = project["image"]
                project_github_link = project["github_link"]
                project_height = project["height"]

                if i % 2 == 0:
                    column = col1
                else:
                    column = col2

                with column:
                    st.markdown(
                        f"""
                            <div style="border: 2px solid; border-radius: 15px; padding: 10px;" class="project-card2">
                                <img src="{project_image}" width="{320}" height="{project_height}">
                                <h3>{project_name}</h3>
                                <p>{project_description}</p>
                                <a href="{project_github_link}" target="_blank">
                                    <img src="https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue?logo=github">
                                </a>
                            </div>
                            """,
                        unsafe_allow_html=True
                    )

    if selected == "AI/ ML Projects":
        animation_css3 = """
                        <style>
                            @keyframes fadeIn {
                                from {
                                    opacity: 0;
                                }
                                to {
                                    opacity: 1;
                                }
                            }

                            .project-card3 {
                                animation: fadeIn 0.6s ease-in-out;
                            }
                        </style>

                    """

        st.markdown(animation_css3, unsafe_allow_html=True)

        css2 = """
                <style>
                    .project-card3 {
                        border: 2px solid;
                        border-radius: 15px;
                        padding: 10px;
                        transition: transform 0.3s ease-in-out;
                        margin-bottom: 20px;
                    }
                    .project-card3:hover {
                        transform: scale(1.05);
                    }
                </style>
                """

        st.markdown(css2, unsafe_allow_html=True)

        project_details = [
            {"name": "Positive News API",
             "description": "This Python script fetches the latest news articles from TechCrunch using the News API and sends them via email.",
             "image": "https://raw.githubusercontent.com/kunal9960/positive-news-api/master/Example.png",
             "github_link": "https://github.com/kunal9960/positive-news-api",
             "height": 152},
            {"name": "Invoice Generator",
             "description": "Automate PDF invoice generation from Excel files with ease using pandas and fpdf libraries in Python.",
             "image": "https://raw.githubusercontent.com/kunal9960/invoice-generator/master/Example.png",
             "github_link": "https://github.com/kunal9960/invoice-generator",
             "height": 152},
        ]

        with st.container():
            col1, col2 = st.columns(2)

            for i, project in enumerate(project_details):
                project_name = project["name"]
                project_description = project["description"]
                project_image = project["image"]
                project_github_link = project["github_link"]
                project_height = project["height"]

                if i % 2 == 0:
                    column = col1
                else:
                    column = col2

                with column:
                    st.markdown(
                        f"""
                            <div style="border: 2px solid; border-radius: 15px; padding: 10px;" class="project-card3">
                                <img src="{project_image}" width="{320}" height="{project_height}">
                                <h3>{project_name}</h3>
                                <p>{project_description}</p>
                                <a href="{project_github_link}" target="_blank">
                                    <img src="https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue?logo=github">
                                </a>
                            </div>
                            """,
                        unsafe_allow_html=True
                    )


# --- PAGE 3 ---

if tabs == 'About':

    temp = st.empty()
    with temp:
        st.components.v1.html(js)
        time.sleep(.1)
    temp.empty()

    rain(
        emoji="😊",
        font_size=40,
        falling_speed=3,
        animation_length="5s",
    )

    st.title("Thank you for visiting")
    st.header("🧪 Insights")

    st.markdown(
        "[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F&label=WEBSITE%20VIEWS&countColor=%232ccce4&labelStyle=upper)](https://visitorbadge.io/status?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F)" +
        " [![Uptime Monitoring Badge](https://img.shields.io/badge/Uptime-100%25-brightgreen?style=for-the-badge)](https://portfolio-kunal.streamlit.app/)" +
        " [![Open Issues](https://img.shields.io/badge/Open%20Issues-3-red?style=for-the-badge)](https://github.com/kunal9960)" +
        " [![Last Commit](https://img.shields.io/github/last-commit/kunal9960/portfolio?style=for-the-badge&color=yellow)](https://github.com/kunal9960/portfolio/commits)")

    import streamlit as st


    def generate_animating_bar(language, percentage):
        bar_html = f"""
        <style>
          .container {{
            width: 96%;
            height: 30px;
            background-color: #f3f3f3;
            position: relative;
            overflow: hidden;
          }}

          .bar {{
            width: {percentage}%;
            height: 100%;
            background-color: #BF40BF;
            position: absolute;
            animation: progress {percentage / 100}s linear forwards;
          }}

          .bar-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-weight: bold;
          }}

          @keyframes progress {{
            0% {{
              width: 0%;
            }}
            100% {{
              width: {percentage}%;
            }}
          }}
        </style>

        <div class="container">
          <div class="bar"></div>
          <div class="bar-text">{percentage}%</div>
        </div>
        """
        return bar_html


    st.markdown(
        "## Languages Used&nbsp;" + "[![Streamlit](https://img.shields.io/badge/Streamlit-1.33.0-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)",
        unsafe_allow_html=True)

    # Define the columns
    col1, col2 = st.columns([1, 7])

    # Display Python logo in first column
    with col1:
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg", width=80)

    # Display animating bar in second column
    with col2:
        st.markdown("[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)")
        st.markdown(generate_animating_bar("Python", 80), unsafe_allow_html=True)


    def generate_animating_bar_css(percentage):
        bar_html = f"""
        <style>
          .container-css {{
            width: 96%;
            height: 30px;
            background-color: #f3f3f3;
            position: relative;
            overflow: hidden;
          }}

          .bar-css {{
            width: {percentage}%;
            height: 100%;
            background-color: #BF40BF;
            position: absolute;
            animation: progress-css {percentage / 100}s linear forwards;
          }}

          .bar-text-css {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-weight: bold;
          }}

          @keyframes progress-css {{
            0% {{
              width: 0%;
            }}
            100% {{
              width: {percentage}%;
            }}
          }}
        </style>

        <div class="container-css">
          <div class="bar-css"></div>
          <div class="bar-text-css">{percentage}%</div>
        </div>
        """
        return bar_html


    # Define the columns
    col1, col2 = st.columns([1, 7])

    # Display CSS logo in first column
    with col1:
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg",
                 width=80)

    # Display animating bar for CSS in second column
    with col2:
        st.markdown(
            "[![CSS](https://img.shields.io/badge/CSS-15%25-1572B6.svg?style=flat&logo=CSS3&logoColor=white)](https://www.w3.org/Style/CSS/Overview.en.html)")
        st.markdown(generate_animating_bar_css(15), unsafe_allow_html=True)
