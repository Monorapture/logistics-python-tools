# ⚖️ SDR Liability Calculator (CMR)

> **Tool:** Automated calculator for transport liability based on Special Drawing Rights (SDR).
> **Status:** ✅ Active (v1.0)

## 🎯 Purpose
In international logistics (CMR convention), carrier liability is strictly limited to **8.33 SDR (Special Drawing Rights) per kg** of gross weight. 

This leads to a common risk: High-value, low-weight cargo is often massively under-insured. This tool calculates the exact gap in seconds.

## ⚡ Features
* **Live API Integration:** Automatically fetches the daily XDR-to-EUR exchange rate.
* **Risk Assessment:** Instantly compares liability limit vs. goods value.
* **Offline Capable:** Falls back to manual rate entry if no internet is available.
* **Zero Dependencies:** Built with Python's standard GUI library (`tkinter`).

## 🛠️ How to Run

1.  Navigate to the folder:
    ```bash
    cd sdr_calculator
    ```
2.  Install requirements (only needs `requests`):
    ```bash
    pip install -r requirements.txt
    ```
3.  Launch the tool:
    ```bash
    python sdr_tool.py
    ```

## 🧮 The Math (CMR Art. 23)
The logic implements the standard formula:
```python
Liability Limit (€) = Gross Weight (kg) * 8.33 * Daily SDR Rate (€)