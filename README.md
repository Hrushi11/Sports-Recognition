# Sports-Recognition

Collection of sports images covering 73 different sports.. Images are 224,224,3 jpg format. Data is separated into train, test and valid directories. Additional a csv file is includes for those that wish to use it to create there own train, test and validation datasets.

![IMG](https://i.ibb.co/wh7LpYm/download.jpg)

Model Summary: 

```
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_layer (InputLayer)     [(None, 224, 224, 3)]     0         
_________________________________________________________________
data_augmentation_layer (Seq (None, None, None, 3)     0         
_________________________________________________________________
efficientnetb0 (Functional)  (None, None, None, 1280)  4049571   
_________________________________________________________________
global_average_pooling (Glob (None, 1280)              0         
_________________________________________________________________
output_layer (Dense)         (None, 73)                93513     
=================================================================
Total params: 4,143,084
Trainable params: 874,953
Non-trainable params: 3,268,131
```
