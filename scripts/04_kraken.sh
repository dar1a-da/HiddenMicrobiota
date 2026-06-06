mkdir -p kraken_results

for r1 in trimmed/*_1_paired.fq.gz
do
    sample=$(basename $r1 _1_paired.fq.gz)
    r2=trimmed/${sample}_2_paired.fq.gz

    echo "Processing $sample"

    kraken2 \
      --db data/  \
      --threads 16 \
      --paired \
      --report kraken_results/${sample}.report \
      --output kraken_results/${sample}.kraken \
      "$r1" "$r2"
done