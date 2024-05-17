FROM python:3.10  

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Node.js and npm for TailwindCSS
RUN apt-get update && apt-get install -y --no-install-recommends nodejs

COPY . .

# Install Tailwind dependencies
RUN npm install

# Collect static files (includes compiled Tailwind CSS)
RUN collectstatic --no-input

EXPOSE 8000  

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver"]