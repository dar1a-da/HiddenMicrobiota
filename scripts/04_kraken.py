# Creation of a abundance table at the species

import os
import pandas as pd

REPORT_DIR = 'kraken_results/kraken_reports'
RANK='S'

tables = []

for file in os.listdir(REPORT_DIR):
    sample = file.replace('.report', '')
    path = os.path.join(REPORT_DIR, file)

    data = []
    with open(path) as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) < 6:
                continue

            percent = float(parts[0])
            clade_reads = int(parts[1])
            rank = parts[3]
            name = parts[5].strip()

            if rank == RANK:
                data.append((name, clade_reads))

    df = pd.DataFrame(data, columns=['taxon', sample])
    tables.append(df.set_index('taxon'))

final = pd.concat(tables, axis=1).fillna(0)

final['sum'] = final.sum(axis=1)
final = final.sort_values('sum', ascending=False)
final = final.drop(columns='sum')

final.to_csv('kraken_species_abundance.tsv', sep='\t')