from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from portfolio_data import load_portfolio
from portfolio_prompt import portfolio_template

# Load API Key (OPENAI_API_KEY) from .env file
load_dotenv()

def analyze_portfolio():
    """
    Fetches portfolio data and uses OpenAI GPT to generate 
    a strategic rebalancing report.
    """
    try:
        # 1. Load the Data
        df = load_portfolio()
        
        # Convert dataframe to string so the AI can read it
        table = df.to_string(index=False)

        # 2. Initialize OpenAI
        # temperature=0.3 keeps the financial advice consistent and less random
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

        # 3. Create the Chain (Prompt | LLM)
        # This uses the modern "|" pipe syntax
        chain = portfolio_template | llm

        # 4. Run the Chain
        # We pass a dictionary matching the {portfolio_table} variable in your prompt
        response = chain.invoke({"portfolio_table": table})

        # Return the DataFrame (for the chart) and the AI's text (for the report)
        return df, response.content

    except Exception as e:
        # Return None for the dataframe so the UI knows something went wrong
        return None, f"Error generating portfolio analysis: {e}"