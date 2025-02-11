import pandas as pd            # Library for data manipulation
import seaborn as sns          # Library for statistical plotting
import matplotlib.pyplot as plt  # For creating custom plots
import streamlit as st         # Framework for building interactive web apps

# ================================================================================
# Missing Data & Data Quality Checks
#
# This lecture covers:
# - Data Validation: Checking data types, missing values, and ensuring consistency.
# - Missing Data Handling: Options to drop or impute missing data.
# - Visualization: Using heatmaps and histograms to explore data distribution.
# ================================================================================
st.title("Missing Data & Data Quality Checks")
st.markdown("""
This lecture covers:
- **Data Validation:** Checking data types, missing values, and basic consistency.
- **Missing Data Handling:** Options to drop or impute missing data.
- **Visualization:** Using heatmaps and histograms to understand data distribution.
""")

# ------------------------------------------------------------------------------
# Load the Dataset
# ------------------------------------------------------------------------------
# Read the Titanic dataset from a CSV file.
df = pd.read_csv("titanic.csv")

# ------------------------------------------------------------------------------
# Display Summary Statistics
# ------------------------------------------------------------------------------
# Show key statistical measures like mean, standard deviation, etc.
st.write("**Summary Statistics**")
st.write(df.shape)
st.dataframe(df.describe())

# a lot of missing values for age, min is 18 - likely missing age from minors
# MNAR - intentional reason for not recording age of minors
# lowest fare is 0, might have something wrong with inputs

# ------------------------------------------------------------------------------
# Check for Missing Values
# ------------------------------------------------------------------------------
# Display the count of missing values for each column.
st.write("**Number of Missing Values by Column**")
st.dataframe(df.isnull().sum()) # can sum because true is equivalent to 1
# ------------------------------------------------------------------------------
# Visualize Missing Data
# ------------------------------------------------------------------------------
# Create a heatmap to visually indicate where missing values occur.
st.write("**Heatmap of Missing Values**")
fig, ax = plt.subplots() # sets up a canvas to print on
sns.heatmap(df.isnull(), cmap = "viridis", cbar = False)
st.pyplot(fig)

# ================================================================================
# Interactive Missing Data Handling
#
# Users can select a numeric column and choose a method to address missing values.
# Options include:
# - Keeping the data unchanged
# - Dropping rows with missing values
# - Dropping columns if more than 50% of the values are missing
# - Imputing missing values with mean, median, or zero
# ================================================================================
st.subheader("Handle Missing Data")
# select box with names of columns that have numeric data types
column = st.selectbox("Choose a column to fill", df.select_dtypes(include=["number"]).columns)

# Work on a copy of the DataFrame so the original data remains unchanged.
st.dataframe(df[column])

# Apply the selected method to handle missing data.
method = st.radio("Choose a method",
                  options = ["Original DF", "Drop Rows", "Drop Columns",
                             "Impute Mean", "Impute Median", "Impute Zero"])

# ------------------------------------------------------------------------------
# Compare Data Distributions: Original vs. Cleaned
#
# Display side-by-side histograms and statistical summaries for the selected column.
# ------------------------------------------------------------------------------

