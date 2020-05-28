ARG PYVER=3.7
FROM python:$PYVER
RUN pip install --upgrade pip
RUN pip install pytest pytest-only pylint
WORKDIR /usr/project
RUN which pytest
RUN which pylint
