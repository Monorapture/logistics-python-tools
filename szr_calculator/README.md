# ⚖️ SZR Liability Calculator (CMR)

> **Tool:** Automated calculator for transport liability based on Special Drawing Rights (SDR).
> **Status:** ✅ Active (v1.0)

## 🎯 Purpose
In international logistics (CMR convention), carrier liability is often limited to **8.33 SDR (Special Drawing Rights) per kg** of gross weight. This tool helps dispatchers and claims managers quickly determine if a shipment is fully covered or if there is an **insurance gap** (under-insurance).

## ⚡ Features
* **Live Currency Conversion:** Automatically fetches the current XDR-to-EUR exchange rate via API (`exchangerate-api.com`) upon startup.
* **Fallback Mode:** Allows manual rate entry if the API/Internet is unavailable.
* **Risk Analysis:** Instantly compares the calculated liability limit against the actual goods value.
* **Visual Feedback:** Clear "Green/Red" status for coverage vs. risk.

## 🛠️ How to Run
1.  Navigate to the folder:
    ```bash
    cd sdr_calculator
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    python sdr_tool.py
    ```

## 🧮 Logic
The calculation follows the CMR standard:
`Liability Limit = Gross Weight (kg) * 8.33 * Daily SDR Rate`

---
*Part of the [Logistics Python Tools](https://github.com/Monorapture/logistics-python-tools) repository.*
