#start official python image
FROM python:3.9-slim

#make working directory
WORKDIR /app

#copy all the files to workdir.
COPY . /app

# install required packages using following command
RUN pip install -r requirement.txt

EXPOSE 80

CMD ["uvicorn", "fastapi_model:app", "--host", "0.0.0.0", "--port", "80"]

#build ------------ docker build -t fastapi-docker .


#run command -------docker run -p <host_port>:<container_port> <image_name>
#run   ------------ docker run -p 8080:80 fastapi-docker
# When you access http://localhost:8080 on your browser