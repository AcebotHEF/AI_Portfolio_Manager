# 📈 AI Portfolio Manager & Wealth Advisor

**A smart investment analysis tool powered by OpenAI and LangChain.**



[Image of investment portfolio allocation chart]


## 📌 Overview
The **AI Portfolio Manager** is a wealth management dashboard that goes beyond simple tracking. It acts as a **"Fiduciary Advisor"**, analyzing your asset allocation, risk exposure, and market sentiment to provide actionable rebalancing strategies.

It ingests portfolio data (Stocks, Bonds, Crypto, Real Estate) and uses **OpenAI (GPT-3.5/4)** to detect concentration risks and "Buy Low / Sell High" opportunities.

## 🚀 Features
* **Smart Risk Analysis:** Calculates weighted portfolio risk and flags dangerous over-exposure (e.g., >15% in a single asset).
* **Strategic Rebalancing:** Identifies assets with high unrealized gains to "Trim" and undervalued assets to "Accumulate."
* **Interactive Visuals:** Features a modern **Matplotlib Donut Chart** to visualize asset allocation.
* **Fiduciary Persona:** The AI acts as a professional manager, avoiding generic advice and focusing on capital preservation and growth.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Orchestration:** LangChain (Core & OpenAI)
* **LLM:** OpenAI GPT-3.5 Turbo (or GPT-4)
* **Data Visualization:** Matplotlib (Donut Charts)
* **Data Handling:** Pandas
* **Environment:** Python 3.10+

## 📂 Project Structure
```text
portfolio_manager/
├── portfolio_app.py     # Main Dashboard (Streamlit + Charts)
├── portfolio_agent.py   # AI Logic (LangChain + OpenAI connection)
├── portfolio_data.py    # Data Generator (Mock Portfolio & Market Sentiment)
├── portfolio_prompt.py  # "Senior Portfolio Manager" Persona Prompt
├── requirements.txt     # Dependencies
├── .env                 # API Keys (Not tracked in git)
└── README.md            # Documentation
⚙️ Setup & Installation
1. Clone the Repository
Bash
git clone [https://github.com/yourusername/ai-portfolio-manager.git](https://github.com/yourusername/ai-portfolio-manager.git)
cd ai-portfolio-manager
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure API Keys
Create a file named .env in the root folder and add your OpenAI API key:

Ini, TOML
OPENAI_API_KEY=sk-proj-....................
4. Run the Application
Launch the dashboard locally:

Bash
python -m streamlit run portfolio_app.py