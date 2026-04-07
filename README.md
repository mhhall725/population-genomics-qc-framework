# Genomic Data Pipeline: v9 Analysis Framework

A modular Python-based pipeline designed for the ingestion, quality control (QC), and processing of high-volume genomic datasets. 

## Project Architecture
- **`data/`**: (Local Only) Encrypted/Private directory for raw genomic source files (e.g., v9 Registered Tier data).
- **`scripts/`**: Modular Python components for data processing and analysis.
- **`results/`**: Automated output directory for QC reports and processed statistical summaries.

## Current Phase: Phase 1 - Automated Ingestion & QC
The pipeline currently implements a hardened ingestion module (`01_data_ingestion.py`) featuring:
- **Automated Logging:** Full traceability of data loading events using the Python `logging` library.
- **QC Protocol:** Immediate generation of descriptive statistics (Mean, Std, Quartiles) to verify data distribution before analysis.
- **Error Handling:** Robust `try-except` blocks to manage file-path integrity and CSV corruption.

## Technical Stack
- **Language:** Python 3.14
- **Libraries:** Pandas, NumPy
- **Version Control:** Git/GitHub

## How to Run
1. Ensure a valid CSV is present in the `data/` directory.
2. Execute the ingestion module:
   ```bash
   python scripts/01_data_ingestion.py
