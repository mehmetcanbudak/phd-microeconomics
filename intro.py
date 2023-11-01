import streamlit as st
from st_pages import Page, add_page_title, show_pages, show_pages_from_config

import src.scripts.plot_themes as thm
import src.scripts.utils as utl

utl.local_css("src/styles/styles_home.css")
utl.external_css(
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
)

st.set_page_config(
    page_title="PhD Microeconomics",
    page_icon="🍎",
    layout="wide",
)

show_pages_from_config()

s1, c1, c2 = utl.wide_col()

# my LinkedIn, GitHub, and email
linkedin_url = "https://www.linkedin.com/in/justinas-grigaitis/"
github_url = "https://github.com/justgri"
email_url = "mailto:justinas.grigaitis@econ.uzh.ch"

# Intro
with c1:
    # Title
    st.title("PhD for All: Microeconomics")

    # Header
    st.markdown(
        '<span style="font-size: 28px; display: block; margin-bottom: 5px;">*Interactive visuals. Rigorous theory. Simple code.*</span>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "<hr style='margin-top: 0; margin-bottom: 5px;'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        r"""Learning and helping others learn along the way.<br>
            Explaining PhD concepts intuitively.<br>
            Procrastinating productively.""",
        unsafe_allow_html=True,
    )
    st.markdown(
        r"""Targeted at **grad students**, but useful for **professionals** and **undergrads** alike.""",
        unsafe_allow_html=True,
    )

    st.markdown("My other Econ PhD apps:")

    but_col1, but_col2, _ = st.columns((1, 1, 2))

    but_col1.link_button(
        "PhD Econometrics",
        "https://phd-econometrics.streamlit.app/",
        type="secondary",
    )

    but_col2.link_button(
        "PhD Macroeconomics",
        "https://phd-macroeconomics.streamlit.app/",
        type="secondary",
    )

    st.markdown(
        f"""
        Please send me feedback:<br>
    <a href="{linkedin_url}" target="_blank">
        <i class="fab fa-linkedin fa-lg"></i>
    </a>
    <a href="{email_url}" target="_blank">
        <i class="fas fa-envelope fa-lg"></i>
    </a>
    <a href="{github_url}" target="_blank">
        <i class="fab fa-github fa-lg"></i>
    </a>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        r"""<u>**Disclaimer:**</u> <br>
        This website does not represent the official curriculum taught at my university. <br>
        My goal is to cover fewer topics in greater depth rather than scratch the surface of many. <br>
        All mistakes are my own.
        """,
        unsafe_allow_html=True,
    )

s1, c2, s2 = utl.narrow_col_intro()

# Textbooks
with c2:
    st.markdown(
        "<h3 style='text-align: center'>Reference Textbooks</h3>",
        unsafe_allow_html=True,
    )

    c2_1, s2_1, c2_2 = st.columns((1, 0.05, 1))

    with c2_1:
        st.image("src/images/intro_MWG.jpg", width=300)

    with c2_2:
        st.image("src/images/intro_osborne_rubinstein.jpg", width=300)


