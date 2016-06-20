FROM ubuntu:14.04

# Install system dependencies
RUN apt-get -yqq update
RUN apt-get -yqq upgrade
RUN apt-get -yqq install make \
						 python-setuptools \
						 gcc \
						 python-dev

RUN easy_install pip

# Copy the needed files to the container
ADD content/ /opt/blog/content/
ADD themes/ /opt/blog/themes/
ADD pelicanconf.py \
    requirements.txt \
    buildAndServe.sh \
    /opt/blog/

# Change working dir
WORKDIR /opt/blog/

# Install Pelican and depencies with pip
RUN pip install -r requirements.txt

# Generate site and serve
CMD /bin/bash -c "source buildAndServe.sh"

# Expose web server port
EXPOSE 8000