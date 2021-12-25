# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
RUN git clone https://github.com/f0ns1/Network-fingerprinting.git /project

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /project

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r tfm/requirements.txt

## SCAPY

RUN apt-get update && \
    apt-get install -y \
    zip \
    unzip \
    python \
    python-pyx \
    python-matplotlib \
    tcpdump \
    python-crypto \
    graphviz \
    imagemagick \
    gnuplot \
    python-gnuplot \
    libpcap-dev && apt-get clean

ADD https://github.com/secdev/scapy/archive/master.zip /tmp/master.zip
RUN unzip /tmp/master.zip -d /usr/local/ && rm /tmp/master.zip

RUN apt-get update && \
    apt-get -qq -y install \
    bridge-utils \
    net-tools \
    iptables \
    python \
    tcpdump \
    build-essential \
    python-dev \
    libnetfilter-queue-dev \
    python-pip

RUN pip install scapy
#RUN pip install NetfilterQueue



VOLUME /project

EXPOSE 8080
WORKDIR /project/tfm

RUN ls .

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]
