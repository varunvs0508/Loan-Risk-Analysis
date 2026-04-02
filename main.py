from src.data_loader import load_loan_data
from src.preprocessing import clean_data
from src.feature_engineering import feature_engineering
from src.eda import eda
from src.visualization import create_visualizations
from src.database import database_integration
from src.insights import generate_insights

def main():
    df = load_loan_data()
    df = clean_data(df)
    df = feature_engineering(df)

    d1, d2, d3 = eda(df)

    database_integration(df)
    generate_insights(df)
    create_visualizations(df, d1, d2, d3)

if __name__ == "__main__":
    main()