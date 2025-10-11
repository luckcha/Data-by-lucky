import pandas as pd
import os

# === USER CONFIGURATION ===
# Input merged file
input_file = r""  #Provide Full Path

# Output cleaned file
output_file = r""  #Provide full path
# ===========================

# Detect file type
file_ext = os.path.splitext(input_file)[1].lower()

# Read file
if file_ext == ".csv":
    df = pd.read_csv(input_file, dtype=str)
elif file_ext in [".xlsx", ".xls"]:
    df = pd.read_excel(input_file, dtype=str)
else:
    print("❌ Unsupported file type. Use CSV or Excel.")
    exit()

print(f"📊 Original data: {len(df)} rows, {len(df.columns)} columns")

# Remove duplicates
df_cleaned = df.drop_duplicates(ignore_index=True)

print(f"✅ Duplicates removed. Cleaned data: {len(df_cleaned)} rows")

# Save cleaned file
if file_ext == ".csv":
    df_cleaned.to_csv(output_file, index=False, encoding='utf-8-sig')
else:
    df_cleaned.to_excel(output_file, index=False)

print(f"📁 Cleaned file saved as: {os.path.abspath(output_file)}")
