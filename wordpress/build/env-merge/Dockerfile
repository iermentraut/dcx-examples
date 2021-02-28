FROM python:3.7.6-slim-stretch

ENV DEBIAN_FRONTEND=noninteractive
ENV USER=docker
ENV GROUP=docker
ENV UID=1000
ENV GID=1000

USER root

RUN \
    addgroup docker \
    && adduser \
        "$USER" \
        --gecos "" \
        --disabled-password \
        --ingroup "$GROUP" \
        --shell /bin/bash \
        --uid "$UID"

VOLUME ["/app"]
WORKDIR /app

RUN \
    pip install pip --upgrade \
    && pip install \
        checksumdir==1.2.0 \
        python-dotenv==0.15.0
    # && pip install -U "python-dotenv[cli]"

COPY --chown=docker:docker ./merge-env.py /home/docker/merge-env.py

COPY ./docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

USER docker

ENTRYPOINT ["docker-entrypoint.sh"]
