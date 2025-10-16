# To merge different excel or csv file into one 


import pandas as pd
import os
import glob

# === USER CONFIGURATION ===
# Path to the folder containing your files
folder_path = r""  #Provide folder path

# Output file name
output_file = "merged_output.csv"

# Whether to search subfolders (True/False)
include_subfolders = True
# ===========================

# Collect all Excel and CSV files
if include_subfolders:
    pattern = "**/*"
else:
    pattern = "*"

file_paths = glob.glob(os.path.join(folder_path, pattern), recursive=include_subfolders)
file_paths = [f for f in file_paths if f.lower().endswith(('.csv', '.xlsx', '.xls'))]

if not file_paths:
    print("❌ No Excel or CSV files found in the folder.")
    exit()

print(f"📂 Found {len(file_paths)} files. Starting merge...\n")

merged_df = pd.DataFrame()

for i, file in enumerate(file_paths, 1):
    try:
        print(f"➡️  Reading file {i}/{len(file_paths)}: {os.path.basename(file)}")

        if file.lower().endswith('.csv'):
            df = pd.read_csv(file, dtype=str)  # keep all data as text
        else:
            df = pd.read_excel(file, dtype=str)

        # Clean column names (remove spaces, lower case)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Append to master dataframe (align columns automatically)
        merged_df = pd.concat([merged_df, df], axis=0, ignore_index=True)

    except Exception as e:
        print(f"⚠️  Skipping file due to error: {file}\n{e}")

# Save merged file
merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')
print("\n✅ Merge complete!")
print(f"📁 Merged file saved as: {os.path.abspath(output_file)}")
print(f"📊 Total rows: {len(merged_df)}, Total columns: {len(merged_df.columns)}")
