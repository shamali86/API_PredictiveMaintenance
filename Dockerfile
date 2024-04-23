# Base Image
FROM python:3.11

WORKDIR /api

# push all files into a folder as app in the docker image
COPY . .

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir -r /api/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "MachineFailurePredictor:api", "--host", "0.0.0.0", "--port", "8000"]

