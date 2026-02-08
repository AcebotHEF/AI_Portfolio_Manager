import streamlit as st
import matplotlib.pyplot as plt
from portfolio_agent import analyze_portfolio

st.title("📈 AI Portfolio Manager")

if st.button("Analyze My Portfolio"):
    df, summary = analyze_portfolio()

    st.subheader("💼 Portfolio Breakdown")
    st.dataframe(df)

    st.subheader("📊 Allocation Pie Chart")
    fig, ax = plt.subplots()
    ax.pie(df["Allocation (%)"], labels=df["Asset"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    st.subheader("🧠 AI Investment Guidance")
    st.write(summary)