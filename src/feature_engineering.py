def feature_engineering(df):
    print("\n=== Feature Engineering ===")

    df['emi_to_income_ratio'] = df['emi_amount'] / df['monthly_income']

    def credit_score_bucket(score):
        if score < 500:
            return 'Low'
        elif score < 700:
            return 'Medium'
        else:
            return 'High'

    df['credit_score_bucket'] = df['credit_score'].apply(credit_score_bucket)

    df['risk_flag'] = (
        (df['emi_delay_days'] > 30) &
        (df['loan_status'] == 'Default')
    ).astype(int)

    return df