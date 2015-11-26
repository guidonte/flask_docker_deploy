FROM ubuntu:14.04
MAINTAINER Guido Amoruso <guidonte@gmail.com>

RUN sudo apt-get -y update

RUN sudo apt-get -y install python-pip
RUN sudo apt-get -y install git
RUN sudo apt-get -y install ssh

RUN sudo pip install gunicorn==19.0
RUN sudo pip install flask==0.10

WORKDIR /srv/flask_docker_deploy
