"""
DCF Model & Valuation Analysis
Author: Charles Eleri
Description: A Python-based Discounted Cash Flow (DCF) model for company valuation.
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_dcf(cash_flows, discount_rate):
    """
    Calculate the discounted cash flow (DCF) valuation.
    
    Parameters:
        cash_flows (list): Projected cash flows for future years.
        discount_rate (float): Discount rate as a percentage (e.g., 0.10 for 10%).
        
    Returns:
        float: Present value of future cash flows (DCF value).
    """
    dcf_value = sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows, start=1))
    return dcf_value

def plot_cash_flows(cash_flows):
    """
    Plot future cash flows.
    """
    years = range(1, len(cash_flows) + 1)
    plt.figure(figsize=(8,5))
    plt.bar(years, cash_flows, color='blue', alpha=0.6)
    plt.xlabel("Years")
    plt.ylabel("Cash Flow ($)")
    plt.title("Projected Cash Flows")
    plt.show()

if __name__ == "__main__":
    # User input for projected cash flows
    num_years = int(input("Enter number of years for cash flow projections: "))
    projected_cash_flows = []
    for i in range(num_years):
        cf = float(input(f"Enter cash flow for year {i+1}: "))
        projected_cash_flows.append(cf)
    
    # User input for discount rate
    discount_rate = float(input("Enter the discount rate (as a percentage): ")) / 100
    
    # Calculate DCF value
    dcf_value = calculate_dcf(projected_cash_flows, discount_rate)
    print(f"\nThe Discounted Cash Flow (DCF) valuation is: ${dcf_value:,.2f}\n")
    
    # Plot cash flows
    plot_cash_flows(projected_cash_flows)
