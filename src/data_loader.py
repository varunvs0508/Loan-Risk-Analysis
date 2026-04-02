import pandas as pd

def load_loan_data():
    df = pd.read_csv("data/RetailLendingRiskIntelligence.csv")
    print("Dataset Loaded | Shape:", df.shape)
    return df