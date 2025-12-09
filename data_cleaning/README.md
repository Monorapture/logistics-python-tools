# 🧹 Supply Chain Data Cleaning Pipeline

> **ETL Strategy:** Transforming raw, messy logistics records into reliable datasets for analysis.

## 🎯 Project Objective
In logistics analysis, the principle **"Garbage In, Garbage Out"** applies. This project builds a robust **Data Cleaning Pipeline** using Python and Pandas to sanitize a raw dataset containing supply chain shipment information.

The goal is to prepare the data for downstream tasks like **Lead Time Analysis** and **Delivery Status Prediction**.

## 💾 The Dataset

* **Source:** Supply Chain Shipment Pricing Data
* **Author:** Pushpit Kamboj (via Kaggle)
* **Link:** [Kaggle Dataset](https://www.kaggle.com/datasets/pushpitkamboj/logistics-data-containing-real-world-data)
* **Context:** The dataset contains ~15,000 rows of shipment data including order dates, shipping modes, customer segments, and delivery statuses.

## 🕵️‍♂️ The Challenge: "Dirty Data"

Upon exploratory data analysis (EDA), several critical data quality issues were identified that would break standard BI tools (PowerBI/Tableau):

1.  **Synthetic Noise in IDs:** `Customer Id` and `Zipcode` fields contained floating-point noise (e.g., `Zip 92745.16` instead of `92745`).
2.  **Inconsistent Types:** Geographic coordinates (`Latitude`/`Longitude`) were mixed with integer logic in some contexts.
3.  **String Dates:** Temporal data (`Order Date`) was stored as object/string, preventing time-series calculation.
4.  **Redundancy:** Naming conventions contained special characters (e.g., `order date (DateOrders)`).

## ⚙️ The Solution: Cleaning Pipeline

The Jupyter Notebook `01_Data_Cleaning_and_Prep.ipynb` implements the following cleaning logic:

### 1. Ingestion & Safety
* Loads data into a dataframe using `pandas`.
* Uses `.copy()` to create a working copy, preserving raw data in memory for verification.

### 2. Type Conversion & Sanitization
* **Zip Codes:** Removal of decimal noise and padding to standard 5-digit string format (e.g., `725.0` -> `00725`).
* **IDs:** Conversion of float-corrupted IDs to clean Integers.
* **Dates:** Parsing string columns into `datetime64[ns]` objects to enable calculations like `Delivery Time = Shipping Date - Order Date`.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Pandas:** For high-performance data manipulation.
* **NumPy:** For numerical operations.
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
