import streamlit as st
import pandas as pd


st.markdown(
    """
    <style>
        /*Page Background */
        .stApp{
            background-color : #f7f9fc;
        }
        /* Title */
        .title {
            color: #2c3e50;
            text-align: center;
            font-size : 36px;
            font-weight :bold;
        }
        /* SubHeaders */
        .subheader{
            color: #34495e;
            font-size: 24px;
            font-weight: bold;
            margin-top:20px;
        }
        /* Dropdown and Buttons*/
        .stSelectbox, stButton button {
            background-color : #2ecc71 !important;
            color: white !important;
            font-weight : bold;
            border-radius : 8px;
            border : none;
        }
        .stButton button:hover{
            background-color: #27ae60 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 
st.set_page_config(page_title="Data Dashboard", page_icon="📂", layout="wide")

# Title
st.markdown('<h1 class="title">  Simple Data Dashboard </h1>', unsafe_allow_html=True)

#  File Uploader
uploaded_file = st.file_uploader("📂Upload a CSV  or Excel file", type=["csv","xlsx"])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = pd.read_excel(uploaded_file)

    #  Data Preview 
    st.markdown('<h2 class="subheader">  🔍Data Preview</h2>', unsafe_allow_html=True)
    st.dataframe(df.head())

    st.markdown('<h2 class="subheader"> 📊 Data Summary </h2>', unsafe_allow_html = True)
    st.write(df.describe())

    st.markdown('<h2 class="subheader">📰 Filter Data </h2>', unsafe_allow_html=True)
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)

    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value ", unique_values)
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.markdown('<h2 class="subheader"> 📉 Plot Data </h2>',unsafe_allow_html=True)
    x_column = st.selectbox("Select x_axis columns", columns)
    y_column = st.selectbox("Select y_axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("📢 Waiting for file upload...")