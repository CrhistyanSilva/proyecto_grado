#!/bin/bash
#SBATCH --job-name=imagenet32_pickles
#SBATCH --ntasks=1
#SBATCH --mem=8000
#SBATCH --time=10:00:00
#SBATCH --tmp=9G
#SBATCH --partition=normal
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --mail-user=cr.silper@gmail.com

source /etc/profile.d/modules.sh
source ~/anaconda/bin/activate
conda activate idf
cd ~/datasets/imagenet32/train/label1
python pickle_to_img.py
cd ~/datasets/imagenet32/validation/label1
python pickle_to_img_validation.py

