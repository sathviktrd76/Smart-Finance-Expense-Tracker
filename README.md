<div align="center">

# 💰 Smart Finance Expense Tracker

### Manage Your Personal Finances with Python & Streamlit

A beginner-friendly personal finance management application built using  
**Python • Streamlit • Pandas • CSV File Handling**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Data%20Storage-217346?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Under%20Development-FFA500?style=for-the-badge)

<br>

**🚧 Currently Under Development**

</div>

---

<div align="center">

## 📌 About the Project

</div>

**Smart Finance Expense Tracker** is a personal finance management application
developed using **Python, Streamlit and Pandas**.

The application allows users to record and organize their daily expenses,
search through financial records, apply multiple filters, sort expenses and
view spending information through an interactive interface.

The project is being developed **step by step** with the goal of transforming
a beginner-level Python application into a more complete and practical
personal finance management system.

The project also focuses on learning how different Python concepts can be
combined with **data processing, file handling, UI development and Git/GitHub
workflow** to build a real-world application.

> 🚧 **Project Status:** Under Development  
> New modules, analytics features and financial tools will be added in future
> development stages.

---

<div align="center">

## ✨ Features

</div>

### 🏠 Dashboard & Navigation

- 🏠 Home Page Dashboard
- 📋 Sidebar Navigation
- 🧭 Organized Application Navigation
- 📊 Dashboard Summary Metrics
- 💰 Total Spending Display
- 📈 Average Expense Display
- 🔝 Highest Expense Display

### ➕ Expense Management

- ➕ Add New Expense
- 📅 Select Expense Date
- 📂 Select Expense Category
- 💰 Enter Expense Amount
- 📝 Add Expense Description
- 💾 Save Expenses to CSV
- 📄 Automatic CSV File Creation
- ✅ Success Message After Saving
- 📋 View Expense Records
- 📊 Display Expenses in an Interactive Table

### 🔍 Search Features

- 🔍 Search Expenses
- 🔎 Search by Category
- 📝 Search by Description
- 🔤 Case-Insensitive Search
- 📂 Pandas DataFrame Filtering
- 🔄 Search Combined with Other Filters

### ⚙️ Filtering & Sorting

- 📂 Filter by Category
- 💰 Filter by Minimum Amount
- 💵 Filter by Maximum Amount
- 📅 Filter by Start Date
- 📅 Filter by End Date
- 🔄 Apply Multiple Filters Together
- ↕️ Sort Expenses by Amount
- 📉 Amount: Low → High
- 📈 Amount: High → Low
- 📅 Date: Oldest → Newest
- 📅 Date: Newest → Oldest
- 🔄 Reset Filters
- ⚠️ Filter Validation
- 📊 Display Filtered Expense Summary

### 🎨 UI & UX Improvements

- 🎨 Custom CSS Styling
- 📏 Increased Input Field Sizes
- 🔘 Improved Button Sizes
- 🔠 Improved Navigation Font Size
- ↔️ Improved Navigation Spacing
- 📊 Improved Expense Table Readability
- 💱 Indian Currency Formatting
- 📱 Wide Application Layout
- ✨ Cleaner Expense Management Interface
- 🧠 Streamlit Session State for Filter Management

---

<div align="center">

## 🛠️ Technologies Used

</div align="center">

| Technology | Purpose | Status |
|:---:|:---|:---:|
| 🐍 **Python** | Core programming language | ✅ |
| 🎈 **Streamlit** | Interactive web application framework | ✅ |
| 🐼 **Pandas** | Data processing and DataFrame operations | ✅ |
| 📄 **CSV** | Expense data storage | ✅ |
| 💻 **OS Module** | File and directory handling | ✅ |
| 📊 **Matplotlib** | Data visualization | 🚧 Coming Soon |

---
</div>

<div align="center">

## 📅 Development Progress

</div>

### ✅ Day 1 — Project Foundation

- Designed the Home Page UI
- Created Sidebar Navigation
- Built the Initial Streamlit Application
- Configured the Streamlit Page
- Established the basic project structure

---

### ✅ Day 2 — Add Expense Module

- Built the Add Expense Module
- Added Date Picker
- Added Category Dropdown
- Added Amount Input
- Added Description Input
- Implemented CSV File Handling
- Automatically Created `expenses.csv`
- Stored Every Expense as a New Row
- Displayed Success Message After Saving

---

### ✅ Day 3 — Expense Data Management

- Implemented View Expenses Module
- Integrated Pandas for Data Handling
- Read Expense Records from CSV
- Converted CSV Data into a Pandas DataFrame
- Displayed Expenses in an Interactive Table
- Added Data Cleaning and Validation
- Converted Date Data into a proper datetime format
- Converted Amount Data into numeric values

---

### ✅ Day 4 — Search Functionality

- Implemented Search Expenses Module
- Added Search Text Box
- Added Search by Expense Category
- Added Search by Expense Description
- Implemented Case-Insensitive Search
- Applied DataFrame Filtering Using Pandas
- Added Search Across Multiple Expense Fields

---

### ✅ Day 5 — Expense Filtering

- Added Category Filter
- Added Minimum Amount Filter
- Added Maximum Amount Filter
- Applied Multiple Filters Together
- Learned Boolean Masking in Pandas
- Improved the Expense Filtering System
- Combined Search and Filtering Functionality

---

### 🚀 Day 6 — Advanced Filtering, Sorting & UI Improvements

