# 🧹 Supply Chain Data Cleaning (ETL)

> **The Engine Room:** Transforming raw, messy logistics records into a reliable dataset for analytics.
> **Status:** ✅ Completed (v1.0)

## 🎯 The Objective
In logistics analysis, the principle **"Garbage In, Garbage Out"** applies strictly. Before any dashboarding or machine learning can happen, the raw data must be sanitized.

This pipeline performs **Exploratory Data Analysis (EDA)** and **Data Cleaning** to fix critical quality issues found in the raw export.

## 📂 File Structure

| File | Description |
| :--- | :--- |
| `01_Data_Cleaning_and_Prep.ipynb` | The **Jupyter Notebook** containing the cleaning logic, EDA charts, and documentation. |
| `raw_supply_chain_data.csv` | The **Raw Input**. Contains ~15,000 rows of shipment data with errors (Negative shipping days, corrupted IDs). |
| `metadata_columns.csv` | Dictionary describing the variables (Source: Kaggle). |
| `cleaned_supply_chain_data.csv` | The **Golden Record** (Output). This file is consumed by the [Dashboard](../dashboard). |

## 🕵️‍♂️ Detected Data Quality Issues

During the initial EDA, several critical issues were identified that would break standard BI tools:

### 1. "Time Travel" & Zombies 🧟
* **Issue:** ~40% of records showed negative shipping times (Shipping Date < Order Date).
* **Issue:** Extreme outliers (e.g., **1,430 days** delivery time) indicated "Zombie Shipments" (system errors or lost packages).
* **Fix:** Removed physically impossible rows and applied a plausibility cutoff (> 120 days).

### 2. ID Corruption 🆔
* **Issue:** IDs for Customers and Products were stored as Floats (e.g., `12097.0`) instead of Integers.
* **Fix:** Cast all ID columns to clean `int` types to ensure referential integrity.

### 3. Zip Code Standardization 📮
* **Issue:** Zip codes contained decimal points (`725.0`) and missing leading zeros.
* **Fix:** Padded all Zip Codes to standard 5-digit strings (e.g., `00725`).

## 🛠️ Tech Stack
* **Python 3.10+**
* **Pandas:** For vectorized data manipulation.
* **NumPy:** For numerical operations.
* **Matplotlib/Seaborn:** For visualization of outliers (Boxplots) inside the notebook.

## 🚀 How to Re-Run
1.  Ensure you have the requirements installed (`pip install -r ../requirements.txt`).
2.  Open the notebook:
    ```bash
    jupyter notebook 01_Data_Cleaning_and_Prep.ipynb
    ```
3.  Run all cells to regenerate `cleaned_supply_chain_data.csv`.