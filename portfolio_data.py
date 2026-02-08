import pandas as pd

def load_portfolio():
    """
    Returns a portfolio dataframe with performance metrics and 
    market sentiment tags for AI analysis.
    """
    data = {
        "Asset": [
            "US Tech Growth (ETF)", 
            "European Blue Chip", 
            "Govt Bonds (10yr)", 
            "Corp Bonds (High Yield)",
            "Real Estate REITs", 
            "Gold (Commodities)",
            "Bitcoin / Crypto"
        ],
        "Allocation (%)": [
            35,  # Overweight in Tech (Risk)
            15, 
            20, 
            10, 
            10, 
            5,
            5
        ],
        "Unrealized Gain (%)": [
            +45.0, # High gain -> Potential candidate to "Trim"
            +8.2,
            -2.5,  # Loss -> Potential candidate to "Buy the Dip"
            +4.0,
            +12.0,
            +1.5,
            +85.0  # Massive gain -> High volatility risk
        ],
        "Risk Score (1-10)": [
            8, # High
            6, 
            1, # Safe
            4, 
            5, 
            3,
            10 # Extreme
        ],
        "Market Outlook": [
            "Overvalued / Correction Likely",
            "Neutral",
            "Undervalued / Safe Haven",
            "Neutral",
            "Bullish / Inflation Hedge",
            "Bullish / Uncertainty Hedge",
            "Speculative Bubble Warning"
        ]
    }
    return pd.DataFrame(data)