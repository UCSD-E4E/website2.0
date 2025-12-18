FROM ubuntu:24.04

USER root

# Install dependencies
RUN apt-get update && apt-get install -y \
                                ruby-full \
                                build-essential \
                                zlib1g-dev \
                                git

USER ubuntu

# Configure Ruby Gems installation path
RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc

ENV GEM_HOME=/home/ubuntu/gems
ENV PATH=/home/ubuntu/gems/bin:$PATH

# Install Jekyll and Bundler gems
RUN gem install jekyll bundler