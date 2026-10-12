import pandas as pd

# ambil dari lokal
#Use this code pathing your data csv to xlsx.
#Delete '#' and fill path to activate

#input_path = r'ur_path_directory.csv'
#output_path = r'ur_path_directory.xlsx'

# read data
df = pd.read_csv(input_path)

# isi data kosong
cat_cols = ['parent_education', 'education_level', 'school_type', 'family_income', 'urban_rural']
df[cat_cols] = df[cat_cols].fillna('Unknown')

# isi data kosong pada kolom angka dengan nilai media
num_cols = ['previous_gpa', 'age', 'previous_exam_score']
for col in num_cols:
    df[col] = df[col].astype(str).str.strip()

# hilangkan spasi berlebih
str_cols = df.select_dtypes(include=['object']).columns
for col in str_cols:
    df[col] = df[col].astype(str).str.strip()

# ekspor data clean
df.to_excel(output_path, index=False)
print("Ini data clean", output_path)
