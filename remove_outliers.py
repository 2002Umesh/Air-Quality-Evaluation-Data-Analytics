def remove_outliers_iqr(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        mean_value = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)][col].mean()

        df[col] = df[col].apply(lambda x: mean_value if x < lower_bound or x > upper_bound else x)
    
    return df