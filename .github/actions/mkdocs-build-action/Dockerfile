FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install mkdocs && apt-get -y install pip && apt-get -y install lftp

RUN pip install markdown mkdocs-macros-plugin

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]