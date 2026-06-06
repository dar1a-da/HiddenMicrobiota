while [[ $# -gt 0 ]]; do
    case "$1" in
        -i|--input)
            INPUT="$2"
            shift 2
            ;;
    esac
done

while read -r line; do
    sratoolkit.3.4.1-ubuntu64/bin/fasterq-dump -e 8 "$line"
done < "$INPUT"