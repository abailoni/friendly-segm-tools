# Segmfriends
Bunch of tools and experiments for image segmentation


## Install
### Basic version from conda
This version can run all the clustering/segmentation algorithms included the package:

- Clone the repository: `git clone https://github.com/abailoni/segmfriends.git`
- `cd ./segmfriends`
- To install the package, you will need [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Once you have it, run `conda create -n segmFr -c abailoni -c conda-forge gasp`
- Activate your new environment with `conda activate segmFr`
- `python setup.py install` (or `python setup.py develop` if you plan to work on the package)

### Full version 
If you plan to work on the package or run the deep-learning tools in it, you will need to install some extra packages (including [inferno](https://github.com/abailoni/inferno), [speedrun](https://github.com/abailoni/speedrun), [neurofire](https://github.com/abailoni/neurofire), [ConfNets](https://github.com/imagirom/ConfNets/tree/multi-scale-unet), ...):

- Clone the repository: `git clone https://github.com/abailoni/segmfriends.git`
- `cd ./segmfriends`
- `chmod +x ./install_full_dependencies.sh`
- To install the dependencies, you will need [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Install the dependencies and the package by running `./install_full_dependencies.sh`. While the script is running, you will need to confirm twice.
- The script will create a new conda environment called `segmFriends` including everything. You can activate your new environment with `conda activate segmFr`


