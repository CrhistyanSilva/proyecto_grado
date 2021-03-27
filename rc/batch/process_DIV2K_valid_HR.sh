#!/bin/bash
#SBATCH --job-name=process_DIV2K_valid_HR
#SBATCH --ntasks=1
#SBATCH --mem=8192
#SBATCH --time=10:00:00
#SBATCH --tmp=9G
#SBATCH --partition=normal
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --mail-user=maria.gabriela.rodriguez@fing.edu.uy
#SBATCH --output=%x_%j.out

source /etc/profile.d/modules.sh
source ~/miniconda3/bin/activate
conda activate rc

cd ~/proyecto_grado/rc/datasets

wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_HR.zip
unzip DIV2K_valid_HR.zip

cd ~/proyecto_grado/rc/RC-PyTorch/src
bash prep_bpg_ds.sh A9_17 $RC_ROOT/datasets/DIV2K_valid_HR
