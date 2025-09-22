FROM astral/uv:python3.11-bookworm

RUN echo "alias ll='ls -alF'" >> ~/.bashrc
RUN echo "alias cls='clear; printf \"\033[3J\"'" >> ~/.bashrc

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

WORKDIR  /usr/src/app

ENV UV_LINK_MODE=copy
<<<<<<< HEAD
ENV PYTHONPYCACHEPREFIX=/var/tmp/.pycache 
=======
ENV PYTHONPYCACHEPREFIX=/tmp/__pycache__
>>>>>>> main

RUN \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync \
    --no-install-project

ENTRYPOINT ["bash"]
