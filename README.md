# Face-Recognition

This is the final project for CS308 Computer Vision course in 2023 Spring semester.

<img src=".\docs\HYQ_sim.png" alt="HYQ_sim" style="zoom:67%;" />

<img src=".\docs\HYQ_info.png" alt="HYQ_info" style="zoom:67%;" />

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
pip install matplotlib
pip install jupyterlab
```



### How to Run Code?

**Git clone this repository**:

```bash
git clone https://github.com/TonyZhang14242/Face-Recognition.git
```

**Make sure the current work directory** is `Face-Recognition` or the execution will crash with error.



After that, simply run, for example:

```bash
python comparison.py
```

Also, we've provided a jupyter notebook (*recognition.ipynb*) to offer a more instinctive and interactive way to show results.
You can simply open this in jupyter lab and select the above environment as kernal to run this piece of code.



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

### Contribution

[张镇涛](https://github.com/TonyZhang14242)

[黎宇杰](https://github.com/Dystractor)

[宋一鸣](https://github.com/iddbh)

### Reference

[1] S. I. Serengil and A. Ozpinar, "LightFace: A Hybrid Deep Face Recognition Framework," 2020 Innovations in Intelligent Systems and Applications Conference (ASYU), Istanbul, Turkey, 2020, pp. 1-5, doi: 10.1109/ASYU50717.2020.9259802.

[2] S. I. Serengil and A. Ozpinar, "HyperExtended LightFace: A Facial Attribute Analysis Framework," 2021 International Conference on Engineering and Emerging Technologies (ICEET), Istanbul, Turkey, 2021, pp. 1-4, doi: 10.1109/ICEET53442.2021.9659697.
