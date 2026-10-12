# 📊 Student Exam Performance Analysis

Hello everyone! This is my **very first data analysis project**. The dataset is sourced from Kaggle: [Student Exam Performance and Success Dataset](https://www.kaggle.com/datasets/mobeenfatimah/student-exam-performance-and-success-dataset).

This project focuses on cleaning student data, running K-Means Clustering, and visualizing the correlation between student demographics and their exam scores.

---

## 🛠️ Prerequisites & Installation

All commands below are optimized for **Windows PowerShell**. Follow these steps to set up the environment and run the code.

### 1. Create a Virtual Environment
Before running the scripts, you need to create a Python virtual environment:
```powershell
python -m venv env
```

### 2. Activate the Environment
Activate the virtual environment by running the following script:
```powershell
.\env\Scripts\Activate.ps1
```
*Note: If you encounter an Execution Policy restriction error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first.*

### 3. Install Required Libraries
Once the environment is active, install all the necessary dependencies:
```powershell
python -m pip install pandas openpyxl scikit-learn matplotlib seaborn
```

---

## 🚀 How to Run

1. Run the data cleaning script to prepare the dataset:
   ```powershell
   python clean_data.py
   ```
2. Run the analysis or clustering script to see the results and visualizations:
   ```powershell
   python clustering.py
   ```
