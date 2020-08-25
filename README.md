# SciPy 2018 Tutorial: Pandas .head() to .tail()
## First-Time Setup

#### 1. Install Python

If you don't already have a working python distribution, you may download one of

* Miniconda ([https://conda.io/miniconda.html](https://conda.io/miniconda.html))
* Python.org  ([https://www.python.org/downloads/](https://www.python.org/downloads/))

You'll need Python 3.

#### 2. Download Tutorial Materials

This GitHub repository is all that is needed in terms of tutorial content. The simplest solution is to download the material using this link:

[https://github.com/deniederhut/Pandas-Tutorial-SciPyConf-2018/archive/master.zip](https://github.com/deniederhut/Pandas-Tutorial-SciPyConf-2018/archive/master.zip)

If you're familiar with Git, you can also clone this repository with:

```sh
git clone git@github.com:deniederhut/Pandas-Tutorial-SciPyConf-2018.git
```

It will create a new folder named Pandas-Tutorial-SciPyConf-2018/ with all the
content you will need, including:

- `requirements.txt` - the package requirements for this tutorial
- `check_environment.py` - a script for testing your installation
- `notebooks/` - the Jupyter notebooks we'll use during the tutoral

#### 3. Install Required Packages

If you are using conda, you can install the necessary packages by opening a terminal and entering the following:

```sh
conda update conda --yes
conda --version  # Should be about 4.5.4
conda env create --file=environment.yml
conda activate pandas-scipy
```

If you are using Python from python.org or your system, you can install the necessary packages by opening a terminal and entering the following:

```sh
# Create a new environment
python3 -m venv pandas-scipy
source pandas-scipy/bin/activate

pip install -U pip wheel setuptools
pip install -U -r requirements.txt
```

#### 4. Test the Installation

To make sure everything was installed correctly, open a terminal, and change its directory (`cd`) so that your working directory is `Pandas-Tutorial-SciPyConf-2018`. The enter the following:

```sh
python check_environment.py
```

#### 5. Start the Notebook

```sh
jupyter notebook
```
## About me

**Piyush Pathak**

[**PORTFOLIO**](https://anirudhrapathak3.wixsite.com/piyush)

[**GITHUB**](https://github.com/piyushpathak03)

[**BLOG**](https://medium.com/@piyushpathak03)


# 📫 Follw me: 

[![Linkedin Badge](https://img.shields.io/badge/-PiyushPathak-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/piyushpathak03/)](https://www.linkedin.com/in/piyushpathak03/)

<p  align="right"><img height="100" src = "https://media.giphy.com/media/l3URDstnIjBNY7rwLB/giphy.gif"></p>


