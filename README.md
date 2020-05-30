# MLOps Pipeline for Automated and better Training of ML Models 
MLops is the approach in which we combine the capabilities of ML(Machine Learning) and DevOps to create more automated and intelligent Machine Learning pipelines.In this project we are using the capabilities of MLOps to create better trained ML(Machine Learning) models by integrating ML with Git and Jenkins.
For more detailed desription please refer to following article: https://medium.com/@pranshul.tiwari97/mlops-pipeline-for-automated-better-training-of-ml-models-6c82056d09f7

## Getting Started
Follow these instructions to implement this project:
### Prerequisites
1) OS: Any Linux Distribution(Preferably RHEL or CentOS). This will act as host OS.
2) Docker-CE
3) Jenkins 
4) JDK(To run jenkins)
### Setup:
1) Install Docker-CE, Jenkins, JDK in this OS.
2) Create docker images using the two dockerfiles given in the repository.
  ```
  Command to create image: docker build -t <name of image> .
  ```
   In this case name of image in kerimage for image containing Keras and kmeansimage for image having scikit learn for running KMeans code.
3) In jenkins create different jobs and use shell scripts as specified in the article.
## Description
In this project 3 main objectives to be achieved are:
1) Train and increase accuracy of ANN model by doing necessary tweakings in it.
2) Train and increase accuracy of CNN model by doing necessary tweakings in it.
3) Create better clusters in KMeans by using WCSS method.
## Working
1) Developer uploads the code on github and from there webhook of github triggers job1 which downloads all the code in its workspace and then copies the code to /root/github directory of the base OS.
2) The program files have to be of specific format because then only checker.py file can analyse the type of code written in it. In the case of CNN and ANN the code has to be in the format of ann.py & CNN.py respectively.
3) Now checker.py file will run analyse the code and acoording to it's type it will create the container.
 ```
 For Example: If the code is of ANN format then container working on kerimage will be created by job-2.
 ```
4) Now job-3 will be triggered and in this firstly the accuracy of developer's code will be calculated firstly and then a loop will run in which at each iteration this code will be tweaked and accuracy will be calculated. In the case of ann and cnn following tweakings will be done:
 * In the first iteration in ANN number of dense layers will be insreased and in CNN number of CRP layers are being increased.
 * In the second iteration number of epochs are being changed in both CNN & ANN.
 * In the third iteration in ANN 2 more hidden layers are being increased and in CNN number of layers in FC layers are being increased.
 * In the fourth iteration in ANN number of neurons are being decreased and in CNN number of neurons in both CRP layers and FC layers      are being reduced.
 * In each iteraton accuracy is calculated after tweaking the model and if accuracy is found to be greater than 80% then loop is breaked    and a mail is sent to admin stating that model has been trained.
 * This tweaking continues until this level of accuracy is reached.
5) In tha case of KMeans the number of clusters which can be formed by a model is being calculated and for doing this WCSS method is used which calculates the WCSS value at different values of number of clusters and the value at which change in wcss is most(i.e it decreases drastically) then that value is considered to be the optimal number of clusters which can be created from that dataset and this point is called Elbow point.
