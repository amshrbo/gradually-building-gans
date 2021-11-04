# dl-challenge-prot
DL challenge from Proteinea

### Installation (Debian)
__1. Installing the required python version (python 3.6)__     
- Install dependencies:     
    - `sudo apt-get update && sudo apt-get install libssl-dev openssl`      
- Building Python (specifing the folder to build on it)
    - Download the required version: `wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz`
    - Unzipping the files: `tar zxf Python-3.6.0.tgz`
    - Change dir: `cd Python-3.6.0/`
    - Specify the folder to build on it:
        - create the folder: `sudo mkdir /opt/python-3.6`
        - specifying the folder for installation: `./configure --prefix=/opt/python-3.6`
    - `make`
    - `sudo make install` __Waitting for the build to finish__ 😅😅😅😅
    - Use this version `/opt/python-3.6/bin/python3.6` _Great you have installed and run the specified py version_ 😎😎     

__2. Installing virtualenv:__ Refer to this [gist](https://gist.github.com/amshrbo/2ca0afb88c428b79ddaf38374226b9e0)       

__3. Creating and activating the venv:__        
- Create: `virtualenv --python=/opt/python-3.6/bin/python3.6 ~/venvpy/tf-1`     
    - `--python` specifing the directory for the python version `~/venvpy/tf-1` the full path for the venv including the name
- Activate (fish shell): `. ~/venvpy/tf-1/bin/activate.fish` __OR__ (Bash shell) `source ~/venvpy/tf-1/bin/activate`       
