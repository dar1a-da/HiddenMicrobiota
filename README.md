# Hidden Matters

## Introduction / short describe

Metagenomics

The composition of the human microbiota is related to the state of health. The presence and representation of different bacterial species or families may correlate with certain diseases. In this work, the relationship of the human gut microbiota with arthritis was investigated. 
Data on the intestinal microbiota were obtained from genome-wide sequencing using the shot-gun method. Further, these raw data were processed using bioinformatic tools via the SLI and python. The results of bacterial representation, functional profiling, and pipeline were obtained.

## Goal: 
Search for diagnostics markers for diseases classification based on WGS human gut samples

### Objectives:
- Literature review
- Dataset selection and preprocessing
- Identification of significant features:
    - Taxonomic analysis
    - Functional analysis
    - k-mer analysis
- Training of classification models
- Development of a reproducible data analysis pipeline
- Annotation and interpretation of identified features

## Workflow

### bash
Quality control &mdash; `FastQC`  
Filtration &mdash; `Trimmomatic`  
Taxonomic analysis &mdash; `Kraken2` (k-mers), `MetaPhlAn` (marker genes)  
Feature extraction &mdash; `MetaFX`  
Estimating the distance between metagenomes MinHash &mdash; `Mash`  

### python
Preprocessing tables from Kraken2, MetaPhlan use библиотеки ?? python pandas numpy.  
Визуализация с использованием matplotlib, seaborn.  
Методы снижения размерности PCA, t-SNE, UMAP. 
Machine learning scikit-learn.




## Data

The data for the analysis of the intestinal microbiome in people with rheumatoid arthritis were taken from the article Gupta "Gut microbial determinants of clinically important improvement in patients with rheumatoid arthritis". The patients were selected from Mayo Clinic (USA). Sequencing data for stool metagenomes used in this study have been deposited at NCBI’s Sequence Read Archive (SRA) data repository (BioProject number PRJNA598446) 49 samples Illumina HiSeq 4000.

Metagenomes of healthy people were taken from [GMRepo](https://gmrepo.humangut.info/data).

## Results

Альфа разнообразие (разные таксоном аннот)
Методы снижения размерности
Иерархическая кластеризация mash
Модели
Признаки


## Bibliography

Gupta, V.K., Cunningham, K.Y., Hur, B. et al. Gut microbial determinants of clinically important improvement in patients with rheumatoid arthritis. Genome Med 13, 149 (2021). https://doi.org/10.1186/s13073-021-00957-0

Wood, D.E., Salzberg, S.L. Kraken: ultrafast metagenomic sequence classification using exact alignments. Genome Biol 15, R46 (2014). https://doi.org/10.1186/gb-2014-15-3-r46

Blanco-Míguez, A., Beghini, F., Cumbo, F. et al. Extending and improving metagenomic taxonomic profiling with uncharacterized species using MetaPhlAn 4. Nat Biotechnol 41, 1633–1644 (2023). https://doi.org/10.1038/s41587-023-01688-w

Artem Ivanov, Vladimir Popov, Maxim Morozov, Evgenii Olekhnovich, Vladimir Ulyantsev, MetaFX: feature extraction from whole-genome metagenomic sequencing data, Bioinformatics, Volume 42, Issue 2, February 2026, btag018, https://doi.org/10.1093/bioinformatics/btag018

[FastQC](https://github.com/s-andrews/fastqc)  
[Trimmomatic](https://github.com/usadellab/trimmomatic)  
[Kraken 2](https://github.com/DerrickWood/kraken2)  
[Metaphlan](https://github.com/biobakery/MetaPhlAn)  
[MetaFX](https://github.com/ctlab/metafx)  
[Mash](https://mash.readthedocs.io/en/latest/)

