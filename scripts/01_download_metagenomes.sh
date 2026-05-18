wget --output-document sratoolkit.tar.gz https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
tar -vxzf sratoolkit.tar.gz
export PATH=$PWD/sratoolkit.3.0.0-ubuntu64/bin:$PATH

while read line; do
  fasterq-dump -e 8 ${line}
done<Accession_list.txt