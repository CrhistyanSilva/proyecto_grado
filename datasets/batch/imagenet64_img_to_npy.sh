#!/bin/bash
#SBATCH --job-name=imagenet64_imgs_to_npy
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
python images_to_npy.py /clusteruy/home03/compresion_imgRN/imagenet64/training/images/ /clusteruy/home03/compresion_imgRN/imagenet64/training/train_64x64.npy