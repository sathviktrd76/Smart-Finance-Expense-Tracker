# ==========================================================
# SMART FINANCE EXPENSE TRACKER
# ==========================================================
# Personal Finance Management Application
# Built using Python, Streamlit and Pandas
# ==========================================================


# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import streamlit as st
import pandas as pd
import csv
import os


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Smart Finance Expense Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GENERAL PAGE
    ====================================================== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }


    /* ======================================================
       SIDEBAR
    ====================================================== */

    section[data-testid="stSidebar"] {
        min-width: 320px !important;
        max-width: 320px !important;
    }

    section[data-testid="stSidebar"] h2 {
        font-size: 32px !important;
        font-weight: 700 !important;
    }


    /* Navigation text */

    section[data-testid="stSidebar"]
    [data-testid="stRadio"] label p {
        font-size: 20px !important;
        line-height: 1.5 !important;
    }


    /* Navigation spacing */

    section[data-testid="stSidebar"]
    [data-testid="stRadio"] > div {
        gap: 14px !important;
    }

    section[data-testid="stSidebar"]
    [data-testid="stRadio"] label {
        padding: 6px 0 !important;
    }


    /* ======================================================
       INPUT BOXES
    ====================================================== */

    /* Text input */

    div[data-testid="stTextInput"] input {
        font-size: 20px !important;
        min-height: 50px !important;
        padding: 10px 14px !important;
    }


    /* Number input */

    div[data-testid="stNumberInput"] input {
        font-size: 20px !important;
        min-height: 50px !important;
        padding: 10px 14px !important;
    }


    /* Selectbox */

    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] {
        min-height: 50px !important;
    }

    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] * {
        font-size: 20px !important;
    }


    /* Date input */

    div[data-testid="stDateInput"] input {
        font-size: 20px !important;
        min-height: 50px !important;
        padding: 10px 14px !important;
    }


    /* Text area */

    div[data-testid="stTextArea"] textarea {
        font-size: 20px !important;
        min-height: 120px !important;
        padding: 12px 14px !important;
    }


    /* ======================================================
       INPUT LABELS
    ====================================================== */

    div[data-testid="stTextInput"] label p,
    div[data-testid="stNumberInput"] label p,
    div[data-testid="stSelectbox"] label p,
    div[data-testid="stDateInput"] label p,
    div[data-testid="stTextArea"] label p {
        font-size: 19px !important;
        font-weight: 600 !important;
    }


    /* ======================================================
       BUTTONS
    ====================================================== */

    div.stButton > button {
        width: 100% !important;
        min-height: 62px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        padding: 14px 24px !important;
        border-radius: 10px !important;
    }


    /* Form submit buttons */

    div[data-testid="stFormSubmitButton"] > button {
        width: 100% !important;
        min-height: 62px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        padding: 14px 24px !important;
        border-radius: 10px !important;
    }


    /* ======================================================
       EXPENSE TABLE
    ====================================================== */

    div[data-testid="stDataFrame"] {
        border-radius: 10px;
    }

    div[data-testid="stDataFrame"]
    [role="columnheader"] {
        font-size: 18px !important;
        font-weight: 700 !important;
    }

    div[data-testid="stDataFrame"]
    [role="gridcell"] {
        font-size: 17px !important;
    }


    /* ======================================================
       METRICS
    ====================================================== */

    div[data-testid="stMetric"] {
        padding: 10px;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 18px !important;
    }

    div[data-testid="stMetricValue"] {
        font-size: 28px !important;
    }


    /* ======================================================
       FOOTER
    ====================================================== */

    .footer {
        text-align: center;
        color: #6B7280;
        font-size: 18px;
        padding-top: 25px;
        padding-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# CONSTANTS
# ==========================================================

CSV_FILE = "expenses.csv"

CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Entertainment",
    "Education",
    "Health",
    "Bills",
    "Other"
]

DEFAULT_MAX_AMOUNT = 10000000.0


# ==========================================================
# CREATE CSV FILE IF IT DOES NOT EXIST
# ==========================================================

if not os.path.isfile(CSV_FILE):

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Category",
            "Amount",
            "Description"
        ])


