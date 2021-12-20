#!/bin/bash
#SBATCH --job-name=imagenet64_imgs_to_npy
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=26G
#SBATCH --time=3:00:00
#SBATCH --tmp=9G
#SBATCH --partition=normal
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@mail
#SBATCH --output=%x_%j.out

source /etc/profile.d/modules.sh
source $CONDA_ACTIVATE
conda activate lbb
cd ~/proyecto_grado/datasets
python images_to_npy.py -i /clusteruy/home03/compresion_imgRN/imagenet64/train/images/ -o /clusteruy/home03/compresion_imgRN/imagenet64/train/train_64x64_mitad.npy
