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
3) In jenkins create different jobs and create scripts as specified in the article.
