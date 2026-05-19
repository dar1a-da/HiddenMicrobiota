# Installation

git clone https://github.com/DerrickWood/kraken2.git  
 ./kraken2/install_kraken2.sh kraken_scripts  

# Download database

mkdir data    
wget -c https://genome-idx.s3.amazonaws.com/kraken/k2_standard_20251015.tar.gz  
tar -xzf k2_standard_20251015.tar.gz`

# Running on all samples

mkdir -p kraken_results

for r1 in trimmed/*_1_paired.fq.gz
do
    sample=$(basename $r1 _1_paired.fq.gz)
    r2=trimmed/${sample}_2_paired.fq.gz

    echo "Processing $sample"

    kraken2 \
      --db /path/to/db  \
      --threads 16 \
      --paired \
      --report kraken_results/${sample}.report \
      --output kraken_results/${sample}.kraken \
      "$r1" "$r2"
done