## To make Mobile Number in correct Indian format 


import pandas as pd
import re


# 📂 Input & output file
file_path = r"" #Path of the file 
output_file = r""  #Path where you want to store file


def clean_number(num):
    """Return cleaned 10-digit mobile number or None if invalid"""
    num = re.sub(r"\D", "", str(num))  # keep only digits
   
    if re.fullmatch(r"91[6-9]\d{9}", num):  # 91XXXXXXXXXX
        return num[-10:]
    elif re.fullmatch(r"0[6-9]\d{9}", num):  # 0XXXXXXXXX
        return num[-10:]
    elif re.fullmatch(r"[6-9]\d{9}", num):  # XXXXXXXXXX
        return num
    else:
        return None  # invalid → null


# 🔹 Read CSV
df = pd.read_csv(file_path, dtype=str)


# 🔹 Clean the "Mobile" column
if "Mobile" in df.columns:
    df["Mobile"] = df["Mobile"].apply(lambda x: clean_number(x) if pd.notna(x) else None)
else:
    raise ValueError("❌ No 'Mobile' column found in the CSV!")


# 🔹 Save cleaned CSV
df.to_csv(output_file, index=False)


print(f"✅ Cleaned CSV saved at: {output_file}")
