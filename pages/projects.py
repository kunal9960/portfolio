import streamlit as st
from streamlit_option_menu import option_menu


def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')


def projects():
    st.markdown("<h1  style='text-align: center;'>🚀 PROJECT SHOWCASE</h1>", unsafe_allow_html=True)
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