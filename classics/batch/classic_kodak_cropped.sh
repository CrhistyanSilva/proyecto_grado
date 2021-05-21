#!/bin/bash
#SBATCH --job-name=classic_mobile_cropped
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

python encode.py webp /clusteruy/home03/compresion_imgRN/kodak_cropped/ --delete --num_cores 18
python encode.py flif /clusteruy/home03/compresion_imgRN/kodak_cropped/ --delete --num_cores 18
