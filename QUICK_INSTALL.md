# How to install TensorFlow?
Here, we describe how to install TensorFlow using conda with support for
GPU computing.  We assume a 64-bit Linux system, with a CUDA-capable
graphics card.  We assume that Python 3.6+ is used.


## Intralling Miniconda
If you have Miniconda already installed, you can skip ahead to the next
section, if Miniconda is not installed, we start with that. Download the
Bash script that will install it from
[conda.io](https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh) using, e.g., `wget`:
```bash
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
Once downloaded, run the script:
```bash
$ bash Miniconda3-latest-Linux-x86_64.sh
```
You will be asked a number of questions.

1. First, the installer will let you have to review the
    license, press enter as requested.  The license is shown, read it,
    hitting the space bar for the next pages.  If you agree, type "yes"
    when requested.
1. The installer will suggest an installation directory, `miniconda3` in
    your home directory.  Bear in mind that, depending on the number of
    conda environments you wish to have, and the number of Python packages,
    you might be better of installing this in your `$VSC_DATA`
    directory.  So if your VSC user ID is vsc98765, and your account's
    affiliation is `my_uni` (either `antwerpen`, `brussel`, `gent`, or
    `leuven`), then the directory could be changed to
    `/data/my_uni/987/vsc98765/miniconda3`.  Typically, your home
    directory will do though.  Either press return to accept the installer's
    suggestion, or enter your own, and pressing return to proceed.
1. The installation will now proceed.
1. Next, the installer will offer to permanently add the path to the
    Miniconda installation to the `PATH` environment variable in your
    `.bashrc` file.  This is convenient, but may lead to conflicts when
    working with the module system, so make sure that you know what you
    are doing in either case.


## GitHub repository
A [GitHub repository](https://github.com/gjbex/Astrohack) has been set up
that contains information and conda environment defintion files.  The
most convenient way to proceed is to clone that repository.
```bash
$ git clone https://github.com/gjbex/Astrohack.git
```


## Creating an environment
First, ensure that the Miniconda installation is in your `PATH`.  The
following command should return the full path to the `conda` command:
```bash
$ which conda
```
If the result is blank, or reports that `conda` can not be found, modify
the `PATH` environment variable appropriately by adding Miniconda's
`bin` directory to `PATH`.

The GitHub repository you just cloned has two YAML files that define
conda enviroments for TensorFlow, a version for
[GPU](Environments/tensorflow.yml), and another for
[CPU only](Environments/tensorflow_non_gpu.yml).

Change to the repository's `Environment` directory:
```bash
$ cd Astrohack/Environments
```

Now you can create the conda environment for GPU or CPU, i.e., for GPU:
```
$ conda env create -f tensorflow.yml
```

Similarly for CPU-only environment:
```bash
$ conda env create -f tensorflow_non_gpu.yml
```


## Testing the installation
In order to test whether the installation was successful, first ensure
the correct conda environment is active:
```bash
$ source activate tensorflow
```
Next, start a Python interpreter:
```bash
$ python
```
A very short sequence of Python statements should confirm that TensorFlow
is installed correctly.
```python
>>> import tensorflow as tf
```
You will get pretty verbose output about the CUDA and cuDNN libraries
being loaded, and the availabilty of a CUDA-capable GPU.
```python
>>> hello = tf.constant('hello TensorFlow!')
>>> session = tf.Session()
>>> session.run(hello)
b'hello TensorFlow!'
```
When you reach this point, we wish you happy deep learning!
