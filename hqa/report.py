import random
from datetime import date

def random_range(low, high, decimals=1):
    return round(random.uniform(low, high), decimals)

def generate_report():
    today = date.today()
    report_date = today.strftime("%d/%m/%Y")
    
    report = {
        "Date": report_date,
        "Laboratory": "HealthCare Diagnostics",
        "CBC": {
            "Hemoglobin": f"{random_range(12.0, 15.5)} g/dL",
            "WBC": f"{random_range(4000, 11000, 0)} /µL",
            "Platelets": f"{random_range(150000, 450000, 0)} /µL",
            "RBC": f"{random_range(4.0, 5.2)} M/µL",
            "Hematocrit": f"{random_range(36, 46, 0)} %",
        },
        "Metabolic Panel": {
            "Glucose (Fasting)": f"{random_range(70, 100)} mg/dL",
            "Creatinine": f"{random_range(0.6, 1.2)} mg/dL",
            "BUN": f"{random_range(7, 20, 0)} mg/dL",
            "Sodium": f"{random_range(135, 145, 0)} mEq/L",
            "Potassium": f"{random_range(3.5, 5.0)} mEq/L",
        },
        "Lipid Profile": {
            "Total Cholesterol": f"{random_range(150, 200, 0)} mg/dL",
            "HDL Cholesterol": f"{random_range(40, 60, 0)} mg/dL",
            "LDL Cholesterol": f"{random_range(50, 100, 0)} mg/dL",
            "Triglycerides": f"{random_range(50, 149, 0)} mg/dL",
        },
        "Liver Function": {
            "ALT": f"{random_range(7, 56, 0)} U/L",
            "AST": f"{random_range(10, 40, 0)} U/L",
            "Alkaline Phosphatase": f"{random_range(44, 147, 0)} U/L",
            "Total Bilirubin": f"{random_range(0.3, 1.2, 1)} mg/dL",
        },
        "Thyroid Function": {
            "TSH": f"{random_range(0.4, 4.0, 2)} µIU/mL",
            "T4": f"{random_range(0.8, 1.8, 1)} ng/dL",
        },
        "Notes": "All values are within normal reference ranges."
    }
    return report

# Example usage:
r = generate_report()
for section, metrics in r.items():
    if isinstance(metrics, dict):
        print(f"\n{section}")
        for k, v in metrics.items():
            print(f"  {k}: {v}")
    else:
        print(f"{section}: {metrics}")
