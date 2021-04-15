#!/bin/bash
#SBATCH --job-name=process_models
#SBATCH --ntasks=1
#SBATCH --mem=8000
#SBATCH --time=15:00:00
#SBATCH --tmp=9G
#SBATCH --partition=normal
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@mail
#SBATCH --output=%x_%j.out

source /etc/profile.d/modules.sh
source $CONDA_ACTIVATE
conda activate rc

cd ~/proyecto_grado/rc/RC-PyTorch/src
bash get_models.sh "$MODELS_DIR"
