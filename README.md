# Face-Recognition

This is the final project for CS308 Computer Vision course in 2023 Spring semester.



### Environment Setup

#### Operating System

**Ubuntu 20.04** is highly recommended.

Using Windows system may encounter crash in dependency installation stage.



#### Package Management

Using **anaconda3** to create a virtual environment, e.g. 

```bash
conda create -n cvproj python=3.8
```



After completion of virtual environment setup, download and install **deepface** dependency using the following instruction:

```bash
python -m pip install --upgrade pip
pip install deepface
```



### How to Run Code?

**Git clone this repository**:

```bash
git clone https://github.com/TonyZhang14242/Face-Recognition.git
```

**Make sure the current work directory** is `Face-Recognition` or the execution will crash with error.



After that, simply run, for example:

```bash
python verify.py
```



##### Execution is slow?

In execution process, the program will ask to download a model weight from Internet, and this is very slow, so we use the following method to boost this process:

i. switch to /home/{your user name}/.deepface/weights

ii. execute the following command to download weight file from another source:

```bash
wget -c https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
wget -c https://github.com/serengil/deepface_models/releases/download/v1.0/facial_expression_model_weights.h5
wget -c https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5
wget -c https://github.com/serengil/deepface_models/releases/download/v1.0/gender_model_weights.h5
wget -c https://github.com/serengil/deepface_models/releases/download/v1.0/race_model_single_batch.h5
```



After all these finished, you are set to go!