# ==========================================================
# LOAD EXPENSES
# ==========================================================

def load_expenses():

    try:

        expenses = pd.read_csv(CSV_FILE)

    except (pd.errors.EmptyDataError, FileNotFoundError):

        expenses = pd.DataFrame(
            columns=[
                "Date",
                "Category",
                "Amount",
                "Description"
            ]
        )


    # Ensure required columns exist

    required_columns = [
        "Date",
        "Category",
        "Amount",
        "Description"
    ]

    for column in required_columns:

        if column not in expenses.columns:

            expenses[column] = ""


    # Convert date

    expenses["Date"] = pd.to_datetime(
        expenses["Date"],
        errors="coerce"
    )


    # Convert amount

    expenses["Amount"] = pd.to_numeric(
        expenses["Amount"],
        errors="coerce"
    )


    # Remove invalid records

    expenses = expenses.dropna(
        subset=["Date", "Amount"]
    )


    # Clean category

    expenses["Category"] = (
        expenses["Category"]
        .fillna("")
        .astype(str)
        .str.strip()
    )


    # Clean description

    expenses["Description"] = (
        expenses["Description"]
        .fillna("")
        .astype(str)
        .str.strip()
    )


    return expenses


# ==========================================================
# SAVE EXPENSE
# ==========================================================

def save_expense(
    expense_date,
    expense_category,
    expense_amount,
    expense_description
):

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            expense_date,
            expense_category,
            expense_amount,
            expense_description
        ])


# ==========================================================
# INDIAN CURRENCY FORMATTER
# ==========================================================

def format_indian_currency(amount):

    amount = float(amount)

    formatted = f"{amount:.2f}"

    integer_part, decimal_part = formatted.split(".")

    if len(integer_part) <= 3:

        formatted_integer = integer_part

    else:

        last_three = integer_part[-3:]

        remaining = integer_part[:-3]

        groups = []

        while len(remaining) > 2:

            groups.insert(
                0,
                remaining[-2:]
            )

            remaining = remaining[:-2]

        if remaining:

            groups.insert(
                0,
                remaining
            )

        formatted_integer = (
            ",".join(groups)
            + ","
            + last_three
        )

    return f"₹{formatted_integer}.{decimal_part}"


# ==========================================================
# LOAD DATA
# ==========================================================

expenses = load_expenses()


# ==========================================================
# DEFAULT DATE
# ==========================================================

if expenses.empty:

    earliest_date = pd.Timestamp.today().date()

else:

    earliest_date = expenses["Date"].min().date()


# ==========================================================
# RESET FILTERS
# ==========================================================

def reset_filters():

    st.session_state["search_filter"] = ""

    st.session_state["category_filter"] = (
        "All Categories"
    )

    st.session_state["start_date_filter"] = (
        earliest_date
    )

    st.session_state["end_date_filter"] = (
        pd.Timestamp.today().date()
    )

    st.session_state["minimum_amount_filter"] = 0.0

    st.session_state["maximum_amount_filter"] = (
        DEFAULT_MAX_AMOUNT
    )

    st.session_state["sort_filter"] = "Default"


# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================

st.sidebar.markdown(
    """
    <h2 style="
        text-align:center;
        font-size:32px;
        color:#1E3A8A;
        margin-bottom:20px;
    ">
        📋 Navigation
    </h2>
    """,
    unsafe_allow_html=True
)


selected_page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💰 Expense Management",
        "📊 Analytics",
        "💵 Budget Tracker",
        "🎯 Savings Tracker",
        "📈 Charts",
        "💡 Smart Insights",
        "📄 Monthly Report",
        "⚙️ Settings"
    ],
    label_visibility="collapsed",
    key="navigation"
)


st.sidebar.divider()


st.sidebar.success(
    "Welcome to Smart Finance Tracker!"
)


# ==========================================================
# HOME PAGE
# ==========================================================

