import pandas as pd

def load_portfolio():
    data = {
        "Asset": ["US Stocks", "International Stocks", "Bonds", "Real Estate", "Crypto"],
        "Allocation (%)": [40, 25, 20, 10, 5],
        "Annual Return (%)": [8.0, 6.5, 3.5, 5.0, 20.0],
        "Risk Score (1–10)": [6, 7, 2, 5, 9]
    }
    return pd.DataFrame(data)