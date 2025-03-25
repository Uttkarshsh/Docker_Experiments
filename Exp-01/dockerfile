# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Keeps Python from generating .pyc files in the container


# Install pip requirements
COPY requirement.txt .
RUN python -m pip install -r requirement.txt

WORKDIR /code
COPY src /code/src


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["streamlit", "run", "src/stream.py"]
