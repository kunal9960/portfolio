from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Kunal Dalvi"
PAGE_ICON = "assets/favicon.ico"
NAME = "PORTFOLIO WEBSITE"
DESCRIPTION = """ 
Hi! I'm Kunal Dalvi, a Python enthusiast with a keen interest in data analysis. 
I'm driven by curiosity and love taking on new challenges. 
I'm dedicated to unravel insights from complex datasets through statistical methods and programming.
"""

SOCIALS = (
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kunal-dalvi-0b273b2b4)",
    "[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kunald9960@gmail.com)",
    "[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kunal9960)",
    "[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/kunalfr_)&nbsp;",
    "[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/bge3cXHuNC)",
)
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 100px !important;
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
st.write("---")
cols = st.columns(len(SOCIALS))
for index, links in enumerate(SOCIALS):
    cols[index].write(f"{links}")


# --- EXPERIENCE AND QUALIFICATIONS
st.write("#")
st.subheader("🎓 Education")
st.write("---")

st.write("1) **Bachelor of Computer Science**")

col1, col2, col3 = st.columns([4, 21, 3])
with col1:
    st.image("assets/college.png")

with col2:
    st.write(
        """
- **P.E.S. Modern College of Arts, Science and Commerce**
- <i>Pune, Maharashtra, India</i>
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
- <i>Pune, Maharashtra, India</i>
- (2018-2020)
""", unsafe_allow_html=True)
with col3:
    st.write("77.8%")


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 🧑‍💻 Programming : Python, Java, SQL
- 📊 Data Visualisation : MS Excel, Power BI
- 📚 Modeling : Decision Trees, Linear Regression
- 🗄️ Databases : MySQL, MongoDB, Postgres
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")


# --- JOB 1
st.write("🚧", "**Data Analyst Intern**")
st.write("March '24 - April '24 ")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)
