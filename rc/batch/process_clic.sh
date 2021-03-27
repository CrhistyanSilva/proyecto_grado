#!/bin/bash
#SBATCH --job-name=process_clic
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

wget https://data.vision.ee.ethz.ch/cvl/clic/mobile_valid_2020.zip
unzip mobile_valid_2020.zip
mv valid mobile_valid 

wget https://data.vision.ee.ethz.ch/cvl/clic/professional_valid_2020.zip
unzip professional_valid_2020.zip
mv valid professional_valid

cd ~/proyecto_grado/rc/RC-PyTorch/src
bash prep_bpg_ds.sh A9_17 $RC_ROOT/datasets/mobile_valid
bash prep_bpg_ds.sh A9_17 $RC_ROOT/datasets/professional_valid
