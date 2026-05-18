micromamba install trimmomatic -c bioconda

mkdir trimmed

JAR=$(find "$CONDA_PREFIX" -maxdepth 5 -type f -name "*trimmomatic*.jar" | head -n 1)
echo "Using jar: $JAR"

for r1 in *_1.fastq.gz
do
    sample=${r1%_1.fastq.gz}
    r2=${sample}_2.fastq.gz

    if [ -f "$r2" ]; then
        echo "Processing $sample"

        java -Xmx8g -jar "$JAR"  PE -threads 12 -phred33 \
        "$r1" "$r2" \
        trimmed/${sample}_1_paired.fq.gz trimmed/${sample}_1_unpaired.fq.gz \
        trimmed/${sample}_2_paired.fq.gz trimmed/${sample}_2_unpaired.fq.gz \
        ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 \
        LEADING:3 TRAILING:3 \
        SLIDINGWINDOW:4:20 \
        MINLEN:60
    else
        echo "WARNING: Missing $r2"
    fi
done