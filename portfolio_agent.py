from portfolio_data import load_portfolio
from portfolio_prompt import portfolio_template
from langchain.chat_models import ChatOpenAI

def analyze_portfolio():
    df = load_portfolio()
    table = df.to_string(index=False)

    llm = ChatOpenAI(temperature=0.3)
    prompt = portfolio_template.format(portfolio_table=table)
    response = llm.predict(prompt)

    return df, response