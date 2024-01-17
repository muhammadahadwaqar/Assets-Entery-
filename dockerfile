FROM python:3.9-slim
WORKDIR /entry-image
COPY ./ /entry-image/
CMD [ "python", "main.py"]
#terminal
#docker image build -t entry-app:1.0 ./
#docker tag entry-app:1.0 muhammadahad2121/entry-app:1.0