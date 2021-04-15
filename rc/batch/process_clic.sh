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
source $CONDA_ACTIVATE
conda activate rc

cd ~/proyecto_grado/rc/datasets

cd ~/proyecto_grado/rc/RC-PyTorch/src
bash prep_bpg_ds.sh A9_17 "$DATASET_DIR/mobile_valid"
bash prep_bpg_ds.sh A9_17 "$DATASET_DIR/professional_valid"
