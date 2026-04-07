import pandas as pd
import os
import logging

# Standard logging configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants for file system paths
DATA_INPUT = "data/v9_sample.csv"
QC_OUTPUT = "results/summary_stats.txt"

def run_ingestion_pipeline(file_path):
    """
    Loads genomic datasets and performs initial quality control checks.
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return

    try:
        # Load dataset into memory
        df = pd.read_csv(file_path)
        logging.info(f"Ingestion complete. Shape: {df.shape}")

        # Execute descriptive statistical analysis
        stats = df.describe()
        
        # Export validation report to results directory
        with open(QC_OUTPUT, "w") as f:
            f.write("=== Ingestion QC Report ===\n")
            f.write(f"Source: {file_path}\n")
            f.write(f"Sample Count: {len(df)}\n\n")
            f.write(stats.to_string())

        logging.info(f"QC report generated: {QC_OUTPUT}")
        
    except Exception as e:
        logging.error(f"Ingestion error: {e}")

if __name__ == "__main__":
    run_ingestion_pipeline(DATA_INPUT)