# Downloading sequencing data
## Installing sratool to download data
```bash
wget --output-document sratoolkit.tar.gz https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
tar -vxzf sratoolkit.tar.gz
```
## Downloading data
Data were downloaded from NCBI Sequence Read Archive (SRA) by project number -> Send results to Run selector -> Accession List (list SRR), metadata
```bash
./scripts/01_download_metagenomes.sh -i data/SRR_Acc_List_gupta.txt
```

# Evaluation of the quality of sequencing readings
## Environment preparation
```bash
micromamba create -f environment_fastqc.yml
micromamba activate venvfastqc 
```

## Script execution
```bash
./scripts/02_quality.sh -o qc_raw -i *_1.fastq.gz *_2.fastq.gz
```

## Creating a report on the quality of readings
```bash
./scripts/02_quality_res.py
```

# Filtering
## Activating the environment with Trimomatic
```bash
micromamba activate venvfastqc
```
## Script execution
```bash
./scripts/03_filter.sh
```
The resulting filtered readings are in the trimmed folder

# Taxonomic annotation
## Kraken
### Installation
```bash
git clone https://github.com/DerrickWood/kraken2.git  
 ./kraken2/install_kraken2.sh kraken_scripts  
```
### Download database
```bash
mkdir data    
cd data
wget -c https://genome-idx.s3.amazonaws.com/kraken/k2_standard_20251015.tar.gz  
tar -xzf k2_standard_20251015.tar.gz`
```
### Script execution
```bash
./scripts/04_kraken.sh
```
### Creating a table of species abundance
```bash
./scripts/04_kraken.py
```

## Metaphlan
### Environment preparation
```bash
micromamba create -f environment_metaphlan.yml
micromamba activate metaphlan4 
```
### Script execution
```bash
./scripts/04_metaphlan.sh
```

# Distance estimate
## Mash
### Installation
```bash
mkdir mash
cd mash
wget https://github.com/marbl/Mash/releases/download/v2.3/mash-Linux64-v2.3.tar
tar -xvf mash-Linux64-v2.3.tar
MASH=mash/mash-Linux64-v2.3/mash
```
### Script execution
```bash
./scripts/05_mash_dist.sh
```

# Feature extraction
## MetaFX
### Environment preparation
```bash
micromamba create -f environment_metafx.yml
micromamba activate metafx_env
git clone https://github.com/ctlab/metafx
cd metafx
export PATH=$PWD/bin:$PWD/bin/metafx-modules:$PWD/bin/metafx-scripts:$PATH
```
### Script execution
```bash
./scripts/06_metafx.sh
```






