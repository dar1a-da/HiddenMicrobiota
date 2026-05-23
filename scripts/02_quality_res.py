import os
import zipfile
import pandas as pd

QC_DIR = "qc_raw"

def parse_fastqc_data(zip_path):
    total = None
    seqlen = None

    with zipfile.ZipFile(zip_path, "r") as z:
        data_file = [f for f in z.namelist() if f.endswith("fastqc_data.txt")][0]
        with z.open(data_file) as fh:
            for raw in fh:
                line = raw.decode().strip()
                if line.startswith("Total Sequences"):
                    total = int(line.split()[-1])
                elif line.startswith("Sequence length"):
                    seqlen = line.split()[-1]
                if total and seqlen:
                    break
    return total, seqlen


rows = []

for file in os.listdir(QC_DIR):
    if file.endswith("_1_fastqc.zip"):
        sample = file.replace("_1_fastqc.zip", "")
        r1_zip = os.path.join(QC_DIR, file)
        r2_zip = os.path.join(QC_DIR, sample + "_2_fastqc.zip")

        total_reads, r1_len = parse_fastqc_data(r1_zip)

        if os.path.exists(r2_zip):
            _, r2_len = parse_fastqc_data(r2_zip)
        else:
            r2_len = None

        rows.append([sample, total_reads, r1_len, r2_len])

df = pd.DataFrame(rows, columns=["sample", "total_reads", "read1_length", "read2_length"]).sort_values("sample")
