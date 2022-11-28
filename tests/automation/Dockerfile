FROM python:3.7

COPY tests/automation/install_system_dependencies.sh ./
RUN ./install_system_dependencies.sh

COPY requirements.txt requirements_dev.txt ./
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    pip install -r requirements_dev.txt
