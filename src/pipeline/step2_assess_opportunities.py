import json
import os


def run():
    file_path = './data/misc/add-on.json'
    output_path = './data/misc/add-on.json'
    
    # --- 1. Initial Attributes Population (V1) ---
    generated_data = {
        0: { # OCR automation
            "Source System": "PDF embedded in an email\nCarrier Invoices",
            "Target System": "SAP Finance Module\nExcel payment file",
            "Field Extraction": "Full line-item details\nInvoice Date, Total Amount, Requestor",
            "Expected Final Result": "Excel file for payment processing\nDirect SAP entry",
            "Automation / AI Capabilities": "OCR (Text Extraction)\nTable Extraction",
            "Data & Compliance Risk": "Commercial pricing info\nVendor sensitivity",
            "Process Stability": "Medium\nCarrier formats vary"
        },
        1: { # Automation for 3rd party (Asian Supply DM PO)
            "Source System": "Email (Generic Mailbox)\nShared Drive (Shipment Docs)",
            "Target System": "Shared Drive (Designated Folder)\nEmail (to Supplier)",
            "Field Extraction": "Email Attachments (Invoice, BL)\nSubject Line (PO Ref)",
            "Expected Final Result": "Merged PDF of Invoice+BL\nSaved in specific folder\nAuto-email sent",
            "Automation / AI Capabilities": "Document Classification (Invoice vs BL)\nPDF Merging\nEmail Automation",
            "Data & Compliance Risk": "Supplier Shipping Docs\nInternal proprietary info",
            "Process Stability": "Medium\nSupplier email formats may change"
        },
        2: { # Updating market stakeholders on stock status
            "Source System": "SAP (MHCS & HY Plant Outbound Data)\nDeployment Schedule (Excel?)",
            "Target System": "Email (Update to Stakeholders)\nPPP Store Status",
            "Field Extraction": "Outbound Stock Data\nShipping Note Due Date\nLead Time parameters",
            "Expected Final Result": "Periodic Email Update\nStatus Report",
            "Automation / AI Capabilities": "Rule-based logic (Date comparison)\nSAP Data Extraction",
            "Data & Compliance Risk": "Internal Stock Levels (Low Risk)",
            "Process Stability": "High\nSAP reports are standardized"
        },
        3: { # Late Differentiation Improvement (validate SUBPO)
            "Source System": "APO Forecast\nSAP (DM Stock on Hand)",
            "Target System": "Excel (Calculated Order Qty)\nSAP (DM Order Creation)",
            "Field Extraction": "Forecast Quantity\nSOH, In-transit Quantity",
            "Expected Final Result": "Calculation of Required DM Order\nFlagged Discrepancies",
            "Automation / AI Capabilities": "Data Consolidation\nRule-based Logic (Tolerance Check)",
            "Data & Compliance Risk": "Forecast Data (Strategic importance)",
            "Process Stability": "High\nLogic defined by tolerance levels"
        },
        4: { # Consolidation of 3rd party supplier invoices for DM
            "Source System": "Email (Generic Mailbox)",
            "Target System": "Shared Drive (MCL Sub-folders)\nTracking Folder",
            "Field Extraction": "Email Body (Shipment Destination)\nAttachments (Invoices)",
            "Expected Final Result": "Files renamed and moved to folders\nEmail Notification",
            "Automation / AI Capabilities": "Email Classification (SG vs Direct)\nAttachment Saving",
            "Data & Compliance Risk": "Supplier Invoices (pricing)",
            "Process Stability": "Medium\nDepends on supplier email consistency"
        },
        5: { # Invoice validation
            "Source System": "Maersk & Carrier Invoices (PDF/Excel)\nLF Work File",
            "Target System": "Power BI / Excel Report\nSAP (Service PO)",
            "Field Extraction": "Net Value, Tax Amount\nLine item details",
            "Expected Final Result": "Variance Report (>2%)\nService PO Creation for mismatch\nMIRO folder for match",
            "Automation / AI Capabilities": "Data Matching\nVariance Calculation",
            "Data & Compliance Risk": "Financial Data\nPayment validation",
            "Process Stability": "High\nLogic is clearly defined (2% threshold)"
        },
        6: { # Compiling the shipping docs to Maersk
            "Source System": "Buyco Portal (BL)\nShared Drive (Invoice)",
            "Target System": "Designated Merge Folder",
            "Field Extraction": "Bill of Lading\nCommercial Invoice",
            "Expected Final Result": "Consolidated PDF (BL + Invoice)",
            "Automation / AI Capabilities": "Web Scraping (Buyco)\nFile Matching (BL to Invoice)\nPDF Merging",
            "Data & Compliance Risk": "Shipping Manifests\nCustoms Docs",
            "Process Stability": "Medium\nBuyco portal changes"
        },
        7: { # Late Differentiation Improvement (SLOBs 60 days)
            "Source System": "APO System",
            "Target System": "Alert List / Excel Report",
            "Field Extraction": "Supply Days per SKU",
            "Expected Final Result": "List of SKUs > 60 days supply",
            "Automation / AI Capabilities": "Rule-based Logic (Threshold > 60)",
            "Data & Compliance Risk": "Inventory Strategy (Slow Moving)",
            "Process Stability": "High\nFixed rule"
        },
        8: { # OCR automation (Inbound Shipments)
            "Source System": "Carrier BL / SWB (PDF)",
            "Target System": "SAP (Inbound Shipment Creation)",
            "Field Extraction": "Invoice Details\nGross Weight, Vessel, ETA",
            "Expected Final Result": "Inbound Shipment Number in SAP",
            "Automation / AI Capabilities": "OCR (Variable layouts)\nSAP Data Entry",
            "Data & Compliance Risk": "Input accuracy critical for Customs",
            "Process Stability": "Medium\nMultiple carrier formats"
        },
        9: { # Late Differentiation Improvement (Kitting)
            "Source System": "Kitting Report\nSAP",
            "Target System": "SAP MIGO (Goods Receipt)",
            "Field Extraction": "SUBPO Quantity\nRate\nBatch Number",
            "Expected Final Result": "Posted Goods Receipt in SAP",
            "Automation / AI Capabilities": "Data Validation\nSAP Automation (Scripting)",
            "Data & Compliance Risk": "Inventory Accuracy",
            "Process Stability": "High"
        },
        10: { # Forecasting of APAC POSM needs
            "Source System": "SAP ECC (Inbound/Outbound Data)",
            "Target System": "Excel Forecast / PO Request",
            "Field Extraction": "Historical movements\nSKU Categories",
            "Expected Final Result": "Demand Forecast Suggestions\nPO Recommendations",
            "Automation / AI Capabilities": "Predictive Analytics (Potentially)\nTrend Analysis",
            "Data & Compliance Risk": "Strategic Sourcing Data",
            "Process Stability": "Medium\nForecasting logic may evolve"
        },
        11: { # Forumh-BIPO error log tracking
            "Source System": "Forumh Error Log\nBIPO Error Log",
            "Target System": "Excel Tracker",
            "Field Extraction": "Error Messages\nEmployee IDs\nTimestamps",
            "Expected Final Result": "Consolidated Error Tracker\nFlagged New vs Resolved",
            "Automation / AI Capabilities": "Text Comparison\nLog Parsing",
            "Data & Compliance Risk": "Employee Data (PII)\nSystem Interface Logs",
            "Process Stability": "High\nLog formats usually stable"
        },
        12: { # OCR automation (MHCS PO)
            "Source System": "MHCS PO (PDF / Scanned)",
            "Target System": "SAP (PO Creation)",
            "Field Extraction": "PO Details (SKU, Qty, Vendor)",
            "Expected Final Result": "Created PO in SAP",
            "Automation / AI Capabilities": "OCR (Scanned Docs)\nSAP Entry",
            "Data & Compliance Risk": "Procurement Data",
            "Process Stability": "Medium\nScan quality varies"
        },
        13: { # MY Duty Validation
            "Source System": "Import Declaration (PDF)\nInternal Excel Calculation\nSupporting Docs (PDF)",
            "Target System": "Validation Report (Excel)",
            "Field Extraction": "Product No, Qty, Prices\nDuty Amounts",
            "Expected Final Result": "Pass/Fail Validation Status",
            "Automation / AI Capabilities": "OCR (PDF Extraction)\nData Comparison Logic",
            "Data & Compliance Risk": "Customs Duty Amounts (Financial/Legal)",
            "Process Stability": "High\nCustoms forms are standard"
        },
        14: { # Highlighting to-be SLOBs
            "Source System": "SAP (Inbound/Outbound)\nAgency Excel Files",
            "Target System": "Email Notification (Triggers)",
            "Field Extraction": "Inventory Ageing\nMovement History",
            "Expected Final Result": "Proactive Email Alerts to Owners",
            "Automation / AI Capabilities": "Data Consolidation (SAP + Excel)\nPredictive Logic (Trending to SLOB)",
            "Data & Compliance Risk": "Inventory Write-off risk",
            "Process Stability": "Medium\nAgency data quality varies"
        },
        15: { # Streamline the DM replenishment process
            "Source System": "IDR Extraction\nDM Request File",
            "Target System": "Serene's Queue (for SubPR)",
            "Field Extraction": "Replenishment Needs\nStock Levels",
            "Expected Final Result": "Consolidated DM Request File",
            "Automation / AI Capabilities": "Data Aggregation\nRPA (as proposed)",
            "Data & Compliance Risk": "Internal Supply Chain",
            "Process Stability": "Medium"
        },
        16: { # ICR letters checking
            "Source System": "Final Approved Excel Sheet\nICR Letter Template (PDF)\nMovement Excel",
            "Target System": "Validation Report",
            "Field Extraction": "Employee details\nBonus/Merit figures\nDates",
            "Expected Final Result": "Verified ICR Letters\nError Log",
            "Automation / AI Capabilities": "Text Extraction (PDF)\nPII Matching\nLanguage Check (JP)",
            "Data & Compliance Risk": "High Sensitive PII\nCompensation Details",
            "Process Stability": "Medium\nAnnual templates change"
        },
        17: { # LVMH Annual Reporting
            "Source System": "Market HR Excel Data",
            "Target System": "LVMH Talent Connect Portal (Web)",
            "Field Extraction": "Social Reporting Metrics",
            "Expected Final Result": "Data Entered in Web Portal",
            "Automation / AI Capabilities": "Web Form Filling (RPA)\nExcel Data Reading",
            "Data & Compliance Risk": "HR Reporting Metrics",
            "Process Stability": "High\nAnnual standard report"
        },
        18: { # Daily invoices population
            "Source System": "Market/Maison Invoices",
            "Target System": "Respective Folders\nEmail to CS",
            "Field Extraction": "Maison Name, Product Type, Country",
            "Expected Final Result": "Organized Folders\nDistributed Emails",
            "Automation / AI Capabilities": "File Classification\nPython Scripting (Folder Routing)",
            "Data & Compliance Risk": "Commercial Invoices",
            "Process Stability": "High"
        },
        19: { # KR Duty Validation
            "Source System": "Import Declaration (PDF)\nShipment List Excel\nInternal Excel Calculation",
            "Target System": "Validation Result",
            "Field Extraction": "Product No, Duty Amounts\nBL Number, Arrival Year",
            "Expected Final Result": "Validated Duty Amounts",
            "Automation / AI Capabilities": "OCR (KR Text?)\nComplex Lookups (Year Validation)",
            "Data & Compliance Risk": "Customs Duty (Financial)",
            "Process Stability": "High"
        },
        20: { # HC report preparation
            "Source System": "Forumh\nMultiple Source Files",
            "Target System": "Consolidated Excel Report",
            "Field Extraction": "Headcount Numbers\nMovement Details",
            "Expected Final Result": "Unified HC Report",
            "Automation / AI Capabilities": "Data Merging\nDe-duplication",
            "Data & Compliance Risk": "Employee Headcount",
            "Process Stability": "Medium"
        },
        21: { # Enhance QIBK reporting
            "Source System": "Last Month Stock File\nThis Month Stock File",
            "Target System": "Power BI Dashboard\nEmail",
            "Field Extraction": "SKU List\nStock Differences",
            "Expected Final Result": "Updated Dashboard\nNew SKU Alerts",
            "Automation / AI Capabilities": "Data Comparison (Delta)\nVisualization Update",
            "Data & Compliance Risk": "Inventory Data",
            "Process Stability": "High"
        },
        22: { # TH Duty Validation
            "Source System": "Customs Form PDF\nInvoice PDF\nPacking List PDF\nMaster Data Excel",
            "Target System": "Validation Report",
            "Field Extraction": "Quantity, Weight, Duty Amounts\nThai Text (Alcohol Category)",
            "Expected Final Result": "Validated Declaration",
            "Automation / AI Capabilities": "OCR (Thai Language)\nCross-document Matching",
            "Data & Compliance Risk": "Customs Compliance",
            "Process Stability": "High"
        },
        23: { # Consolidation of Carrier invoices
            "Source System": "Generic Mailbox (Carrier Invoices)",
            "Target System": "Shared Drive Sub-folders",
            "Field Extraction": "Carrier Name\nInvoice Number",
            "Expected Final Result": "Files Saved in Correct Folder",
            "Automation / AI Capabilities": "Email attachment saving\nRule-based Routing",
            "Data & Compliance Risk": "Billing Data",
            "Process Stability": "Medium"
        },
        24: { # Conflict of Interest
            "Source System": "Employee Declarations (Email/Forms)",
            "Target System": "Consolidated Excel\nDocusign Form",
            "Field Extraction": "Declaration Status (Positive/Negative)\nEmployee Response",
            "Expected Final Result": "Populated COI Forms",
            "Automation / AI Capabilities": "Text Analysis (Sentiment/Keyword)\nForm Pre-filling",
            "Data & Compliance Risk": "Confidential Employee Declarations",
            "Process Stability": "High"
        },
        25: { # PO Population
            "Source System": "DM Invoice (PDF)",
            "Target System": "SAP ME21N (PO Creation)",
            "Field Extraction": "SKU, Qty, Supplier, Batch, Date",
            "Expected Final Result": "Created Service PO in SAP",
            "Automation / AI Capabilities": "OCR\nSAP Automation",
            "Data & Compliance Risk": "Procurement Data",
            "Process Stability": "High"
        },
        26: { # Validate the Shopify
            "Source System": "Shopify Orders",
            "Target System": "Alert Email (Ops)\nArchive",
            "Field Extraction": "Cust Name, Address, Stock Level\nPrestige Item Count",
            "Expected Final Result": "Validated Orders\nAlerts for Dupes/Stockouts",
            "Automation / AI Capabilities": "Duplicate Detection\nAddress Validation Logic",
            "Data & Compliance Risk": "Customer Customer Data (PII)",
            "Process Stability": "Medium\nPlatform rules may change"
        },
        27: { # VN Duty Validation
            "Source System": "Customs Form Excel\nBL, Invoice, COO, Arrival PDF\nMaster Data",
            "Target System": "Validation Result",
            "Field Extraction": "Dates, Permit No, Invoice No\nVietnamese Descriptions",
            "Expected Final Result": "Cross-checked Duty Amounts",
            "Automation / AI Capabilities": "OCR (Vietnamese)\nExcel-to-Excel Comparison",
            "Data & Compliance Risk": "Customs Compliance",
            "Process Stability": "High"
        },
        28: { # HC validation
            "Source System": "ADP System\nManual Excel Report",
            "Target System": "Discrepancy Report",
            "Field Extraction": "Headcount Totals\nEmployee Lists",
            "Expected Final Result": "List of Mismatches",
            "Automation / AI Capabilities": "Data Reconciliation",
            "Data & Compliance Risk": "HR Data",
            "Process Stability": "High"
        },
        29: { # HC Evolution report
            "Source System": "Employee List\nLVMH HReporting\nBudget",
            "Target System": "Evolution Report (Excel)",
            "Field Extraction": "Market, Responsibility Code\nHeadcount",
            "Expected Final Result": "Budget vs Actual Breakdown",
            "Automation / AI Capabilities": "Data Pivot/Aggregation",
            "Data & Compliance Risk": "Sensitive HR Budget",
            "Process Stability": "Medium"
        },
        30: { # VAS quotation validation
            "Source System": "Maersk Quotation (Excel?)\nContract Rates",
            "Target System": "Validated Quotation",
            "Field Extraction": "Quoted Rate\nContract Rate",
            "Expected Final Result": "Approval/Rejection of Quote",
            "Automation / AI Capabilities": "Rate Lookup\nComparison",
            "Data & Compliance Risk": "Contract Pricing",
            "Process Stability": "Medium"
        },
        31: { # TW Duty Validation
            "Source System": "Import Declaration (PDF)\nShipment Tracking Excel",
            "Target System": "Excel Calculation (Duty)",
            "Field Extraction": "Doc Number, Product No, Qty\nDuty Amounts",
            "Expected Final Result": "Validated Duty Calculation",
            "Automation / AI Capabilities": "OCR\nData Cross-referencing",
            "Data & Compliance Risk": "Customs Financials",
            "Process Stability": "High"
        },
        32: { # MY Customs Form Extraction
            "Source System": "Import Decl PDFs (K1, K9, K8, ZB1)",
            "Target System": "Excel Summary",
            "Field Extraction": "Dates, Doc Numbers, Amounts\nContainer/Flight Codes",
            "Expected Final Result": "Extracted Dataset",
            "Automation / AI Capabilities": "OCR (Multi-format)\nTemplate Recognition",
            "Data & Compliance Risk": "Customs Data",
            "Process Stability": "Medium\nMultiple form types"
        },
        33: { # Ateis scanning cost validation
            "Source System": "SAP Scanning Transactions\nMaersk Excel File\nWeekly Schedule",
            "Target System": "Cost Validation Report",
            "Field Extraction": "Scanning Counts\nCompleted Volumes",
            "Expected Final Result": "Reconciled Cost Sheet",
            "Automation / AI Capabilities": "Data Matching (SAP vs Excel)",
            "Data & Compliance Risk": "Vendor Costing",
            "Process Stability": "Medium"
        },
        34: { # KR Duty Validation (POSM)
            "Source System": "Import Declaration (PDF)\nOnline Tariff Tool",
            "Target System": "Validation Result",
            "Field Extraction": "HS Code, Country\nDuty %",
            "Expected Final Result": "Duty Validation",
            "Automation / AI Capabilities": "Web Scraping (Tariff Tool)\nPDF Extraction",
            "Data & Compliance Risk": "Customs Data",
            "Process Stability": "High"
        },
        35: { # Carrier Invoices (Hapag Lloyd)
            "Source System": "Hapag Lloyd Invoices (PDF)",
            "Target System": "Invoices Summary File",
            "Field Extraction": "Billing Info",
            "Expected Final Result": "Populated Tracker",
            "Automation / AI Capabilities": "PDF Text Extraction\nStructured Data Parsing",
            "Data & Compliance Risk": "Billing Info",
            "Process Stability": "High"
        },
        36: { # VN Delivery Note Validation
            "Source System": "Customs Form PDF\nInvoice PDF\nDelivery Note PDF",
            "Target System": "Validation Check",
            "Field Extraction": "Product Desc, Qty",
            "Expected Final Result": "Match/Mismatch Flag",
            "Automation / AI Capabilities": "Cross-PDF Comparison",
            "Data & Compliance Risk": "Shipping Docs",
            "Process Stability": "High"
        },
        37: { # TW Harbour Service Fee Validation
            "Source System": "Harbour Service Fee PDF",
            "Target System": "Excel Calculation",
            "Field Extraction": "Amount, Doc Number",
            "Expected Final Result": "Validated Fee",
            "Automation / AI Capabilities": "OCR (Simple)",
            "Data & Compliance Risk": "Fee Data",
            "Process Stability": "High"
        },
        38: { # MY Duty Validation (POSM)
            "Source System": "Invoice PDF\nOnline Tariff Tool\nImport Decl PDF",
            "Target System": "Validation Report",
            "Field Extraction": "Product No, Qty, Price\nDuty %",
            "Expected Final Result": "Duty Verification",
            "Automation / AI Capabilities": "Web Lookup\nMulti-doc matching",
            "Data & Compliance Risk": "Customs Data",
            "Process Stability": "High"
        },
        39: { # TH RSP Extraction
            "Source System": "RSP PDF (Scanned)",
            "Target System": "Internal Excel",
            "Field Extraction": "License No, Product No, Price\nAlcohol %",
            "Expected Final Result": "Formatted Excel Data",
            "Automation / AI Capabilities": "OCR (Scanned Table)\nFormatting Logic",
            "Data & Compliance Risk": "Pricing Data",
            "Process Stability": "High"
        },
        40: { # TW Handling Fee Validation
            "Source System": "Handling Fee PDF",
            "Target System": "Excel Calculation",
            "Field Extraction": "Amount",
            "Expected Final Result": "Validated Amount",
            "Automation / AI Capabilities": "OCR (Scanned PDF?)",
            "Data & Compliance Risk": "Fee Data",
            "Process Stability": "High"
        }
    }
    
    # --- 2. Refinements (V2) ---
    refinements = {
        4: { # Opportunity 4: Invoice to Folder
            "Automation / AI Capabilities": "Email Filtering & Attachment Saving (Rule-based)" 
        },
        10: { # Forecasting of APAC POSM needs
             "Target System": "SAP (PO Creation) / Excel Report", 
             "Automation / AI Capabilities": "Forecasting Logic (Trend Analysis)" 
        },
        26: { # Validate Shopify
            "Automation / AI Capabilities": "Rule-based Validation (Duplicates, Stock Check)" 
        }
    }
    
    try:
        print(f"Reading {file_path}...")
        with open(file_path, 'r') as f:
            data = json.load(f)
    
        updated_count = 0
        refinement_count = 0
    
        # Apply V1
        for idx, item in enumerate(data):
            if idx in generated_data:
                gen = generated_data[idx]
                # Update specific fields
                item["Source System"] = gen.get("Source System", "")
                item["Target System"] = gen.get("Target System", "")
                item["Field Extraction"] = gen.get("Field Extraction", "")
                item["Expected Final Result"] = gen.get("Expected Final Result", "")
                item["Automation / AI Capabilities"] = gen.get("Automation / AI Capabilities", "")
                item["Data & Compliance Risk"] = gen.get("Data & Compliance Risk", "")
                item["Process Stability"] = gen.get("Process Stability", "")
                updated_count += 1
                
        # Apply V2 Refinements
        for idx, changes in refinements.items():
            if idx < len(data):
                for k, v in changes.items():
                    data[idx][k] = v
                    refinement_count += 1
    
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
            
        print(f"Success. Populated {updated_count} items and applied {refinement_count} refinements.")
        print(f"Saved to {output_path}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
