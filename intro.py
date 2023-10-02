import streamlit as st
from st_pages import Page, add_page_title, show_pages, show_pages_from_config

import src.scripts.plot_themes as thm
import src.scripts.utils as utl

st.set_page_config(
    page_title="PhD Microeconomics",
    page_icon="🍎",
    layout="wide",
)

utl.local_css("src/styles/styles_home.css")
utl.external_css(
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
)

show_pages_from_config()

s1, c1, c2 = utl.wide_col()

# my LinkedIn and GitHub
linkedin_url = "https://www.linkedin.com/in/justinas-grigaitis/"
github_url = "https://github.com/justgri"

# Intro
with c1:
    st.title("Microeconomics for PhD Students")
    st.sidebar.success("Select a page above.")

    st.markdown(
        "Trying to learn and enjoy the first year of Econ PhD. <br> Procrastinating productively. <br> All mistakes are my own.",
        unsafe_allow_html=True,
    )

    st.markdown(
        """**Disclaimer:** <br>
        This website does not represent the official curriculum taught at my university. <br>
        My goal is to master the fundamentals of a few topics rather than scratch the surface of many. <br>
        It might not even look like PhD level stuff, because topics are largely overlapping with the undergraduate course. <br>
        """,
        # Main difference is matrix algebra and proving everything along the way, which might not always be included here.
        # Hopefully it will give insights to both PhD students, undergrads, and others.
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        Please send me comments: 
    <a href="{linkedin_url}" target="_blank">
        <i class="fab fa-linkedin fa-lg"></i>
    </a>
    <a href="{github_url}" target="_blank">
        <i class="fab fa-github fa-lg"></i>
    </a>
    """,
        unsafe_allow_html=True,
    )


s1, c2, s2 = utl.narrow_col()

# Textbooks
with c2:
    st.markdown(
        "<h3 style='text-align: center'>Reference Textbooks</h3>",
        unsafe_allow_html=True,
    )

    c2_1, s2_1, c2_2 = st.columns((1, 0.05, 1))

    with c2_1:
        st.image("src/images/intro_MWG.jpg", width=350)

    with c2_2:
        st.image("src/images/intro_osborne_rubinstein.jpg", width=350)


# Other references
with c2:
    st.markdown(
        "<h3 style='text-align: center'>Other References</h3>",
        unsafe_allow_html=True,
    )

    st.link_button(
        "Lecture Notes by Jonathan Gruber (MIT)",
        "https://ocw.mit.edu/courses/14-01-principles-of-microeconomics-fall-2018/pages/lecture-notes/",
        type="secondary",
    )

    st.link_button(
        "Lecture Notes by Ariel Rubinstein (NYU) (new ed. on his website)",
        "https://arielrubinstein.tau.ac.il/books/PUP2020.pdf",
        type="secondary",
    )

    st.link_button(
        "Rubinstein's website with free most recent textbooks and lecture notes",
        "https://arielrubinstein.org/gt/arielDocs/",
        type="secondary",
    )

    st.link_button(
        "Microeconomic Theory (great for short proofs) YouTube channel by Selcuk Ozyurt (York U)",
        "https://www.youtube.com/@selcukozyurt",
        type="secondary",
    )

    st.link_button(
        "Intermediate Microeconomics YouTube playlist by Robert Townsend (MIT)",
        "https://youtube.com/playlist?list=PLUl4u3cNGP63wnrKge9vllow3Y2OOOKqF&si=OQh7qTNYK2AqG9pl",
        type="secondary",
    )

with c2:
    st.markdown(
        "<h3 style='text-align: center'>What is Microeconomics?</h3>",
        unsafe_allow_html=True,
    )

    rubinstein_public = "https://arielrubinstein.tau.ac.il/books/PUP2020.pdf"

    st.markdown(
        r"""
        "I would like to pause for a moment and alert you to the fact that many economists
            have strong and conflicting views about what economic theory is. Some
            see it as a *set of theories* about the interaction between individuals in
            economic situations, theories that can be tested. Others see it as a *bag
            of tools* to be used by economists. Many see it as a *lens* through which
            academic economists view the world. <br>
            My own view may disappoint those of you who have come to this
            course with practical motives. In my view, economic theory is ”just” an
            arena for the *investigation of concepts* we use in thinking about real-life
            economic situations. What makes a theoretical model into an “economic
            model” is that the concepts are taken from real-life reasoning about economic
            issues. Through the investigation of these concepts, we hope to
            better able to understand reality, and the models provide a language
            that enables us to think about economic interactions in a systematic
            way. However, I do not view economic models as an attempt to describe
            the world, to provide tools for predicting the future or to prescribe how
            people should behave. I object to looking for ultimate truth in economic
            theory, and I do not expect it to be the foundation for any policy recommendations.
            Nothing is “holy” in economic theory – it is the creation
            of people like yourself."
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""Rubinstein, Ariel. *Lecture notes in microeconomic theory: the economic agent*. Princeton University Press, 2012. (free access [link]({rubinstein_public}))""",
        unsafe_allow_html=True,
    )

# Preliminary ToC

with c2:
    st.markdown(
        "<h3 style='text-align: center'>Tentative Table of Contents</h3>",
        unsafe_allow_html=True,
    )

    with st.expander("Click to expand", expanded=False):
        st.write(
            "Chapters follow Mas-Colell, Whinston, Green *Microeconomic Theory* (1995). Chapters from Osborne and Rubinstein *Models in Microeconomic Theory* (2020) are added were relevant."
        )
        st.write(
            "Subsections are likely to change depending on which topics I find most interesting or challenging."
        )

        st.markdown(
            r"""
    <div class="numbered-header">
        <b>Section 1: Preferences and Choice</b><br>
    </div>
        
    <div class="numbered">
        1. Topic 1 (MWG Chapters) <br>
        2. Topic 2 (SMWGLP Chapters) <br>
    </div>

    <br>

    <div class="numbered-header">
        <b>Section 2: Demand Theory</b><br>
    </div>
        
    <div class="numbered">
        3. Topic 3 (MWG Chapters) <br>
        4. Topic 4 (MWG Chapters) <br>
    </div>

    <br>

       <div class="numbered-header">
        <b>Section 3: Choice under Uncertainty</b><br>
    </div>
        
    <div class="numbered">
        5. Topic 5 (MWG Chapters) <br>
        6. Topic 6 (MWG Chapters) <br>
    </div>

    <br>

    
    <div class="numbered-header">
        <b>Section 4: Production</b><br>
    </div>
        
    <div class="numbered">
        7. Topic 7 (MWG Chapters) <br>
        8. Topic 8 (MWG Chapters) <br>
    </div>

    <br>

    <div class="numbered-header">
        <b>Section 5: General Equilibrium</b><br>
    </div>
        
    <div class="numbered">
        9. Topic 9 (MWG Chapters) <br>
        10. Topic 10 (MWG Chapters) <br>
    </div>

    <br>

    Next semester - game theory and market design. <br>
    Bonus if time permits (it never does) - TBD.

    """,
            unsafe_allow_html=True,
        )

# Top 10
with c2:
    st.markdown(
        "<h3 style='text-align: center'>10 Tools for Microeconomics</h3>",
        unsafe_allow_html=True,
    )

    st.write(f"Find a good source for top 10 things to know in microeconomics.")
    st.write(f"Whom to follow on Twitter?")

    with st.expander("Click to expand", expanded=True):
        st.markdown(
            r"""
        1. **Top 1 thing to know** <br>
        Some fancy formula: $E[x] = E[E[x|y]]$ <br>
        
        2. **Top 2 thing to know** <br>
        Some other fancy formula: $E[x] = E[E[x|y]]$ <br>
        
        """,
            unsafe_allow_html=True,
        )
