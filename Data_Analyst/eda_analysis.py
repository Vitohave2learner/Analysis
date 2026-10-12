import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
#Delete '#' and fill path to activate

#input_path = r'ur_path_directory.csv'
df = pd.read_csv(input_path)

# PERBAIKAN WIB: Pastikan tipe data numerik bersih dari spasi dan diubah ke angka
numeric_cols = ['previous_exam_score', 'previous_gpa', 'age']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col].astype(str).str.strip(), errors='coerce')
    df[col] = df[col].fillna(df[col].median()) # isi data kosong dengan median

# 2. Korelasi Variabel Utama terhadap Nilai Ujian Sebelumnya
correlation = df[numeric_cols].corr()['previous_exam_score'].sort_values(ascending=False)
print("--- KORELASI TERHADAP PREVIOUS EXAM SCORE ---")
print(correlation)

# PERBAIKAN WVB: Bersihkan kolom kategori yang ada di data Anda
df['parent_education'] = df['parent_education'].astype(str).str.strip().fillna('Unknown')

# 3. Analisis Nilai Berdasarkan Pendidikan Orang Tua
print("\n--- RATA-RATA NILAI BERDASARKAN PENDIDIKAN ORANG TUA ---")
group_summary = df.groupby('parent_education')['previous_exam_score'].agg(['mean', 'median', 'std', 'count'])
print(group_summary)

# 4. Visualisasi Data (Matplotlib & Seaborn)
plt.figure(figsize=(14, 6))

# Grafik 1: IPK Sebelumnya vs Nilai Ujian Sebelumnya
plt.subplot(1, 2, 1)
# Menggunakan data sampel 2000 jika data terlalu besar agar scatter plot tidak lemot
sample_size = min(2000, len(df))
sns.scatterplot(data=df.sample(sample_size, random_state=42), x='previous_gpa', y='previous_exam_score', alpha=0.5, color='blue')
plt.title('IPK Sebelumnya vs Nilai Ujian Sebelumnya')
plt.xlabel('IPK Sebelumnya (Previous GPA)')
plt.ylabel('Nilai Ujian Sebelumnya')

# Grafik 2: Pendidikan Orang Tua vs Nilai Ujian Sebelumnya
plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='parent_education', y='previous_exam_score', palette='Set2')
plt.title('Distribusi Nilai Berdasarkan Pendidikan Orang Tua')
plt.xlabel('Pendidikan Orang Tua')
plt.ylabel('Nilai Ujian Sebelumnya')
plt.xticks(rotation=45) # Memutar teks label agar tidak saling bertumpuk

plt.tight_layout()
plt.show()
