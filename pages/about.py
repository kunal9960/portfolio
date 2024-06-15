import streamlit as st
from streamlit_extras.let_it_rain import rain


def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def about():
    rain(
        emoji="😊",
        font_size=40,
        falling_speed=3,
        animation_length="5s",
    )

    typing_svg_link = "https://readme-typing-svg.herokuapp.com?font=Inconsolata&weight=600&size=39&duration=4000&pause=200&color=F7F7F7&random=false&width=435&lines=THANK+YOU+FOR+VISITING"
    typing_svg_markdown = f"[![Typing SVG]({typing_svg_link})](https://git.io/typing-svg)"
    st.markdown(typing_svg_markdown, unsafe_allow_html=True)
    st.info("Most of this website is built using Python, one of the known issues is that "
            "this isn't an android/ IOS friendly website because of the streamlit limitations.", icon="ℹ️")

    V_SPACE(1)

    st.subheader("🧪 Some Insights")
    st.write("---")
    st.markdown(
        " [![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F&label=WEBSITE%20VIEWS&countColor=%232ccce4&labelStyle=upper)](https://visitorbadge.io/status?path=https%3A%2F%2Fportfolio-kunal.streamlit.app%2F)" +
        " [![Uptime Monitoring Badge](https://img.shields.io/badge/Uptime-100%25-brightgreen?style=for-the-badge)](https://portfolio-kunal.streamlit.app/)" +
        " [![Open Issues](https://img.shields.io/badge/Open%20Issues-3-red?style=for-the-badge)](https://github.com/kunal9960)" +
        " [![Last Commit](https://img.shields.io/github/last-commit/kunal9960/portfolio?style=for-the-badge&color=yellow)](https://github.com/kunal9960/portfolio/commits)")

    V_SPACE(1)

    def generate_combined_progress_bar(python_percentage, css_percentage, html_percentage):
        bar_html = f"""
            <div style="width: 96%; height: 25px; background-color: #f3f3f3; margin-bottom: 10px; position: relative; border: 2px solid black;">
                <div style="width: {python_percentage}%; height: 100%; background-color: #8a2be2; position: absolute; top: 0; left: 0;">
                    <span style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-weight: bold;">{python_percentage}%</span>
                </div>
                <div style="width: {css_percentage}%; height: 100%; background-color: #1572B6; position: absolute; top: 0; left: {python_percentage}%; border-left: 2px solid black;">
                    <span style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-weight: bold;">{css_percentage}%</span>
                </div>
                <div style="width: {html_percentage + 1}%; height: 100%; background-color: #E34F26; position: absolute; top: 0; left: {python_percentage + css_percentage}%; border-left: 2px solid black;">
                    <span style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-weight: bold;">{html_percentage}%</span>
                </div>
            </div>
            """
        return bar_html

    st.subheader("✍ Languages Used")
    st.write("---")
    col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 1, 2, 1, 2])

    with col1:
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg", width=70)
    with col2:
        V_SPACE(1)
        st.markdown(
            "[![Python](https://img.shields.io/badge/Python-3.12-8a2be2.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)")

    with col3:
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg",
                 width=68)
    with col4:
        V_SPACE(1)
        st.markdown(
            "[![CSS](https://img.shields.io/badge/CSS-3.0-1572B6.svg?style=flat&logo=CSS3&logoColor=white)](https://www.w3.org/Style/CSS/Overview.en.html)")

    with col5:
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg",
                 width=68)
    with col6:
        V_SPACE(1)
        st.markdown(
            "[![HTML](https://img.shields.io/badge/HTML-5.0-E34F26.svg?style=flat&logo=html5&logoColor=white)](https://www.w3.org/TR/html52/)")

    col4 = st.columns(1)[0]

    with col4:
        st.markdown(generate_combined_progress_bar(70, 20, 10), unsafe_allow_html=True)

    V_SPACE(1)
    st.subheader("📌 Resources Used")
    st.write("---")

    youtube_video_urls = [
        "https://www.youtube.com/embed/hEPoto5xp3k",
        "https://www.youtube.com/embed/RW8b-lxCm_8"
    ]

    youtube_embed_codes = [
        f'<iframe width="100%" height="315" src="{url}" frameborder="0" allowfullscreen></iframe>'
        for url in youtube_video_urls
    ]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(youtube_embed_codes[0], unsafe_allow_html=True)

    with col2:
        st.markdown(youtube_embed_codes[1], unsafe_allow_html=True)

    github_logo = '<a href="https://github.com/kunal9960"><img src="https://raw.githubusercontent.com/kunal9960/kunal9960/main/github.png" width="120"/></a>'

    repo_links = {
        "Let it Rain": "https://arnaudmiribel.github.io/streamlit-extras/extras/let_it_rain/",
        "Streamlit on Hover Tabs": "https://github.com/Socvest/streamlit-on-Hover-tabs",
        "Streamlit Option Menu": "https://github.com/victoryhb/streamlit-option-menu",
        "Bootstrap Carousal": "https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
        "Streamlit Extras": "https://github.com/arnaudmiribel/streamlit-extras"
    }

    streamlit_logo = '<a href="https://streamlit.io"><img src="https://raw.githubusercontent.com/github/explore/968d1eb8fb6b704c6be917f0000283face4f33ee/topics/streamlit/streamlit.png" width="120"/></a>'
    streamlit_links = {
        "Empty Spaces": "https://discuss.streamlit.io/t/create-empty-space-to-separate-portions-of-the-app/8689",
        "Animations": "https://discuss.streamlit.io/t/how-to-plot-a-matplotlib-animation-in-my-streamlit-app/22764",
        "Streamlit API Reference": "https://docs.streamlit.io/develop/api-reference/layout",
        "Navigation Bar": "https://discuss.streamlit.io/t/new-component-streamlit-navigation-bar/66032",
        "Components": "https://docs.streamlit.io/develop/concepts/custom-components/create"
    }

    col5, col6 = st.columns(2)
    col1, col2, col8, col3, col4, = st.columns([3, 3, 1, 3, 2])

    with col5:
        st.write("<h4>🔗 Github Repo</h4>", unsafe_allow_html=True)
        with col1:
            st.markdown(github_logo, unsafe_allow_html=True)

        with col2:
            for repo_name, repo_link in repo_links.items():
                st.markdown(f"**[{repo_name}]({repo_link})**")

        with col8:
            st.markdown(
                """
                <style>
                    .vertical-line {
                        border-left: 6px solid #CBC3E3;
                        height: 230px;
                        margin: auto;
                    }
                </style>
                """, unsafe_allow_html=True
            )
            st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

    with col6:
        st.write("<h4>🔗 Streamlit</h4>", unsafe_allow_html=True)
        with col3:
            st.markdown(streamlit_logo, unsafe_allow_html=True)

        with col4:
            for link_name, link_url in streamlit_links.items():
                st.markdown(f"**[{link_name}]({link_url})**")