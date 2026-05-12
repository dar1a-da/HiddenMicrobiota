# Hidden Matters

## Introduction

Metagenomics studies the set of genes of all microorganisms present in an environmental sample, called a metagenome. 
Microbial communities play a key role in maintaining human health. Metagenomic sequencing is used to describe microbial communities in individuals, which helps identify a set of human microbes and understand how changes in the human microbiota correlate with changes in health.

The composition of the human microbiota is related to the state of health. The presence and representation of different bacterial species or families may correlate with certain diseases. In this work, the relationship of the human gut microbiota with arthritis was investigated. 
Data on the intestinal microbiota were obtained from genome-wide sequencing using the shot-gun method. Further, these raw data were processed using bioinformatic tools via the CLI and python. The results of bacterial representation, functional profiling, and pipeline were obtained.

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

## Methods

### bash
`FastQC` was used for quality control of sequence data before and after filtration. The sequences were filtered using a `Trimmomatic` with the following parameters: ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 (Remove adapters),  LEADING:3 (Remove leading low quality or N bases (below quality 3)), TRAILING:3 (Remove trailing low quality or N bases), SLIDINGWINDOW:4:20 (Scan the read with a 4-base wide sliding window, cutting when the average quality per base drops below 20), MINLEN:60 (Drop reads below 60 bases long).  
The `Kraken 2` was used for taxonomic classification based on k-mers. Kraken 2 is a fast and memory efficient tool for taxonomic assignment of metagenomics sequencing reads. The result was a abundance table at the species. The `MetaPhlAn` was used for taxonomic classification based on marker genes. MetaPhlan is a tool for profiling the composition of microbial communities from metagenomic shotgun sequencing data. Output files contain taxon abundances are listed one clade per line, tab-separated from the clade's relative abundance in %. `MetaFX` was used for feature extraction from whole-genome metagenome sequencing data and classification of groups of samples. The analysis was performed on k-mers of size 31. The results: feature table, table of samples categories, contigs in FASTA format as features for each category. `Mash` was used for estimating the distance between metagenomes. Splits sequences into k-mers, makes a MinHash sketch, compares sketches, and gets the distance. Results: table of distance between samples.  

### python
Preprocessing tables from Kraken2, MetaPhlan, Mash, MetaFX used `pandas`, `numpy`. Preprocessing includes creating metadata with sample group, selection taxonomic level.  
The Shannon index was used to calculate alpha diversity.  
`Matplotlib`, `seaborn` was used for visualization.  
Methods for reduction dimensions: `PCA`, `t-SNE`, `UMAP`.  
Machine learning (library scikit-learn) was used to train classification models. The `Random Forest` algorithm was used for the task of classifying and evaluating the features importances. Using the `SHAP` (SHapley Additive exPlanations) method, we evaluated how each feature affects the final prediction.


## Data

The data for the analysis of the intestinal microbiome in people with rheumatoid arthritis were taken from the article Gupta "Gut microbial determinants of clinically important improvement in patients with rheumatoid arthritis". The patients were selected from Mayo Clinic (USA). Sequencing data for stool metagenomes used in this study have been deposited at NCBI’s Sequence Read Archive (SRA) data repository (BioProject number PRJNA598446) 49 samples Illumina HiSeq 4000.

Metagenomes of healthy people were taken from [GMRepo](https://gmrepo.humangut.info/data). Project PRJEB28543. 48 samples.

## Results

### Taxonomic classification

Top-20 species from 

Kraken
![alt text](imgs/mean_rel_abund_kraken.png) 
MetaPhlan
![alt text](imgs/mean_rel_abund100_metaphlan.png)

### Alpha diversity

Alpha diversity was estimated by the Shannon index. This is a metric for determining the degree of homogeneity of the distribution of features of objects in the sample, for estimating the species diversity of a community.

$H = -\sum_{i=1}^{n} p_i \log_2 p_i$,  

where $p_i$ the number of features of the object.

![alt text](imgs/alpha_div_all.png)

The absolute index values for Kraken2 are systematically higher than for MetaPhlAn. These discrepancies are probably related to differences in the methodology of the taxonomic classification of Kraken2 and MetaPhlAn. Kraken accounts for a wider range of organisms, including unclassified potential contaminating organisms, whereas MetaPhlAn focuses on well-annotated bacterial markers and is more conservative.  
The Mann-Whitney test was used to evaluate the statistically significant difference within the method between patients and healthy people. As a result, it was found that the difference in the Shannon index between patients and healthy people is not significant: Kraken p-value 0.808, MetaPhlAn p-value: 0.119.
To assess the statistically significant difference between the methods, the Wilcoxon test was used, since the same sample was analyzed by two methods, the data are paired. It is shown that the difference between the methods in the Shannon index is statistically significant with a p-value of 1.67e-11.


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

