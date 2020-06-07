ARG PYVER=3.7
FROM python:$PYVER
RUN pip install --upgrade pip
RUN pip install pytest pytest-only pylint pdoc3
COPY tooling/docker/scripts/pydoc-html.sh /usr/scripts/pydoc-html.sh
RUN ln -s /usr/scripts/pydoc-html.sh /usr/local/bin/pydoc-html
WORKDIR /usr/project
RUN which pytest
RUN which pylint
RUN which pydoc-html
