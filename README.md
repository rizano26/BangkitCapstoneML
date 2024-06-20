# Bangkit Capstone ML for AIReal
End to End ML Progress for the AIReal Application <br>

![image](https://github.com/Aireal-C241-PS337/machine-learning/assets/100218015/a97202de-c2b8-405c-b235-fe6923cea185)

1. **Searching for Dataset and Perform Data Augmentation**<br>
The dataset used to create the model consists of 88.882 E-commerce product images, including 44.441 blurred images and 44.441 non-blurred images. The non-blurred images are sourced from one of the following Kaggle datasets: [Fashion Product Images Small](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small). The blurred images are generated from the non-blurred images through data augmentation using the OpenCV library in Python. The complete link to the dataset is [here](https://drive.google.com/file/d/1SaSjZ-z6W0v3nTGQIQsczaUxN-JbzN9C/view?usp=sharing).
2. **Data Pre-processing**<br>
In this process, normalization is performed by dividing each pixel in the image by 255 so that the pixel values in the image range between 0 and 1. Additionally, the data is split into training data and validation data with a ratio of 80:20, where 80% is for training data and 20% is for validation data.
3. **Creating a Blur and Non Blur Image Classification Model**<br>
In this process, a model is created to detect blurred and non-blurred images using a Convolutional Neural Network (CNN). The model will accept color images with a size of 60x80 as input. A Dense layer with a Sigmoid activation function is used in the output layer. The complete architecture of the model is as follows:
![Arsitektur Model](https://github.com/Aireal-C241-PS337/machine-learning/assets/100218015/8bc2ed5f-e6e8-4f23-8813-5d31491c2876)
The model will be trained using the binary_crossentropy loss function with the Adam optimizer for 5 epochs. The model achieves a validation accuracy of approximately 99% after the training process. Below is the graph of training accuracy and validation accuracy for each epoch:<br>
![accuracy line chart test](https://github.com/Aireal-C241-PS337/machine-learning/assets/100218015/121aa062-741e-4e79-bcaf-48cb4aca9a44)
4. **Deploy Model to Production**<br>
After the model is completed, it will be saved in [.H5 format](https://drive.google.com/file/d/1XXFRWWVcB_ERbSWkDyWmAYRukrMm5jTk/view). Next, the model is converted into a format that can be used by the Cloud Computing team for deployment using TensorFlow Serving.
