# Task 1
import pandas as pd

data = {
    "CustomerID": [201,202,203,204,205,206,207,207,208,209],
    "Name": ["Rahul","Anita",None,"Kiran","Sneha","Tom","Pooja","Pooja","Zara","Neha"],
    "Age": [24,29,None,21,27,None,34,34,26,None],
    "City": [" Hyderabad","Pune ","Delhi",None,"Hyderabad","Chennai ",
             "Pune","Pune"," Delhi","Hyderabad "],
    "OrderAmount": [1800,None,2600,2100,None,3200,1400,1400,None,2900],
    "PaymentMethod": ["UPI","Card","Cash",None,"UPI","Card",
                      "Cash","Cash","UPI",None],
    "Date": ["2024-01-08","2024-01-15","2024-02-03","2024-02-12","2024-03-05",
             "2024-03-08","2024-03-15","2024-03-15","2024-04-04","2024-04-10"]
}

df = pd.DataFrame(data)

print("Shape before cleaning:", df.shape)
print("\nMisiing values report:")
print(df.isna().sum())

numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col].fillna(df[col].median(),inplace=True)
df = df.drop_duplicates()
print("\nShape after cleaning:",df.shape)

# Task 2

import pandas as pd

df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Price": ["$120.50", "$99.99", "$150.00", "$80.25"],
    "Date": ["2024-01-05", "2024-01-10", "2024-02-01", "2024-02-15"]
})

print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print(df.dtypes)

# Task 3

import pandas as pd

df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "New York", " new york "]
})

df["Location"] = df["Location"].str.strip()

df["Location"] = df["Location"].str.title()
print("\nAfter Cleaning:")
print(df["Location"].unique())
