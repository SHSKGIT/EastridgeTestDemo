FROM python:3.9

MAINTAINER JW

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /Eastridge/webapp

WORKDIR /Eastridge/webapp

ADD . /Eastridge/webapp

# update pip version. The python interpreter location is up to your computer.
# RUN python -m pip install --upgrade pip

RUN pip install -r requirements/base.txt

RUN chmod a+x ./start.sh