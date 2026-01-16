# Automation Opportunity Matrix Analysis

**Objective**: Map the 28 identified opportunities to a structured "Yes/No" matrix based on key Attributes and their specific Sub-Attributes.

## Proposed Matrix Structure

Instead of open-ended text fields, we will implement a Boolean (Yes/No) matrix. This allows for precise filtering and "heat map" analysis of the opportunities.

### 1. Attribute: Field Extraction
*What specific data points need to be captured?*

| Sub-Attribute | Description / Keywords Found | Frequency (Est) |
| :--- | :--- | :--- |
| **Price / Amount** | `price`, `amount`, `rate`, `tax`, `total`, `cost` | High |
| **Quantity** | `qty`, `quantity`, `volume`, `weight` | High |
| **Dates** | `date`, `arrival`, `year`, `month` | Medium |
| **Codes / IDs** | `sku`, `number`, `no`, `code`, `permit`, `license` | High |
| **Description** | `description`, `text`, `brand`, `name` | Medium |
| **Document Metadata** | `invoice no`, `po number`, `bl number` | Medium |

### 2. Attribute: Automation / AI Capabilities
*What technical action is being performed?*

| Sub-Attribute | Description / Keywords Found | Frequency (Est) |
| :--- | :--- | :--- |
| **Extraction (OCR)** | `extract`, `ocr`, `pdf to excel`, `read` | High |
| **Validation / Matching** | `validate`, `compare`, `match`, `check`, `reconcile` | Very High |
| **Classification** | `classify`, `sort`, `filter`, `router` | Low |
| **Generation / Creation** | `create`, `generate`, `populate`, `merge` | Medium |
| **Lookup / Retrieval** | `lookup`, `search`, `find` | Low |
| **Translation** | `translate` (e.g., Thai/Vietnamese to English) | Low |

### 3. Attribute: Source System
*Where does the data come from?*

| Sub-Attribute | Description / Keywords Found | Frequency (Est) |
| :--- | :--- | :--- |
| **PDF Document** | `pdf`, `scanned` | High |
| **Excel File** | `excel`, `spreadsheet` | High |
| **Email** | `email`, `mailbox` | Medium |
| **Web / Portal** | `portal`, `website`, `online tool` | Low |
| **SAP / ERP** | `sap`, `me21n` | Low |

### 4. Attribute: Target System
*Where does the data go?*

| Sub-Attribute | Description / Keywords Found | Frequency (Est) |
| :--- | :--- | :--- |
| **Excel Report** | `excel`, `calculation`, `tracker` | High |
| **SAP / ERP** | `sap`, `po`, `shipment creation` | Medium |
| **Email Notification** | `email`, `send`, `notify` | Medium |
| **File Storage** | `folder`, `drive`, `sharepoint` | Medium |

## Logic Mapping Example

Here is how specific opportunities would map to this new matrix:

**Opportunity 1: "VN Duty Validation"**
> *Description: Validate details in Customs Form Excel against B/L, Invoice, COO PDF...*
*   **Field Extraction**: `[x] Price/Amount`, `[x] Quantity`, `[x] Dates`, `[x] Codes/IDs`
*   **Automation**: `[x] Extraction`, `[x] Validation/Matching`, `[x] Translation`
*   **Source**: `[x] Excel`, `[x] PDF`
*   **Target**: `[x] Excel Report`

**Opportunity 2: "OCR automation (Carrier Invoices)"**
> *Description: Extract all PDF info... for payment...*
*   **Field Extraction**: `[x] Price/Amount`, `[x] Document Metadata`
*   **Automation**: `[x] Extraction`
*   **Source**: `[x] PDF`
*   **Target**: `[x] SAP`, `[x] Excel Report`

## Recommendation for Next Steps
1.  **Approve/Refine Definition**: Confirm if these 4 Main Attributes and their Sub-attributes cover your needs.
2.  **Generate Matrix**: I will programmatically generate this "Yes/No" table for all 28 items.
