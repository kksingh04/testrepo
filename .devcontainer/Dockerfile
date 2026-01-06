FROM mcr.microsoft.com/devcontainers/python:2-3.14-bookworm

# Install Git LFS
RUN apt-get update && \
    apt-get install -y git-lfs && \
    git lfs install && \
    apt-get clean && rm -rf /var/lib/apt/lists/*