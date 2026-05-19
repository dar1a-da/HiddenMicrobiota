mkdir mash
wget https://github.com/marbl/Mash/releases/download/v2.3/mash-Linux64-v2.3.tar
tar -xvf mash-Linux64-v2.3.tar
./mash

MASH=/path/to/mash/mash-Linux64-v2.3/mash

mkdir -p mash_sketches

for r1 in *_R1.fq.gz
do
    sample=$(basename "$r1" _R1.fq.gz)
    r2="${sample}_R2.fq.gz"

    $MASH sketch -r -m 2 -o "mash_sketches/${sample}" -k 21 -s 1000000 "$r1" "$r2"
done

$MASH paste mash_all.msh mash_sketches/*.msh

$MASH dist mash_all.msh mash_all.msh > mash_dist.tsv