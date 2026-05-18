micromamba create -n venvfastqc
micromamba activate venvfastqc 

micromamba install -c bioconda fastqc

fastqc -t 8 -o qc_raw *_1.fastq.gz *_2.fastq.gz