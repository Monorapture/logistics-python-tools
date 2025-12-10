# 🧹 Supply Chain Data Cleaning Pipeline

> **ETL Strategy:** Transforming raw, messy logistics records into reliable datasets for analysis.
> **Status:** ✅ Completed (v1.0)

## 🎯 Project Objective
In logistics analysis, the principle **"Garbage In, Garbage Out"** applies. This project builds a robust **Data Cleaning Pipeline** using Python and Pandas to sanitize a raw dataset containing supply chain shipment information.

The goal is to prepare the data for downstream tasks like **Lead Time Analysis** (KPI Calculation) and **Delivery Status Prediction**.

## 💾 The Dataset

* **Source:** Supply Chain Shipment Pricing Data
* **Author:** Pushpit Kamboj (via Kaggle)
* **Link:** [Kaggle Dataset](https://www.kaggle.com/datasets/pushpitkamboj/logistics-data-containing-real-world-data)
* **Context:** The dataset contains ~15,000 rows of shipment data including order dates, shipping modes, customer segments, and delivery statuses.

## 🕵️‍♂️ The Challenge: "Dirty Data"

Upon exploratory data analysis (EDA), several critical data quality issues were identified that would break standard BI tools (PowerBI/Tableau):

1.  **Logical Fallacies ("Time Travel" & "Zombies"):** * About 40% of the dataset contained **negative shipping times** (Shipment Date < Order Date).
    * Extreme positive outliers were found (e.g., **1,430 days** delivery time for standard shipping), indicating "Zombie Shipments".
2.  **Synthetic Noise in IDs:** `Customer Id` and `Zipcode` fields contained floating-point noise (e.g., `Zip 92745.16` instead of `92745`).
3.  **Financial Precision:** Monetary values (Prices, Sales, Profit) often had 6+ decimal places, requiring standardization.
4.  **Inconsistent Types:** Geographic coordinates (`Latitude`/`Longitude`) were mixed with integer logic in some contexts.
5.  **String Dates:** Temporal data (`Order Date`) was stored as object/string, preventing time-series calculation.

## ⚙️ The Solution: Cleaning Pipeline

The Jupyter Notebook `01_Data_Cleaning_and_Prep.ipynb` implements the following cleaning logic:

### 1. Ingestion & Safety
* Loads data using `pandas`.
* Uses `.copy()` to create a working copy, preserving raw data in memory for verification.

### 2. Type Conversion & Sanitization
* **Zip Codes:** Removal of decimal noise and padding to standard 5-digit string format (e.g., `725.0` -> `00725`).
* **IDs:** Conversion of float-corrupted IDs (Product, Category, Customer) to clean Integers.
* **Dates:** Parsing string columns into `datetime64[ns, UTC]` objects.
* **Financials:** Rounding all monetary columns (Sales, Price, Discount) to 2 decimal places for accounting precision.

### 3. Logic Preservation (Quality Gate)
* **Lead Time Calculation:** Computed `actual_shipping_days`.
* **Anomaly Removal:** * Removed rows with **negative lead times** (physically impossible).
    * Applied a **Plausibility Cutoff**: Removed shipments > 120 days (unrealistic for consumer goods).
* **Destructive Cleanup:** Dropped original "dirty" columns after successful transformation to reduce memory usage.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Pandas:** For high-performance data manipulation and ETL.
* **Jupyter Notebook:** For interactive development and documentation.

## 🚀 How to Run

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install pandas
    ```
3.  Open the notebook:
    ```bash
    jupyter notebook 01_Data_Cleaning_and_Prep.ipynb
    ```

---
*Created by [Kilian Sender](https://www.linkedin.com/in/kilian-sender-aa3100347/) - Aspiring Data Analyst & Supply Chain Expert.*
