# FROM centos:latest AS base
# LABEL maintainer="zachary.wilson@outlook.com"
# ENV PYTHONUNBUFFERED=1
# RUN yum update -y && yum install java python3 -y && yum clean all

# FROM base AS dev
# RUN yum update -y && yum install bash-completion man-pages -y && yum clean all
# RUN adduser python3
# USER python3
# WORKDIR /home/python3
# COPY requirements.txt .
# RUN python3 -m pip install --user -r requirements.txt

# FROM ubuntu:latest AS base
# RUN apt-get update -y && apt-get install curl -y
# RUN adduser conda
# USER conda
# WORKDIR /home/conda
# RUN curl --silent -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
#     && sh Miniconda3-latest-Linux-x86_64.sh -b \
#     && ~/miniconda3/bin/conda init
# RUN . ~/.bashrc
# COPY ./requirements.txt .
# RUN conda install --file requirements.txt

FROM continuumio/miniconda3:latest AS base

LABEL maintainer="Zachary Wilson"
LABEL maintainer.email="wilsonze@gmail.com"

ENV PYTHONUNBUFFERED=1

# next command is due to jre install bug
RUN mkdir -p /usr/share/man/man1/

RUN apt-get update -y && apt-get install default-jre -y

WORKDIR /code
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
