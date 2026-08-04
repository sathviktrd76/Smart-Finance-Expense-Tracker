# ==========================================================
# Smart Finance Expense Tracker
# Day 1 - Home Page
# ==========================================================

# ----------------------------------------------------------
# Import the Streamlit library
# ----------------------------------------------------------
import streamlit as st

# ----------------------------------------------------------
# Configure the webpage
# ----------------------------------------------------------
st.set_page_config(
    page_title="Smart Finance Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.markdown(
    "<h2 style='text-align:center;'>📋 Navigation</h2>",
    unsafe_allow_html=True
)

st.sidebar.markdown("<p style='font-size:20px;'>🏠 Home</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>💰 Expense Management</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>📊 Analytics</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>💵 Budget Tracker</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>🎯 Savings Tracker</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>📈 Charts</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>💡 Smart Insights</p>", unsafe_allow_html=True)

st.sidebar.divider()

st.sidebar.success("Welcome to Smart Finance Tracker!")

# ==========================================================
# MAIN TITLE
# ==========================================================

st.markdown(
    """
    <h1 style="
        text-align:center;
        font-size:55px;
        color:#1E3A8A;
    ">
        💰 Smart Finance Expense Tracker
    </h1>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# SUBTITLE
# ==========================================================

st.markdown(
    """
    <h3 style="
        text-align:center;
        font-size:28px;
        color:gray;
    ">
        Manage Your Personal Finances Easily
    </h3>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==========================================================
# WELCOME MESSAGE
# ==========================================================

st.markdown(
    """
    <div style="
        font-size:22px;
        line-height:1.8;
        text-align:center;
    ">

    Welcome to your personal finance dashboard. 👋

    This application helps you:

    💰 Track your daily expenses<br>
    📊 Analyze your spending habits<br>
    💵 Manage your monthly budget<br>
    🎯 Monitor your savings goals<br>
    📈 Visualize your expenses using charts

    <br><br>

    <b>Version 1.0</b><br>
    More exciting features will be added throughout this project.

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==========================================================
# FEATURES SECTION
# ==========================================================

st.markdown(
    """
    <h2 style="
        text-align:center;
        font-size:40px;
        color:#1E3A8A;
    ">
        🚀 Features Coming Soon
    </h2>
    """,
    unsafe_allow_html=True
)

features = [
    "➕ Add Expense",
    "📋 View Expenses",
    "✏️ Edit Expense",
    "🗑️ Delete Expense",
    "🔍 Search Expenses",
    "📂 Filter Expenses",
    "💰 Budget Tracker",
    "🎯 Savings Tracker",
    "📊 Analytics Dashboard",
    "📈 Charts",
    "🧠 Smart Insights",
    "📤 Export Data"
]

for feature in features:
    st.markdown(
        f"""
        <div style="
            font-size:22px;
            padding:8px;
            border-radius:8px;
        ">
            {feature}
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:18px;
        color:gray;
    ">
        Developed by <b>Sathvik</b> using Python and Streamlit
    </p>
    """,
    unsafe_allow_html=True
)