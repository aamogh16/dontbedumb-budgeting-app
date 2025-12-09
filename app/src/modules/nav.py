import streamlit as st

def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def UserHomeNav():
    st.sidebar.page_link("pages/00_User_Home.py", label="Dashboard", icon="👤")

def BudgetTrackerNav():
    st.sidebar.page_link("pages/10_Budget_Tracker.py", label="Budget Tracker", icon="💰")

def SavingsNav():
    st.sidebar.page_link("pages/12_Savings.py", label="Savings", icon="🎯")

def OtherNav():
    st.sidebar.page_link("pages/13_Other.py", label="Other", icon="📊")

def AIInsightsNav():
    st.sidebar.page_link("pages/20_AI_Insights.py", label="AI Insights", icon="💡")

def UsersPageNav():
    st.sidebar.page_link("pages/30_Users.py", label="Switch User", icon="👥")

def AboutNav():
    st.sidebar.page_link("pages/40_About.py", label="About", icon="ℹ️")

def BackToDashboard():
    col1, col2, col3 = st.columns([1, 1, 6])
    with col1:
        if st.button("← Dashboard", key="back_to_dashboard"):
            st.switch_page('pages/00_User_Home.py')

def SideBarLinks(show_home=False, show_back=True):
    st.sidebar.image("assets/logo.png", width=150)
    
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")
    
    HomeNav()
    
    if st.session_state["authenticated"]:
        UserHomeNav()
        BudgetTrackerNav()
        SavingsNav()
        OtherNav()
        AIInsightsNav()
        UsersPageNav()
        
        if st.session_state.get("role") == "family":
            st.sidebar.page_link("pages/25_Dependents.py", label="Family Members", icon="👨‍👩‍👧‍👦")
    
    AboutNav()
    
    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            del st.session_state["user_id"]
            del st.session_state["first_name"]
            st.switch_page("Home.py")