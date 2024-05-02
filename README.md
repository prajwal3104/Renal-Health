<h1 align="center">Renal Health Classification: Enhancing Diagnostic Precision!!</h1>
<p style="text-align:center;">
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="LICENCE" target="_blank">
    <img alt="License: ISC" src="https://img.shields.io/badge/License-ISC-yellow.svg" />
  </a>
  <a href="https://twitter.com/Prajwal_b_k" target="_blank">
    <img alt="Twitter: Prajwal_b_k" src="https://img.shields.io/twitter/follow/Prajwal_b_k.svg?style=social" />
  </a>
</p>

> In this repo, you will find a demonstration of how to build a Renal Health Classification model. The model is trained using Transfer Learning and the VGG16 architecture.

## Prerequisites 📋

- [AWS](https://aws.amazon.com/) | [AWS CLI](https://aws.amazon.com/cli/)
- [DVC](https://dvc.org/) | [DVC1.17](https://dvc.org/doc/install)
- [Python](https://www.python.org/) | [Python3.8](https://www.python.org/downloads/release/python-380/)
- [MLFlow](https://mlflow.org/) | [MLFlow1.19](https://mlflow.org/docs/latest/quickstart.html)
- [TensorFlow](https://www.tensorflow.org/) | [TensorFlow2.5](https://www.tensorflow.org/install/pip)

## Model Architecture 🏗️


```
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_1 (InputLayer)        [(None, 224, 224, 3)]     0         
                                                                 
 block1_conv1 (Conv2D)       (None, 224, 224, 64)      1792      
                                                                 
 block1_conv2 (Conv2D)       (None, 224, 224, 64)      36928     
                                                                 
 block1_pool (MaxPooling2D)  (None, 112, 112, 64)      0         
                                                                 
 block2_conv1 (Conv2D)       (None, 112, 112, 128)     73856     
                                                                 
 block2_conv2 (Conv2D)       (None, 112, 112, 128)     147584    
                                                                 
 block2_pool (MaxPooling2D)  (None, 56, 56, 128)       0         
                                                                 
 block3_conv1 (Conv2D)       (None, 56, 56, 256)       295168    
                                                                 
 block3_conv2 (Conv2D)       (None, 56, 56, 256)       590080    
                                                                 
 block3_conv3 (Conv2D)       (None, 56, 56, 256)       590080    
                                                                 
 block3_pool (MaxPooling2D)  (None, 28, 28, 256)       0         
                                                                 
 block4_conv1 (Conv2D)       (None, 28, 28, 512)       1180160   
                                                                 
 block4_conv2 (Conv2D)       (None, 28, 28, 512)       2359808   
                                                                 
 block4_conv3 (Conv2D)       (None, 28, 28, 512)       2359808   
                                                                 
 block4_pool (MaxPooling2D)  (None, 14, 14, 512)       0         
                                                                 
 block5_conv1 (Conv2D)       (None, 14, 14, 512)       2359808   
                                                                 
 block5_conv2 (Conv2D)       (None, 14, 14, 512)       2359808   
                                                                 
 block5_conv3 (Conv2D)       (None, 14, 14, 512)       2359808   
                                                                 
 block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         
                                                                 
 flatten (Flatten)           (None, 25088)             0         
                                                                 
 dense (Dense)               (None, 4)                 100356    
                                                                 
=================================================================
Total params: 14815044 (56.51 MB)
Trainable params: 100356 (392.02 KB)
Non-trainable params: 14714688 (56.13 MB)
_________________________________________________________________
```

```
(venv) prajwal@PK-2 Renal-Health % dvc dag
+----------------+            +--------------------+ 
| data_ingestion |            | prepare_base_model | 
+----------------+*****       +--------------------+ 
         *             *****             *           
         *                  ******       *           
         *                        ***    *           
         **                        +----------+      
           **                      | training |      
             ***                   +----------+      
                ***             ***                  
                   **         **                     
                     **     **                       
                  +------------+                     
                  | evaluation |                     
                  +------------+
```

## Getting Started 🚀

### How to run the project

1. Clone the repository
```bash
git clone https://github.com/prajwal3104/Renal-Health.git
```
2. Create a virtual environment
```bash
python3.8 -m venv venv
```
3. Activate the virtual environment
```bash
source venv/bin/activate
```
4. Install the requirements
```bash
pip install -r requirements.txt
```
5. Run the project or the pipeline's
```bash
python main.py
```


## Author 👤

* Website: [Prajwaal.dev](http://prajwaal.dev)
* Twitter: [Prajwal_b_k](https://twitter.com/Prajwal_b_k)
* Github: [prajwal3104](https://github.com/prajwal3104)
* LinkedIn: [prajwal-kumbar](https://www.linkedin.com/in/prajwal-kumbar)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/prajwal3104/Renal-Health/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2024 [Prajwal](https://github.com/prajwal3104).<br />
This project is [MIT](LICENCE) licensed.
