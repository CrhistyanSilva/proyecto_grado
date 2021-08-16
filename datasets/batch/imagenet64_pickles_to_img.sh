#!/bin/bash
#SBATCH --job-name=imagenet64_pickle_to_imgs
#SBATCH --ntasks=1
#SBATCH --mem=25G
#SBATCH --time=3:00:00
#SBATCH --tmp=9G
#SBATCH --partition=normal
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@mail

source ~/anaconda/bin/activate
cd ~/proyecto_grado/datasets
python pickle_to_img.py /clusteruy/home03/compresion_imgRN/imagenet64/training/pickles/ /clusteruy/home03/compresion_imgRN/imagenet64/training/images/