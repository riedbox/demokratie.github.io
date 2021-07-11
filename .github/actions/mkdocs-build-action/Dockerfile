FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install mkdocs && apt-get -y install pip

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]