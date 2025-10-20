import pandas as pd
df = pd.read_csv("C:\\Users\\apues\\Downloads\\archive (28)\\us-shein-office_and_school_supplies-4233.csv", header=None)


df = df.iloc[1:, :]

df.columns = ['title', 'url', 'rank', 'category', 'price', 'discount', 'popularity', 'extra']

df = df[['title', 'url', 'price', 'discount', 'popularity']]
df['title'] = df['title'].str.strip()
df['price'] = df['price'].str.replace('$', '', regex=False)
df['discount'] = df['discount'].str.replace('$', '', regex=False)
df['popularity'].fillna('No Data', inplace=True)

df = df.drop_duplicates(subset='url').reset_index(drop=True)

print(df.head(10))
print(f"Total Cleaned Rows : {len(df)}")
df.to_csv("C:\\Users\\apues\\Downloads\\shein_cleaned.csv", index=False)
