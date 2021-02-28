FROM ruby:3.0.0-buster

RUN gem install \
        deep_merge

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint
COPY yaml-merge.rb /usr/local/bin/yaml-merge

RUN chmod +x \
        /usr/local/bin/docker-entrypoint \
        /usr/local/bin/yaml-merge

WORKDIR /yaml

VOLUME ["/yaml"]

ENTRYPOINT ["docker-entrypoint"]
