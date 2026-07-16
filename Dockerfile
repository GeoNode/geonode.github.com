# Dockerfile to build and preview the GeoNode Jekyll website locally.
#
# Build the image:
#   docker build -t geonode-site .
#
# Preview at http://localhost:4000:
#   docker run --rm -p 4000:4000 geonode-site
#
# Live-reload while editing (mount the working tree):
#   docker run --rm -p 4000:4000 -v "$PWD":/site geonode-site
#
# Build only, writing the static site to ./_site (no server):
#   docker run --rm -v "$PWD":/site geonode-site bundle exec jekyll build

FROM ruby:3.3-slim

# System packages required to build native gem extensions (nokogiri, ffi, ...)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        git \
    && rm -rf /var/lib/apt/lists/*

# Install gems from a directory OUTSIDE the site tree, and point Bundler at it.
# This way, bind-mounting the working tree over /site for live-reload cannot
# shadow the Gemfile/Gemfile.lock, nor make Bundler resolve against a stale
# host Gemfile.lock. Gems live in /usr/local/bundle (the base image default).
ENV BUNDLE_GEMFILE=/deps/Gemfile
WORKDIR /deps
COPY Gemfile ./
RUN gem install bundler \
    && bundle install

# Site content. Bundler still reads the Gemfile from /deps (BUNDLE_GEMFILE),
# so the copied/mounted files here are treated purely as Jekyll sources.
WORKDIR /site
COPY . .

EXPOSE 4000

# --host 0.0.0.0 so the server is reachable from the host; --force_polling
# makes live-reload work reliably with mounted volumes.
CMD ["bundle", "exec", "jekyll", "serve", \
     "--host", "0.0.0.0", \
     "--port", "4000", \
     "--force_polling"]
