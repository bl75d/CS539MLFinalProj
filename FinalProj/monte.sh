#!/bin/sh
#SBATCH --output=slurm_jobs/%j.out
#SBATCH -N 1
#SBATCH -n 40
#SBATCH --mem 64G
#SBATCH --gres=gpu:0
#SBATCH -p normal 
#SBATCH -t 02:00:00

while getopts ":w:e:" opt; do
  case $opt in
    w) width="$OPTARG"
    ;;
    e) epochs="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

source ~/.bashrc
venv test
# echo "python3 main.py --train --dir $SLURM_JOB_ID/ --epochs $epochs --layer_width $width"
# python3 main.py --train --dir $SLURM_JOB_ID/ --epochs $epochs --layer_width $width

# python3 results.py --monte
python3 results.py --monte