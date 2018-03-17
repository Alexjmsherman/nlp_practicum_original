# conda cheat sheet
- https://conda.io/docs/_downloads/conda-cheatsheet.pdf


### CONDA INSTALLATION
**create a basic conda environment**

conda create --name guild

	**create an environment with Python 3.6 and all anaconda packages**

	conda create --name guild python=3.6 anaconda -y

#### RESOLVE ERRORS
**run the below code, if you run into errors, such as**
- **An error downloading a .dll file**
- **CondaError: PermissionError(13, 'Permission denied')**

conda clean --all --yes

### ENVIRONMENTS
**list conda environments**

conda env list

### INSTALL PACKAGES SETUP
**add conda-forge to provide ease of access to install python packages**

conda config --add channels conda-forge


### JUPYTER NOTEBOOK SETUP
**add new kernel to jupyer notebook to access kernel**- http://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments
https://stackoverflow.com/questions/37433363/link-conda-environment-with-jupyter-notebook

Type the following commands:
	- source activate guild
	- conda install nb_conda
	- python -m ipykernel install --user --name myenv --display-name "guild environment"

#### RESOLVE ERRORS
**identify which python version is running in Jupyter notebook**
- import sys
- sys.executable
##### if it is the correct python version, try the following
conda install ipykernel --name Python3


### RESOURCES:
**conda vs pip vs virtualenv**
https://conda.io/docs/_downloads/conda-cheatsheet.pdf

**Video: Managing python environments with conda**
https://www.youtube.com/watch?v=EGaw6VXV3GI

**Effectively using open source with conda**
ppt: https://www.slideshare.net/teoliphant/effectively-using-open-source-with-conda

**Create a virtual env with conda**
http://uoa-eresearch.github.io/eresearch cookbook/recipe/2014/11/20/conda/