if selected_page == "🏠 Home":

    # ======================================================
    # PAGE TITLE
    # ======================================================

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-size:55px;
            color:#1E3A8A;
            margin-top:10px;
            margin-bottom:10px;
            font-weight:700;
        ">
            💰 Smart Finance Expense Tracker
        </h1>
        """,
        unsafe_allow_html=True
    )


    # ======================================================
    # PAGE DESCRIPTION
    # ======================================================

    st.markdown(
        """
        <p style="
            text-align:center;
            font-size:25px;
            color:#666666;
            margin-top:0px;
            margin-bottom:25px;
        ">
            Manage your personal finances easily,
            intelligently and efficiently.
        </p>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    # ======================================================
    # DASHBOARD SUMMARY
    # ======================================================

    total_expenses = len(expenses)

    total_spending = expenses["Amount"].sum()

    average_expense = (
        expenses["Amount"].mean()
        if not expenses.empty
        else 0
    )

    highest_expense = (
        expenses["Amount"].max()
        if not expenses.empty
        else 0
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "📋 Total Expenses",
            total_expenses
        )


    with col2:

        st.metric(
            "💰 Total Spending",
            format_indian_currency(total_spending)
        )


    with col3:

        st.metric(
            "📊 Average Expense",
            format_indian_currency(average_expense)
        )


    with col4:

        st.metric(
            "🔝 Highest Expense",
            format_indian_currency(highest_expense)
        )


    st.divider()


    # ======================================================
    # WELCOME SECTION
    # ======================================================

    st.markdown(
        """
        <h2 style="
            text-align:center;
            font-size:40px;
            color:#1E3A8A;
            margin-bottom:10px;
        ">
            👋 Welcome!
        </h2>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <p style="
            text-align:center;
            font-size:22px;
            color:#555555;
            line-height:1.7;
            margin-bottom:20px;
        ">
            Smart Finance Expense Tracker is a personal finance
            management application built using
            <b>Python, Streamlit and Pandas</b>.
            <br>
            Track expenses, understand spending patterns,
            and make better financial decisions.
        </p>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    # ======================================================
    # AVAILABLE + UPCOMING FEATURES
    # ======================================================

    col1, col2 = st.columns(2)


    # ======================================================
    # AVAILABLE FEATURES
    # ======================================================

    with col1:

        st.markdown(
            """
            <h2 style="
                font-size:38px;
                color:#1E3A8A;
                margin-bottom:15px;
            ">
                🚀 Available Features
            </h2>
            """,
            unsafe_allow_html=True
        )


        available_features = [
            "➕ Add expenses",
            "🔍 Search expenses",
            "📂 Filter by category",
            "📅 Filter by date",
            "💰 Filter by amount",
            "↕️ Sort expenses"
        ]


        for feature in available_features:

            st.markdown(
                f"""
                <div style="
                    font-size:22px;
                    color:#333333;
                    padding:7px 0px;
                ">
                    {feature}
                </div>
                """,
                unsafe_allow_html=True
            )


    # ======================================================
    # UPCOMING FEATURES
    # ======================================================

    with col2:

        st.markdown(
            """
            <h2 style="
                font-size:38px;
                color:#1E3A8A;
                margin-bottom:15px;
            ">
                🔮 Upcoming Features
            </h2>
            """,
            unsafe_allow_html=True
        )


        upcoming_features = [
            "📊 Expense analytics",
            "📈 Interactive charts",
            "💵 Budget tracker",
            "🎯 Savings tracker",
            "💡 Smart spending insights",
            "📄 Monthly reports"
        ]


        for feature in upcoming_features:

            st.markdown(
                f"""
                <div style="
                    font-size:22px;
                    color:#333333;
                    padding:7px 0px;
                ">
                    {feature}
                </div>
                """,
                unsafe_allow_html=True
            )


    st.divider()


    # ======================================================
    # ADD NEW EXPENSE
    # ======================================================

    st.markdown(
        """
        <h2 style="
            text-align:center;
            font-size:40px;
            color:#1E3A8A;
            margin-bottom:8px;
        ">
            ➕ Add New Expense
        </h2>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <p style="
            text-align:center;
            font-size:22px;
            color:#666666;
            margin-top:0px;
            margin-bottom:25px;
        ">
            Quickly record your latest expense.
        </p>
        """,
        unsafe_allow_html=True
    )


    # ======================================================
    # EXPENSE FORM
    # ======================================================

    with st.form("home_add_expense_form"):

        col1, col2 = st.columns(2)


        # --------------------------------------------------
        # LEFT COLUMN
        # --------------------------------------------------

        with col1:

            st.markdown(
                """
                <p style="
                    font-size:22px;
                    font-weight:bold;
                    color:#1E3A8A;
                    margin-bottom:5px;
                ">
                    📅 Date
                </p>
                """,
                unsafe_allow_html=True
            )


            expense_date = st.date_input(
                "Expense Date",
                label_visibility="collapsed",
                key="home_expense_date"
            )


            st.markdown(
                """
                <p style="
                    font-size:22px;
                    font-weight:bold;
                    color:#1E3A8A;
                    margin-top:18px;
                    margin-bottom:5px;
                ">
                    📂 Category
                </p>
                """,
                unsafe_allow_html=True
            )


            expense_category = st.selectbox(
                "Expense Category",
                CATEGORIES,
                label_visibility="collapsed",
                key="home_expense_category"
            )


        # --------------------------------------------------
        # RIGHT COLUMN
        # --------------------------------------------------

        with col2:

            st.markdown(
                """
                <p style="
                    font-size:22px;
                    font-weight:bold;
                    color:#1E3A8A;
                    margin-bottom:5px;
                ">
                    💰 Amount
                </p>
                """,
                unsafe_allow_html=True
            )


            expense_amount = st.number_input(
                "Expense Amount",
                min_value=0.0,
                step=1.0,
                label_visibility="collapsed",
                key="home_expense_amount"
            )


            st.markdown(
                """
                <p style="
                    font-size:22px;
                    font-weight:bold;
                    color:#1E3A8A;
                    margin-top:18px;
                    margin-bottom:5px;
                ">
                    📝 Description
                </p>
                """,
                unsafe_allow_html=True
            )


            expense_description = st.text_area(
                "Expense Description",
                placeholder="Enter a short description...",
                label_visibility="collapsed",
                key="home_expense_description"
            )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        # --------------------------------------------------
        # SUBMIT BUTTON
        # --------------------------------------------------

        submitted = st.form_submit_button(
            "➕ Add Expense",
            use_container_width=True
        )


    # ======================================================
    # SAVE EXPENSE
    # ======================================================

    if submitted:

        if expense_amount <= 0:

            st.warning(
                "⚠️ Please enter an amount greater than ₹0."
            )

        elif not expense_description.strip():

            st.warning(
                "⚠️ Please enter an expense description."
            )

        else:

            save_expense(
                expense_date,
                expense_category,
                expense_amount,
                expense_description.strip()
            )

            st.success(
                "✅ Expense added successfully!"
            )


# ==========================================================
# EXPENSE MANAGEMENT PAGE
# ==========================================================

elif selected_page == "💰 Expense Management":

    # ======================================================
    # PAGE TITLE
    # ======================================================

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-size:50px;
            color:#1E3A8A;
            margin-bottom:8px;
        ">
            💰 Expense Management
        </h1>
        """,
        unsafe_allow_html=True
    )


    # ======================================================
    # PAGE DESCRIPTION
    # ======================================================

    st.markdown(
        """
        <p style="
            text-align:center;
            font-size:23px;
            color:#666666;
            margin-top:0px;
        ">
            Search, filter and organize your expenses.
        </p>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    # ======================================================
    # DEFAULT FILTER VALUES
    # ======================================================

    if "search_filter" not in st.session_state:

        st.session_state["search_filter"] = ""


    if "category_filter" not in st.session_state:

        st.session_state["category_filter"] = (
            "All Categories"
        )


    if "start_date_filter" not in st.session_state:

        st.session_state["start_date_filter"] = (
            earliest_date
        )


    if "end_date_filter" not in st.session_state:

        st.session_state["end_date_filter"] = (
            pd.Timestamp.today().date()
        )


    if "minimum_amount_filter" not in st.session_state:

        st.session_state["minimum_amount_filter"] = 0.0


    if "maximum_amount_filter" not in st.session_state:

        st.session_state["maximum_amount_filter"] = (
            DEFAULT_MAX_AMOUNT
        )


    if "sort_filter" not in st.session_state:

        st.session_state["sort_filter"] = "Default"


    # ======================================================
    # EXPENSE FILTERS
    # ======================================================

    st.markdown(
        """
        <h2 style="
            font-size:34px;
            color:#1E3A8A;
            margin-bottom:15px;
        ">
            🔍 Expense Filters
        </h2>
        """,
        unsafe_allow_html=True
    )


    # ======================================================
    # FIRST FILTER ROW
    # ======================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        search = st.text_input(
            "🔍 Search Expenses",
            key="search_filter",
            placeholder="Search category or description..."
        )


    with col2:

        selected_category = st.selectbox(
            "📂 Filter by Category",
            ["All Categories"] + CATEGORIES,
            key="category_filter"
        )


    with col3:

        sort_option = st.selectbox(
            "↕️ Sort Expenses By",
            [
                "Default",
                "Amount : Low → High",
                "Amount : High → Low",
                "Date : Oldest → Newest",
                "Date : Newest → Oldest"
            ],
            key="sort_filter"
        )


    # ======================================================
    # SECOND FILTER ROW
    # ======================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        start_date = st.date_input(
            "📅 Start Date",
            key="start_date_filter"
        )


    with col2:

        end_date = st.date_input(
            "📅 End Date",
            key="end_date_filter"
        )


    with col3:

        minimum_amount = st.number_input(
            "💰 Minimum Amount",
            min_value=0.0,
            step=100.0,
            key="minimum_amount_filter"
        )


    # ======================================================
    # THIRD FILTER ROW
    # ======================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        maximum_amount = st.number_input(
            "💵 Maximum Amount",
            min_value=0.0,
            step=100.0,
            key="maximum_amount_filter"
        )


    with col2:

        st.write("")


    with col3:

        st.button(
            "🔄 Reset Filters",
            on_click=reset_filters,
            use_container_width=True
        )


    st.divider()


    # ======================================================
    # VALIDATE FILTER VALUES
    # ======================================================

    invalid_date_range = (
        start_date > end_date
    )

    invalid_amount_range = (
        maximum_amount < minimum_amount
    )


    if invalid_date_range:

        st.error(
            "❌ Start Date cannot be later than End Date."
        )


    elif invalid_amount_range:

        st.error(
            "❌ Maximum Amount must be greater than "
            "or equal to Minimum Amount."
        )


    else:

        # ==================================================
        # CREATE FILTERED DATAFRAME
        # ==================================================

        filtered_expenses = expenses.copy()


        # ==================================================
        # FILTER BY CATEGORY
        # ==================================================

        if selected_category != "All Categories":

            filtered_expenses = filtered_expenses[
                filtered_expenses["Category"]
                == selected_category
            ]


        # ==================================================
        # FILTER BY DATE
        # ==================================================

        filtered_expenses = filtered_expenses[
            (
                filtered_expenses["Date"]
                >= pd.to_datetime(start_date)
            )
            &
            (
                filtered_expenses["Date"]
                <= pd.to_datetime(end_date)
            )
        ]


        # ==================================================
        # FILTER BY MINIMUM AMOUNT
        # ==================================================

        filtered_expenses = filtered_expenses[
            filtered_expenses["Amount"]
            >= minimum_amount
        ]


        # ==================================================
        # FILTER BY MAXIMUM AMOUNT
        # ==================================================

        filtered_expenses = filtered_expenses[
            filtered_expenses["Amount"]
            <= maximum_amount
        ]


        # ==================================================
        # SEARCH EXPENSES
        # ==================================================

        if search.strip():

            search_text = search.strip()

            filtered_expenses = filtered_expenses[
                filtered_expenses["Category"]
                .str.contains(
                    search_text,
                    case=False,
                    na=False,
                    regex=False
                )
                |
                filtered_expenses["Description"]
                .str.contains(
                    search_text,
                    case=False,
                    na=False,
                    regex=False
                )
            ]


        # ==================================================
        # APPLY SORTING
        # ==================================================

        if sort_option == "Amount : Low → High":

            filtered_expenses = (
                filtered_expenses
                .sort_values(
                    by="Amount",
                    ascending=True
                )
            )


        elif sort_option == "Amount : High → Low":

            filtered_expenses = (
                filtered_expenses
                .sort_values(
                    by="Amount",
                    ascending=False
                )
            )


        elif sort_option == "Date : Oldest → Newest":

            filtered_expenses = (
                filtered_expenses
                .sort_values(
                    by="Date",
                    ascending=True
                )
            )


        elif sort_option == "Date : Newest → Oldest":

            filtered_expenses = (
                filtered_expenses
                .sort_values(
                    by="Date",
                    ascending=False
                )
            )


        # ==================================================
        # SUMMARY
        # ==================================================

        st.markdown(
            f"""
            <h2 style="
                font-size:30px;
                color:#1E3A8A;
                margin-top:15px;
                margin-bottom:15px;
            ">
                📋 Showing {len(filtered_expenses)} expense(s)
            </h2>
            """,
            unsafe_allow_html=True
        )


        # ==================================================
        # FILTERED SUMMARY METRICS
        # ==================================================

        if not filtered_expenses.empty:

            filtered_total = (
                filtered_expenses["Amount"].sum()
            )

            filtered_average = (
                filtered_expenses["Amount"].mean()
            )


            col1, col2, col3 = st.columns(3)


            with col1:

                st.metric(
                    "📋 Expenses",
                    len(filtered_expenses)
                )


            with col2:

                st.metric(
                    "💰 Total",
                    format_indian_currency(
                        filtered_total
                    )
                )


            with col3:

                st.metric(
                    "📊 Average",
                    format_indian_currency(
                        filtered_average
                    )
                )


        st.divider()


        # ==================================================
        # PREPARE DATA FOR DISPLAY
        # ==================================================

        display_expenses = filtered_expenses.copy()


        # ==================================================
        # FORMAT DATE
        # ==================================================

        if not display_expenses.empty:

            display_expenses["Date"] = (
                display_expenses["Date"]
                .dt.strftime("%d-%m-%Y")
            )


        # ==================================================
        # FORMAT INDIAN CURRENCY
        # ==================================================

        if not display_expenses.empty:

            display_expenses["Amount"] = (
                display_expenses["Amount"]
                .apply(format_indian_currency)
            )


        # ==================================================
        # DISPLAY EXPENSE TABLE
        # ==================================================

        if display_expenses.empty:

            st.info(
                "🔍 No expenses found matching your filters."
            )

        else:

            st.dataframe(
                display_expenses,
                use_container_width=True,
                hide_index=True,
                height=450,

                column_config={

                    "Date": st.column_config.TextColumn(
                        "📅 Date",
                        width="medium"
                    ),

                    "Category": st.column_config.TextColumn(
                        "📂 Category",
                        width="medium"
                    ),

                    "Amount": st.column_config.TextColumn(
                        "💰 Amount",
                        width="medium"
                    ),

                    "Description": st.column_config.TextColumn(
                        "📝 Description",
                        width="large"
                    )
                }
            )


# ==========================================================
# OTHER PAGES
# ==========================================================

else:

    # ======================================================
    # PAGE TITLE
    # ======================================================

    st.markdown(
        f"""
        <h1 style="
            text-align:center;
            font-size:50px;
            color:#1E3A8A;
            margin-top:30px;
            margin-bottom:15px;
        ">
            {selected_page}
        </h1>
        """,
        unsafe_allow_html=True
    )


    # ======================================================
    # PAGE DESCRIPTION
    # ======================================================

    st.markdown(
        """
        <p style="
            text-align:center;
            font-size:23px;
            color:#666666;
            margin-bottom:35px;
        ">
            This module is currently under development.
        </p>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    # ======================================================
    # DEVELOPMENT MESSAGE
    # ======================================================

    st.info(
        "🚧 This feature will be implemented in the upcoming "
        "development stages of the project."
    )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">
        Developed by <b>Sathvik</b>
        using Python, Streamlit & Pandas
    </div>
    """,
    unsafe_allow_html=True
)