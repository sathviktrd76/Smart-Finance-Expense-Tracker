# ==========================================================
# Smart Finance Expense Tracker
# Day 1 - Home Page
# ==========================================================

# ----------------------------------------------------------
# Import the Streamlit library
# ----------------------------------------------------------
import streamlit as st

#-----------------------------------------------------------
# Import csv 
#-----------------------------------------------------------
import csv  # comma seperated values. It is a simple text file used to store data in a table format.

#-----------------------------------------------------------
#Import os #os stands for operating system
#-----------------------------------------------------------
import os #lets python interact with your operating system

# ----------------------------------------------------------
# Configure the webpage
# ----------------------------------------------------------
st.set_page_config(
    page_title="Smart Finance Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# ==========================================================
# CREATE CSV FILE IF IT DOESN'T EXIST
# ==========================================================

if not os.path.isfile("expenses.csv"): #path is location of file

    with open("expenses.csv", "w", newline="") as file: #open the file expenses.csv in write mode and call it file

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Category",
            "Amount",
            "Description"
        ]) #csv becomes Date,Category,Amount,Description




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

st.sidebar.markdown("<p style='font-size:20px;'>📄 Monthly Report</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>⚙️ Settings</p>", unsafe_allow_html=True)
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

#------------------------------------------------------------
# ADD NEW EXPENSE
#------------------------------------------------------------
st.markdown(
    """
    <h2 style="
        text-align:center;
        font-size:40px;
        color:#1E3A8A;
    ">
        ➕ Add New Expense
    </h2>
    """,
    unsafe_allow_html=True
)

#---------------------------------------------------------------
# DATE
#---------------------------------------------------------------
st.markdown(
    """
    <p style="
        font-size:22px;
        font-weight:bold;
        color:#1E3A8A;
    ">
        📅 Select Date
    </p>
    """,
    unsafe_allow_html=True
)

expense_date = st.date_input(
    "",
    label_visibility="collapsed"
)

#------------------------------------------------------------------
# CATEGORY
#------------------------------------------------------------------

st.markdown(
    """
    <p style="
        font-size:22px;
        font-weight:bold;
        color:#1E3A8A;
    ">
        📂 Select Category
    </p>
    """,
    unsafe_allow_html=True
)

expense_category = st.selectbox(
    "",
    [
        "Food",
        "Travel",
        "Shopping",
        "Entertainment",
        "Education",
        "Health",
        "Bills",
        "Other"
    ],
    label_visibility="collapsed"
)

#-------------------------------------------------------------------
# AMOUNT
#-------------------------------------------------------------------
st.markdown(
    """
    <p style="
        font-size:22px;
        font-weight:bold;
        color:#1E3A8A;
    ">
        💰 Enter Amount
    </p>
    """,
    unsafe_allow_html=True
)

expense_amount = st.number_input(
    "",
    min_value=0.0,
    step=1.0,
    label_visibility="collapsed"
)

#---------------------------------------------------------------------------
# DESCRIPTION
#---------------------------------------------------------------------------

st.markdown(
    """
    <p style="
        font-size:22px;
        font-weight:bold;
        color:#1E3A8A;
    ">
        📝 Expense Description
    </p>
    """,
    unsafe_allow_html=True
)

expense_description = st.text_area(
    "",
    placeholder="Enter a short description of the expense...",
    label_visibility="collapsed"
)

st.divider()

#----------------------------------------------------------------------------
# BUTTON
#----------------------------------------------------------------------------

if st.button("➕ Add Expense"):

    with open("expenses.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            expense_date,
            expense_category,
            expense_amount,
            expense_description
        ])

    st.success("✅ Expense Added Successfully!")

#----------------------------------------------------------------------
# Append "a" adds new data at the end without deleting existing data
# Write "w" creates a new file or overwrite an existing one
#-----------------------------------------------------------------------

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