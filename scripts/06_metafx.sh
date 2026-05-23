# Installation

micromamba create -n metafx_env -c conda-forge -c bioconda python=3.8
micromamba activate metafx_env
micromamba install -c conda-forge -c bioconda \
    numpy=1.24 \
    pandas=1.5 \
    scikit-learn=1.2 \
    matplotlib=3.7 \
    joblib \
    ete3=3.1.3 \
    xgboost

git clone https://github.com/ctlab/metafx
cd metafx

export PATH=$PWD/bin:$PWD/bin/metafx-modules:$PWD/bin/metafx-scripts:$PATH

# Creation sample_list_train.txt

for f in *_merged.fastq.gz
do
    abs="$(pwd)/$f"
    if [[ $f == ERR* ]]; then
        echo -e "$abs\thealth"
    elif [[ $f == SRR* ]]; then
        echo -e "$abs\tdisease"
    fi
done > sample_list_train.txt

# Extract features from samples

metafx unique -t 16 -m 128G -w wd_unique -k 31 -i sample_list_train.txt

# Создались kmers.bin
metafx unique -t 16 -m 128G -w wd_unique -k 31 -i sample_list_train.txt --kmers-dir /wd_unique/kmers/kmers


# Validation
# Train classification model for category prediction

metafx cv -t 2 -w wd_cv_train -f wd_unique_train/feature_table.tsv -i wd_unique_train/samples_categories.tsv -n 2 --grid

# Process new samples with hidden categories

ls *_merged.fastq.gz | sed 's|^|/mnt/tank/scratch/dchekanova/data_paper/all/test/|' > test_files.txt

metafx calc_features -t 16 -m 128G -w wd_new_samples -k 31 -d wd_unique_train \
        -i $(cat /mnt/tank/scratch/dchekanova/data_paper/all/test/test_files.txt)

# Get prediction results for new samples

metafx predict -w wd_predict -f wd_new_samples/feature_table.tsv --model wd_cv_train/rf_model_cv.joblib
