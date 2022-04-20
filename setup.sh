# Create and activate conda environment
mamba env create -f environment.yml -p ~/envs/ligo
conda activate ligo

# Install kernel for jupyter notebook
python -m ipykernel install --user --name ligo --display-name "Python 2"