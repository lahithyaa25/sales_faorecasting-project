import streamlit as st
import pandas as pd

st.title("Sales Forecasting App")

csv_file_path = r"C:\Users\lahit\OneDrive\Desktop\sales_forecasting project\sales_data.csv"

try:
    df = pd.read_csv(csv_file_path)
    
    # Clean column names
    df.columns = df.columns.str.strip().str.lower()
    
    # Optional: rename common variations
    rename_dict = {
        'date': 'month',
        'sale_price': 'price',
        'promo': 'promotion'
    }
    df.rename(columns=rename_dict, inplace=True)
    
    required_cols = ['month', 'price', 'promotion']
    missing_cols = [col for col in required_cols if col not in df.columns]
    
    if missing_cols:
        st.error(f"Missing columns in dataset: {missing_cols}")
        st.write("Columns in CSV:", df.columns.tolist())
    else:
        st.success("All required columns are present!")
        st.dataframe(df)
        st.line_chart(df.set_index('month')['price'])

except FileNotFoundError:
    st.error(f"CSV file not found at path: {csv_file_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")