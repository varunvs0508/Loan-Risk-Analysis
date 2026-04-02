def eda(df):
    print("\n=== Exploratory Data Analysis ===")

    default_by_loan_type = (
        df.groupby('loan_type')['loan_status']
        .value_counts(normalize=True)
        .unstack()
    )

    default_by_credit_score = (
        df.groupby('credit_score_bucket')['loan_status']
        .value_counts(normalize=True)
        .unstack()
    )

    npa_by_region = (
        df.groupby('region')['loan_status']
        .value_counts(normalize=True)
        .unstack()
    )

    return default_by_loan_type, default_by_credit_score, npa_by_region