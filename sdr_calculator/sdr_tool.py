"""
TOOL: CMR Liability Calculator (SDR/SZR)
AUTHOR: Kilian Sender
DESCRIPTION: 
    Calculates carrier liability based on weight and daily SDR rates.
    Fetches live exchange rates via API or allows manual input.
    Built with Tkinter for zero-dependency local usage.
"""

import tkinter as tk
from tkinter import messagebox
import requests

# --- BACKEND LOGIC ---

def fetch_live_sdr_rate():
    """
    Fetches the current XDR (SDR) to EUR exchange rate from a public API.
    Returns the rate as a string or None if the request fails.
    """
    url = "https://open.er-api.com/v6/latest/XDR" # Free Exchange Rate API
    
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            rate = data['rates']['EUR']
            return str(rate)
    except Exception as e:
        print(f"API Connection failed: {e}") # Debugging info
        return None

def calculate_liability():
    """
    Reads inputs, calculates liability limit, and compares it with goods value.
    Updates the UI with the result.
    """
    try:
        # Get values from GUI
        weight = float(entry_weight.get())
        goods_value = float(entry_value.get())
        sdr_rate = float(entry_rate.get())
        
        # CMR Logic: 8.33 SDR per kg gross weight
        liability_limit = weight * 8.33 * sdr_rate
        
        # Comparison logic
        gap = goods_value - liability_limit
        
        # Display Result
        result_text = f"⚖️ Liability Limit: {liability_limit:,.2f} €\n"
        
        if liability_limit >= goods_value:
            # Safe Scenario
            messagebox.showinfo(
                "Result: Covered ✅", 
                f"{result_text}\n✅ FULL COVERAGE.\nThe carrier liability covers the entire value of goods."
            )
        else:
            # Risk Scenario
            messagebox.showwarning(
                "Result: Insurance Gap ⚠️", 
                f"{result_text}\n⚠️ RISK ALERT: Under-insured!\nPotential Gap: {gap:,.2f} €\nRecommend extra cargo insurance."
            )
            
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers (use point '.' for decimals).")

# --- FRONTEND (GUI) ---

# Main Window Setup
root = tk.Tk()
root.title("Logistics CMR Checker 🚛")
root.geometry("400x380")

# Header
header_label = tk.Label(root, text="CMR Liability Auditor", font=("Arial", 16, "bold"))
header_label.pack(pady=15)

# Input: Weight
tk.Label(root, text="Gross Weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Input: Value
tk.Label(root, text="Value of Goods (€):").pack()
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Input: SDR Rate
rate_label = tk.Label(root, text="Current SDR Rate (XDR -> EUR):")
rate_label.pack()
entry_rate = tk.Entry(root)
entry_rate.pack(pady=5)

# Auto-Fetch Logic on Startup
current_rate = fetch_live_sdr_rate()
if current_rate:
    entry_rate.insert(0, current_rate)
    rate_label.config(text="Current SDR Rate (Live API ✅):", fg="green")
else:
    rate_label.config(text="Current SDR Rate (Manual Input Required):", fg="red")

# Spacer
tk.Label(root, text="").pack()

# Action Button
calc_button = tk.Button(
    root, 
    text="Calculate Liability Risk", 
    command=calculate_liability,
    bg="#007ACC", 
    fg="white", 
    font=("Arial", 10, "bold"),
    height=2,
    width=25
)
calc_button.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="v1.0 | Logistics Python Tools", fg="grey", font=("Arial", 8))
footer_label.pack(side="bottom", pady=5)

# Start App
root.mainloop()