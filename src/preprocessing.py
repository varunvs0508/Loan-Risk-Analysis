def clean_data(df):
    print("\n=== Data Cleaning & Preprocessing ===")

    df['monthly_income'] = df['monthly_income'].fillna(df['monthly_income'].median())
    df['credit_score'] = df['credit_score'].fillna(df['credit_score'].median())

    df = df.drop_duplicates()

    Q1 = df['loan_amount'].quantile(0.25)
    Q3 = df['loan_amount'].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df['loan_amount'] >= lower) & (df['loan_amount'] <= upper)]

    return df