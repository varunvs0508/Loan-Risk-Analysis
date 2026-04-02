import matplotlib.pyplot as plt

def create_visualizations(df, default_by_loan_type, default_by_credit_score, npa_by_region):

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    default_by_loan_type['Default'].plot(kind='bar')
    plt.title("Default Rate by Loan Type")

    plt.subplot(2, 2, 2)
    default_by_credit_score['Default'].plot(kind='bar')
    plt.title("Credit Score vs Default Rate")

    plt.subplot(2, 2, 3)
    plt.hist(df['emi_to_income_ratio'], bins=20)
    plt.axvline(0.5, linestyle='--')
    plt.title("EMI-to-Income Ratio")

    plt.subplot(2, 2, 4)
    npa_by_region['Default'].plot(kind='bar')
    plt.title("Region-wise NPA")

    plt.tight_layout()
    plt.savefig("loan_risk_analysis_dashboard.png", dpi=300)
    plt.show()