- 📅 Added Start Date Filter
- 📅 Added End Date Filter
- 🔎 Implemented Date Range Filtering
- ↕️ Added Expense Sorting
- 💰 Added Low → High Amount Sorting
- 💰 Added High → Low Amount Sorting
- 📅 Added Oldest → Newest Date Sorting
- 📅 Added Newest → Oldest Date Sorting
- 🔄 Added Reset Filters Functionality
- 🧠 Implemented Streamlit Session State
- ♻️ Created a Reusable `reset_filters()` Function
- 📊 Added Filtered Expense Count
- 💰 Added Filtered Total Spending
- 📈 Added Filtered Average Expense
- ⚠️ Added Date Range Validation
- ⚠️ Added Amount Range Validation
- 💱 Added Indian Currency Formatting
- 🎨 Improved Expense Management UI
- 📏 Increased Input Field Sizes
- 🔘 Improved Button Sizes
- 🔠 Improved Navigation Typography
- ↔️ Improved Navigation Spacing
- 📊 Improved Expense Table Readability
- ✨ Added Custom CSS Styling

---

<div align="center">

## 🚀 Current Version

# **v1.5**

### Advanced Filtering • Sorting • Session State • UI Improvements

</div>

---

<div align="center">

## 📂 Project Structure

</div>

```text
Smart-Finance-Expense-Tracker/
│
├── app.py
├── expenses.csv
└── README.md
```

### 📄 File Description

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `expenses.csv` | Stores expense records |
| `README.md` | Project documentation |

> **Note:** `expenses.csv` is automatically created by the application if it
> does not already exist.

---

<div align="center">

## ▶️ Installation & Setup

</div>

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YourUsername/Smart-Finance-Expense-Tracker.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Smart-Finance-Expense-Tracker
```

### 3️⃣ Install Required Dependencies

```bash
pip install streamlit pandas
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

<div align="center">

## 📊 Current Application Capabilities

</div>

At **v1.5**, the application can currently:

```text
Add Expense
     ↓
Store Expense in CSV
     ↓
Load Data using Pandas
     ↓
Search Expenses
     ↓
Filter by Category
     ↓
Filter by Amount
     ↓
Filter by Date Range
     ↓
Sort Expenses
     ↓
Reset Filters
     ↓
Display Filtered Results
```

This workflow demonstrates how a simple Python application can gradually
evolve into a more structured data-driven application.

---

<div align="center">

## 🔮 Upcoming Features

</div>

The following features are planned for upcoming development stages:

### 💼 Expense Management

- ✏️ Edit Expenses
- 🗑️ Delete Expenses
- 🔄 Update Existing Expense Records

### 💵 Financial Management

- 💵 Budget Tracker
- 🎯 Savings Tracker
- 📊 Budget Analysis
- 🎯 Savings Goals

### 📊 Analytics & Visualization

- 📊 Analytics Dashboard
- 📈 Interactive Charts
- 🥧 Category-wise Spending Charts
- 📅 Monthly Spending Analysis
- 📉 Spending Trends

### 🧠 Smart Features

- 🧠 Smart Spending Insights
- 🔝 Top Expense Identification
- 💡 Personalized Spending Suggestions

### 📄 Reports & Data

- 📄 Monthly Financial Reports
- 📤 Export Data
- 📑 PDF Reports

### ⚙️ Application

- ⚙️ Settings
- 🎨 Further UI/UX Improvements

---

<div align="center">

## 📚 Learning Outcomes

</div>

Through this project, I am gaining practical experience in:

- 🐍 Python Application Development
- 🎈 Streamlit Framework
- 🐼 Pandas Data Processing
- 📄 CSV File Handling
- 💾 File-Based Data Storage
- 📊 DataFrame Operations
- 🔍 Search Functionality
- ⚙️ DataFrame Filtering
- 🧠 Boolean Masking
- 📅 Date-Based Filtering
- ↕️ Sorting Data using Pandas
- 🧠 Streamlit Session State
- ♻️ Creating Reusable Functions
- ⚠️ Input Validation
- 💱 Currency Formatting
- 🎨 Streamlit UI/UX Customization
- 🧩 Building Real-World Applications
- 🌱 Git & GitHub Workflow

---

<div align="center">

## 🎯 Project Goals

</div>

The long-term goal of **Smart Finance Expense Tracker** is to evolve this
application from a simple expense tracker into a more complete personal
finance management system.

The planned final application will provide users with tools to:

**Track → Filter → Analyze → Understand → Improve**

their personal spending habits.

---

<div align="center">

## 📸 Project Preview

</div>

Screenshots and application demonstrations will be added as the project
continues to develop.

> 📌 More screenshots will be included as major features such as analytics,
> charts, budgets and reports are implemented.

---

<div align="center">

## 🌱 Development Journey

</div>

This project is being developed incrementally to strengthen practical
programming skills.

```text
Python Fundamentals
        ↓
File Handling
        ↓
CSV Data Storage
        ↓
Streamlit UI
        ↓
Pandas Data Processing
        ↓
Search & Filtering
        ↓
Sorting & Session State
        ↓
Analytics & Visualization
        ↓
Complete Finance Application
```

---

<div align="center">

## 🤝 Future Development

</div>

This project will continue to evolve with additional functionality,
better data visualization, improved user experience and more advanced
financial management capabilities.

The development process focuses on writing understandable code first and
gradually improving the application's structure, functionality and
professional quality.

---

<div align="center">

## 👨‍💻 Author

# **Sathvik Talabathula**

**B.Tech CSE (AI & ML) Student | CMR UNIVERSITY**

<br>

Made using

### 🐍 Python • 🎈 Streamlit • 🐼 Pandas • 📄 CSV

<br>

⭐ **If you find this project interesting, consider giving it a star!**

</div>

---

<div align="center">

### 🚀 Smart Finance Expense Tracker

**From a simple Python project to a complete personal finance application.**

</div>
