FROM python:3.10 

# RUN python -m venv /env
# ENV PATH /env/bin:$PATH

WORKDIR /lounge-app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# Install Node.js and npm for TailwindCSS
RUN apt-get update && apt-get install -y --no-install-recommends nodejs npm

# Install Tailwind dependencies
RUN npm install

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--worker-class", "gevent", "--worker-connections", "1000", "--workers", "3", "lounge.wsgi:application"]