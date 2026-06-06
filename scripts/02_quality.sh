#fastqc -t 8 -o qc_raw *_1.fastq.gz *_2.fastq.gz

while [[ $# -gt 0 ]]; do
    case "$1" in
        -o|--output)
            OUTDIR="$2"
            shift 2
            ;;
        -i|--input)
            shift
            INPUTS=("$@")
            break
            ;;
    esac
done

if [[ ${#INPUTS[@]} -eq 1 && -d "${INPUTS[0]}" ]]; then
    FILES=("${INPUTS[0]}"/*.fastq.gz)
else
    FILES=("${INPUTS[@]}")
fi

fastqc -t 8 -o "$OUTDIR" "${FILES[@]}"