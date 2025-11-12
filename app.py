import streamlit as st
from streamlit_option_menu import option_menu
from resume import resume_analyzer
from assistant import main_app
import base64

if 'intro_shown' not in st.session_state:
    st.session_state.intro_shown = False


def show_intro():
    # Introduction page code (unchanged)
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .intro-container { padding: 1rem; }
        .feature-icon { font-size: 2rem; }
        .intro-title { font-size: 2rem; }
        .intro-subtitle { font-size: 1.25rem; }
        .team-member { margin-bottom: 1rem; }
    }
    .intro-container {
        padding: 2rem;
        background-color: #f0f2f6;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    .feature-icon:hover {
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="intro-container">
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/10349/10349936.png" 
                 style="max-width: 150px; height: auto; margin: 0 auto;"/>
        </div>
        <h1 style="color: #4A90E2; font-size: 2.5rem;">Career Path Oracle 🧙‍♂️</h1>
        <h3 style="color: #333; margin-top: 0.5rem;">Your AI-Powered Career Companion</h3>
        <p style="text-align: center; color: #555;">
            Get personalized career guidance, skill analysis, and job market insights
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")

    # Features row
    st.subheader("What I Can Do For You")
    feature_cols = st.columns(3)
    features = [
        ("📝", "Resume Analysis", "Extract skills and get tailored career suggestions"),
        ("🕵️", "Job Market Insights", "Discover relevant job postings and salary data"),
        ("📚", "Learning Resources", "Get free course recommendations to upskill")
    ]
    
    for idx, (icon, title, desc) in enumerate(features):
        with feature_cols[idx]:
            st.markdown(f"""
            <div style="text-align: center; margin: 1.5rem 0;">
                <span class="feature-icon">{icon}</span>
                <h4>{title}</h4>
                <p style="color: #666; font-size: 0.9rem;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")

    # How it works
    st.subheader("How It Works")
    steps = ["1. Upload/Describe Skills", "2. Get Career Suggestions", 
             "3. Explore Opportunities", "4. Refine Search"]
    step_cols = st.columns(4)
    for idx, step in enumerate(steps):
        with step_cols[idx]:
            st.markdown(f"""
            <div style="text-align: center;">
                <h2 style="color: #4A90E2;">{idx+1}</h2>
                <p>{step}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.write("---")

    # Personal Info Section

    # Load image as base64
    with open("kausar.png", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()

    st.subheader("Developer")
    st.markdown(f"""
    <div style="text-align: center; margin: 2rem 0;">
        <img src="data:image/jpeg;base64,{img_data}" 
            style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%; 
                    margin-bottom: 1rem; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
        <p style="color: #4A90E2;">
            <a href="https://github.com/mohd-ksr" target="_blank" style="text-decoration: none; color: #4A90E2; font-size: 2rem;">
            Mo Kausar
            </a>
        </p>
        <p style="color: #bbb; font-size: 0.9rem;">
            Machine Learning Engineer & Developer<br>
            <code style="background: #222; color: #7CFC00;">ID: 12316343</code>
        </p>
        <p style="max-width: 600px; margin: 0 auto; color: #ccc; font-size: 0.9rem;">
            Hi, I'm <strong>Mo Kausar</strong> — an energetic and innovative 
            <strong>B.Tech Computer Science</strong> student with a strong foundation in programming 
            and machine learning. I’m passionate about solving real-world problems through 
            intelligent, AI-driven solutions and love turning ideas into impactful, user-centered projects. 
            Always eager to learn and contribute to meaningful work leveraging emerging technologies.
        </p>
    </div>
    """, unsafe_allow_html=True)


    st.write("---")
    

    if st.button("Let's Get Started ➡️", use_container_width=True):
        st.session_state.intro_shown = True
        st.rerun()

def main_page():
    st.title("CareerMate🧙‍♂️")

    # Initialize session state (only once)
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = "Bot Assistant"

    with st.sidebar:
        selected = option_menu(
        menu_title=None,
        options=["Bot Assistant", "Resume Analyzer"],
        icons=["robot", "gear"],
        menu_icon="cast",
        default_index=["Bot Assistant", "Resume Analyzer"].index(st.session_state.selected_option),
        orientation="horizontal",
        key="selected_option"  # <- MAGIC: direct bind to session state
        )
        st.write("---")
        st.subheader("About Me")
        st.write("I'm your Career Path adviser CareerMate and Resume Analyzer! You can ask me:")
        st.write("- About myself and how I can help you")
        st.write("- For career path suggestions")
        st.write("- About job market insights")
        st.write("- For learning resources")
        
        st.write("---")
        st.subheader("Example Questions")
        st.write("Try asking:")
        st.write("- What skills do I need for data science?")
        st.write("- What are the best career paths for Python developers?")
        st.write("- How can I transition to AI engineering?")
        st.write("- Make 1 year roadmap for becoming MERN developer")
        
        st.write("---")

    # Show content based on selection
    if st.session_state.selected_option == "Bot Assistant":
        main_app();

    elif st.session_state.selected_option == "Resume Analyzer":
        resume_analyzer();
            

# Main app entry point
if not st.session_state.intro_shown:
    show_intro()
else:
    main_page()
