# dl-challenge-prot
DL challenge from Proteinea

### Installation (Debian)
__1. Installing the required python version (python 3.6.15)__     
> Avoid installing the 3.6.0 It's too old and have lots of error with the new packages

- Install dependencies:     
    - `$ sudo apt update && sudo apt install libssl-dev openssl libbz2-dev liblzma-dev`      
- Building Python (specifing the folder to build on it)
    - Download the required version: `$ wget https://www.python.org/ftp/python/3.6.0/Python-3.6.15.tgz`
    - Unzipping the files: `$ tar zxf Python-3.6.15.tgz`
    - Change dir: `$ cd Python-3.6.15/`
    - Specify the folder to build on it:
        - create the folder: `$ sudo mkdir /opt/python-3.6`
        - specifying the folder for installation: `$ ./configure --prefix=/opt/python-3.6`
    - `$ make`
    - `$ sudo make install` __Waitting for the build to finish__ 😅😅😅😅
    - Use this version `$ /opt/python-3.6/bin/python3.6` _Great you have installed and run the specified py version_ 😎😎     

__2. Installing virtualenv:__ Refer to this [gist](https://gist.github.com/amshrbo/2ca0afb88c428b79ddaf38374226b9e0)       

__3. Creating and activating the venv:__        
- Create: `$ virtualenv --python=/opt/python-3.6/bin/python3.6 ~/venvpy/torch-cpu-py3.6`     
    - `$ --python` specifing the directory for the python version `$ ~/venvpy/torch-cpu-py3.6` the full path for the venv including the name
- Activate (fish shell): `$ . ~/venvpy/torch-cpu-py3.6/bin/activate.fish` __OR__ (Bash shell) `$ source ~/venvpy/torch-cpu-py3.6/bin/activate`       

__4. Upgrade pip:__ `$ python -m pip install --upgrade pip` make sure that your venv is activated

__5. Installing packages:__
1. pytorch: `pip3 install torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html`
2. other packages: `pip install ipython matplotlib jupyter tqdm`
3. downgrading jedi for autocomplete to work in jupyter: `pip install jedi==0.17.2`
