# Installation

micromamba create -n metaphlan4 -c conda-forge -c bioconda metaphlan=4 -y
micromamba activate metaphlan4

# Running on all samples

mkdir -p metaphlan_results

for f in trimmed/*_1_paired.fq.gz
do
    sample=$(basename "$f" _1_paired.fq.gz)

    metaphlan "trimmed/${sample}_1_paired.fq.gz,trimmed/${sample}_2_paired.fq.gz" \
        --input_type fastq \
        --nproc 8 \
        --force \
        --mapout "metaphlan_results/${sample}.bowtie2out.txt" \
        -o "metaphlan_results/${sample}.txt"
done

# Creation abundance table

merge_metaphlan_tables.py profiles/*.txt > merged_abundance_table.txt