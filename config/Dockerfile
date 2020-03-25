FROM ubuntu:latest AS base
RUN apt-get update -y && apt-get install curl -y
RUN adduser conda
USER conda
WORKDIR /home/conda
RUN curl --silent -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && ~/miniconda3/bin/conda init
RUN . ~/.bashrc
COPY ./requirements.txt .
RUN conda install --file requirements.txt
