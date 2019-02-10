FROM ubuntu:16.04

# Set noninteractive mode
ARG DEBIAN_FRONTEND=noninteractive

# System Updates
RUN apt-get -y update && \
	apt-get --no-install-recommends -y install apt-utils

# Adding wget and bzip2
RUN apt-get install -y wget bzip2 

# Anaconda installing
RUN wget https://repo.continuum.io/archive/Anaconda3-5.3.1-Linux-x86_64.sh
RUN bash Anaconda3-5.3.1-Linux-x86_64.sh -b
RUN rm Anaconda3-5.3.1-Linux-x86_64.sh

# Set path to conda
ENV PATH /root/anaconda3/bin:$PATH

# Updating Anaconda packagess
RUN conda update conda
RUN conda update anaconda
RUN conda update --all

# Install CCXT
RUN pip install ccxt

# Configuring access to Jupyter
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py

# Prep our /app directory
WORKDIR /app
COPY . /app/


