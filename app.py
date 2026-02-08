import streamlit as st
import matplotlib.pyplot as plt
# Ensure portfolio_agent.py is in the same directory
from portfolio_agent import analyze_portfolio

# 1. Configure the Page
st.set_page_config(page_title="AI Portfolio Manager", layout="wide", page_icon="📈")

st.title("📈 AI Portfolio Manager")
st.markdown("### Wealth Management & Risk Assessment Dashboard")

# 2. Main Action Button
if st.button("Analyze My Portfolio", type="primary"):
    
    with st.spinner("Analyzing asset allocation and market risks..."):
        # Call the agent
        df, summary = analyze_portfolio()

        if df is not None:
            # --- Layout: Split into two columns ---
            col1, col2 = st.columns([1.2, 1])

            with col1:
                st.subheader("💼 Asset Allocation")
                # Display data with a height limit so it doesn't take up the whole screen
                st.dataframe(df, use_container_width=True, height=400)

            with col2:
                st.subheader("📊 Visual Breakdown")
                
                # --- Improved Donut Chart ---
                fig, ax = plt.subplots(figsize=(6, 6))
                
                # distinct colors for financial charts
                colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
                
                # create pie chart
                wedges, texts, autotexts = ax.pie(
                    df["Allocation (%)"], 
                    labels=df["Asset"], 
                    autopct="%1.1f%%", 
                    startangle=90,
                    colors=colors,
                    pctdistance=0.85, # Move % labels towards the edge
                    explode=[0.05] * len(df) # Slightly separate slices
                )
                
                # draw a white circle in the center to make it a 'Donut'
                centre_circle = plt.Circle((0,0),0.70,fc='white')
                fig.gca().add_artist(centre_circle)
                
                ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
                
                # Make percentage labels legible
                for text in autotexts:
                    text.set_color('black')
                    text.set_fontsize(10)

                st.pyplot(fig)

            # --- AI Report Section ---
            st.divider()
            st.subheader("🧠 Investment Strategy Report")
            
            # Use a container to make the report stand out
            with st.container(border=True):
                st.markdown(summary)
