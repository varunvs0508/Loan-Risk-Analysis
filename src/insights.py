def generate_insights(df):
    print("\n=== Insights ===")

    high_stress_default = (
        df[df['emi_to_income_ratio'] > 0.5]['loan_status']
        .value_counts(normalize=True)
        .get('Default', 0) * 100
    )

    print(f"High EMI stress default rate: {high_stress_default:.2f}%")