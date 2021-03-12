FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN mkdir /denv
WORKDIR /denv
RUN apt-get update && \
        apt-get install -y \
        build-essential \
		ca-certificates \
	   	cmake \
	   	git \
	   	libgtk2.0-dev \
	   	pkg-config \
	   	libavcodec-dev \
	   	libavformat-dev \
	   	libswscale-dev \
		python3-dev \
		wget \
		netcat \
		libpoppler-cpp-dev \
        python-dev
COPY requirements.txt /denv/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /denv/