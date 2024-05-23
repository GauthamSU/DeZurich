FROM python:3.10  

WORKDIR /lounge-app

COPY requirements.txt /lounge-app
RUN pip install -r requirements.txt

# Install Node.js and npm for TailwindCSS
RUN apt-get update && apt-get install -y --no-install-recommends nodejs npm

COPY . /lounge-app

# Install Tailwind dependencies
RUN npm install

EXPOSE 8000  

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver"]