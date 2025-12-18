FROM ubuntu:24.04

USER root

# Install dependencies
RUN apt-get update && apt-get install -y \
                                ruby-full \
                                build-essential \
                                zlib1g-dev \
                                git \
                                graphicsmagick \
                                nodejs \
                                npm

USER ubuntu

# Configure Ruby Gems installation path
RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc

RUN echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc
RUN echo 'export LC_CTYPE=C.UTF-8' >> ~/.bashrc
RUN echo 'export LANG=C.UTF-8' >> ~/.bashrc

ENV GEM_HOME=/home/ubuntu/gems
ENV PATH=/home/ubuntu/gems/bin:$PATH

# Install Jekyll and Bundler gems
RUN gem install jekyll bundler