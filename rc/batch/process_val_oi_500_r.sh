#!/bin/bash
#SBATCH --job-name=process_val_oi_500_r
#SBATCH --ntasks=1
#SBATCH --mem=8192
#SBATCH --time=10:00:00
#SBATCH --tmp=9G
#SBATCH --partition=normal
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@mail
#SBATCH --output=%x_%j.out

source /etc/profile.d/modules.sh
source ~/miniconda3/bin/activate
conda activate rc

cd ~/proyecto_grado/rc/datasets

wget http://data.vision.ee.ethz.ch/mentzerf/validation_sets_lossless/val_oi_500_r.tar.gz
mkdir val_oi_500_r && pushd val_oi_500_r
tar xvf ../val_oi_500_r.tar.gz

cd ~/proyecto_grado/rc/RC-PyTorch/src
bash prep_bpg_ds.sh A9_17 $RC_ROOT/datasets/val_oi_500_r
