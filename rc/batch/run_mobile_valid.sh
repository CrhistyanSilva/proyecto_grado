#!/bin/bash
#SBATCH --job-name=run_mobile_valid
#SBATCH --ntasks=1
#SBATCH --mem=16384
#SBATCH --time=12:00:00
#SBATCH --partition=normal
#SBATCH --qos=gpu
#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@mail
#SBATCH --output=%x_%j.out

source /etc/profile.d/modules.sh
source $CONDA_ACTIVATE
conda activate rc
cd ~/proyecto_grado/rc/RC-PyTorch/src
CUDA_VISIBLE_DEVICES=0 python -u run_test.py "$MODELS_DIR" 1109_1715 "AUTOEXPAND:$DATASET_DIR/mobile_valid" --restore_itr 1000000 --tau --clf_p "$MODELS_DIR/1115_1729 clf@down2_nonorm_down clf@model1715 exp_min=6.25e-06 lr.initial=0.0001 lr.schedule=exp_0.25_i50000 n_resblock=4/ckpts/ckpt_0000106000.pt" --qstrategy CLF_ONLY
