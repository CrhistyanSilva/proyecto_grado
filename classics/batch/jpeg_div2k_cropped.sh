#!/bin/bash
#SBATCH --job-name=jpeg_div2k_cropped
#SBATCH --ntasks=1
#SBATCH --mem=16G
#SBATCH --time=12:00:00
#SBATCH --partition=normal
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@mail
#SBATCH --output=%x_%j.out

source /etc/profile.d/modules.sh
source $CONDA_ACTIVATE
conda activate lbb
cd ~/proyecto_grado/classics

python encode.py jpeg /clusteruy/home03/compresion_imgRN/DIV2K_valid_HR_cropped/ --delete --num_cores 18
