FROM centos:7
RUN yum install python36 -y
RUN yum install libSM -y
RUN yum install libXrender -y
RUN yum install libXext -y
RUN yum install python3-devel -y
RUN pip3 install opencv-python
RUN pip3 install keras
RUN pip3 install pandas
PUN pip3 install tensorflow
