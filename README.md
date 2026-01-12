# Automation Assessment Pipeline

This repository contains a 4-step pipeline to automatedly assess and populate attributes for opportunity datasets.

## Overview

The pipeline takes a raw Excel input (`add-on.xlsx`), converts it to a workable JSON format, applies specific assessment logic (Source/Target/AI Capabilities), verifies the data, and exports a final formatted Excel report.

## Prerequisites

You need a Python environment with the following libraries:
*   `pandas`
*   `openpyxl` (for reading Excel)
*   `xlsxwriter` (for writing formatted Excel)

Recommended environment: `datascience` (or ensure `xlsxwriter` is installed in your active env).

## Quick Start (Run All)

To run the entire workflow in one go:

```bash
conda run -n datascience python main.py
```

## Manual Usage Steps

Run the scripts in the `src/` directory in the following order:

### 1. Convert Input
**Script:** `src/1_convert_input.py`
*   **Input:** `src/add-on.xlsx`
*   **Output:** `src/add-on.json`
*   **Purpose:** Converts the raw Excel spreadsheet into a JSON format to ensure data integrity during processing.

```bash
python src/1_convert_input.py
```

### 2. Assess Opportunities (Core Logic)
**Script:** `src/2_assess_opportunities.py`
*   **Input:** `src/add-on.json`
*   **Output:** `src/add-on.json` (updated)
*   **Purpose:** 
    *   Populates 7 key attributes (Source System, Target System, Field Extraction, etc.) based on predefined logic.
    *   Applies V2 refinements (e.g., distinguishing "Rule-based" vs "AI").
    
```bash
python src/2_assess_opportunities.py
```

### 3. Audit Results
**Script:** `src/3_audit_results.py`
*   **Input:** `src/add-on.json`
*   **Output:** Terminal Output (Print)
*   **Purpose:** Prints the `Description` and `Remarks` alongside the generated attributes for manual verification of context accuracy.

```bash
python src/3_audit_results.py
```

### 4. Generate Report
**Script:** `src/4_generate_report.py`
*   **Input:** `src/add-on.json`
*   **Output:** `src/final_assessment_result.xlsx`
*   **Purpose:** Converts the fully populated JSON back into an Excel file.
*   **Features:** Applies text wrapping and auto-adjusts column widths for readability.

```bash
# Ensure you use an env with xlsxwriter
conda run -n datascience python src/4_generate_report.py
```

## Attribute Definitions

The pipeline populates the following attributes:

1.  **Source System**: Where the data originates (e.g., "PDF embedded in Email", "SAP").
2.  **Target System**: Where the data is entered or sent (e.g., "SAP Finance Module", "Excel Report").
3.  **Field Extraction**: Specific data points needed (e.g., "Invoice Date", "Total Amount").
4.  **Expected Final Result**: The tangible outcome (e.g., "Posted Service PO").
5.  **Automation / AI Capabilities**: Comparison of tech needed (e.g., "OCR", "Rule-based Logic", "RPA").
6.  **Data & Compliance Risk**: Potential sensitivities (e.g., "PII", "Commercial Pricing").
7.  **Process Stability**: Assessment of standardized vs. variable inputs.