# Other references
with c2:
    st.markdown(
        "<h3 style='text-align: center'>Other References</h3>",
        unsafe_allow_html=True,
    )

    st.link_button(
        "MIT Open Course by Alexander Wolitzky (MIT)",
        "https://ocw.mit.edu/courses/14-121-microeconomic-theory-i-fall-2015/pages/lecture-slides/",
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
        "Lecture Notes by Mark Dean (Columbia)",
        "http://www.columbia.edu/~md3405/Choice_PHD_19.shtml",
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

    st.link_button(
        "Intermediate Microeconomics with Excel by Humberto Barreto (DePauw)",
        "https://socialsci.libretexts.org/Bookshelves/Economics/Intermediate_Microeconomics_with_Excel_(Barreto)",
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
        2. Topic 2 (MWG Chapters) <br>
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
        <b>Section 3: Choice Under Uncertainty</b><br>
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
    Bonus if time permits (it never does) - behavioral economics, stochastic choice.

    """,
            unsafe_allow_html=True,
        )

# Top 10
with c2:
    st.markdown(
        "<h3 style='text-align: center'>10 Tools for Microeconomics</h3>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""This is just a personal attempt - suggestions are more than welcome!<br>
        Limited to PhD Micro I so far.""",
        unsafe_allow_html=True,
    )

    with st.expander("Click to expand", expanded=True):
        st.markdown(
            r"""
        1. **Rational Choice Theory** <br>
        A preference relation $\succeq$ is rational if it's complete and transitive.<br>
        Completeness implies reflexivity. <br>
        
        2. **Utility Representation** <br>
        $u: X \to \mathbb{R}$ represents $\succeq$, if for all $x, y \in X$, $x \succeq y iff u(x) \geq u(y)$ <br>
        $\succeq$ can be represented by $u$ if and only if it is rational. <br>
        If $X = \mathbb{R}^L_+$ and $\succeq$ is rational and continuous, then $\exists u$ (continuous) that represents $\succeq$<br>

        3. **WARP and Axioms $\alpha$ and $\beta$** <br>
        WARP is necessary but not sufficient for rationality. $\alpha$ and $\beta$ together imply WARP and vice-versa. <br>
        WARP: if $x, y \in B_1 \cap B_2$ and if $x \in C(B_1)$, $y \in C(B_2)$, then it must be the case that $x \in C(B_2)$. <br>
        $\alpha$ (aka Independence of Irrelevant Alternatives): if $x$ chosen from a subset, then it must be chosen from the superset.<br>
        $\beta$: if $x, y$ are chosen from a subset and $y$ is chosen from a superset, then $x$ must be chosen from the superset.<br>

        4. **Duality of utility maximization and expenditure minimization** <br>
        If $u$ is continous and represents a locally nonsatiated $\succeq$, then $x^*$ that solves UMP also solves EMP and vice-versa.<br>
        Solving UMP gives the Walrasian (or Marshallian) demand and solving EMP gives the Hicksian demand. <br>
        If $x(p, w)$ is the Walrasian demand function, then:<br>
            &nbsp;&nbsp;&nbsp;&nbsp; i. $p \cdot x(p, w) = w$<br>
            &nbsp;&nbsp;&nbsp;&nbsp; ii. $x(p, w)$ is homogeneous of degree 0 in $(p, w)$ <br>
            &nbsp;&nbsp;&nbsp;&nbsp; iii. If $\succeq$ is convex (so $u$ is quasiconcave), $x(p,w)$ is a convex set. If $\succeq$ is strictly convex (so $u$ is strictly quasiconcave), $x(p,w)$ is single-valued.
                    
        5. **General equilibrium** <br>
        Fundamental Theorems of Welfare Economics:<br>
        &nbsp;&nbsp;&nbsp;&nbsp; First: competitive equilibrium is Pareto-efficient. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; Second: for any Pareto-efficient allocation $(x^*, y^*), \exists p \neq 0$, s.t., $(x^*, y^*, p)$ is a price quasi-equilibrium with transfers.<br>
        Edgeworth box. <br>  
        
        6. **Comparative statics**<br>
        Compensating variation and equivalent variation. <br>
        Consumer surplus. <br>

        7. **Optimization with Lagrange and Kuhn-Tucker** <br>

        8. **Weierstrass Theorem** <br>
        Let $X \subset \mathbb{R}^n$ be compact, and let $f: X \to \mathbb{R}$ be continuous. Then $f$ attains a maximum and a minimum on $X$,<br>
        i.e., there exists points $z_1$, $z_2 \in X$ such that $f(z_1) \leq f(x) \leq f(z_2)$ for all $x \in X$. <br> 

        9. **Choice Under Uncertainty** <br>
        Independence axiom. <br>
        Linearity of vNM expected utility: $U(L)= \sum_{n=1}^N p_n u_n$, where $u_n$ are Bernoulli utilities  <br>
        Certainty equivalent, risk premium, and probability premium.
      
        """,
            unsafe_allow_html=True,
        )
