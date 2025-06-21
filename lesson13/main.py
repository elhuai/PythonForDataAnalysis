import streamlit as st
import pandas as pd
def main():
    st.title("streamlit App")
    st.write("Hi")

    df = pd.read_csv("taiwan.csv")
    st.write(df)

if __name__ == "__main__":    
    main()