FROM centos:latest AS base
LABEL maintainer="zachary.wilson@outlook.com"
RUN yum update -y && yum install python3 -y && yum clean all
RUN adduser daemon
FROM base as app
USER daemon
WORKDIR /home/daemon
COPY requirements.txt .
RUN python3 -m pip install --user -r requirements.txt
