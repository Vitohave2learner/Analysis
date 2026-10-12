import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Take data with ur path
#Delete '#' and fill path to activate

#input_path = r'ur_path_directory.csv'
df = pd.read_csv(input_path)

features_col = [
    'age',
    'previous_gpa',
    'previous_exam_score'
]

# isi nilai kosong pada kolom angka dengan nilai median masing-masing kolom
for col in features_col:
    df[col] = pd.to_numeric(df[col], errors='coerce') # pastikan tipenya angka
    df[col] = df[col].fillna(df[col].median())

X = df[features_col]

# Standarisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# jumlah klaster (K=3) dan latih model K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Analisis rata_rata klaster
cluster_summary = df.groupby('cluster')[features_col].mean()
print("--- RATA-RATA KARAKTERISTIK TIAP KLASTER ---")
print(cluster_summary)

# visualisasi setiap klaster
plt.figure(figsize=(10, 5))
# PERBAIKAN: Mengubah target sumbu y menjadi 'previous_exam_score' sesuai data Anda
sns.boxplot(data=df, x='cluster', y='previous_exam_score', palette='Set2')
plt.title('Distribusi Nilai Ujian Berdasarkan Klaster Siswa')
plt.xlabel('Klaster Siswa')
plt.ylabel('Nilai Ujian Sebelumnya (Previous Exam Score)')
plt.show()
