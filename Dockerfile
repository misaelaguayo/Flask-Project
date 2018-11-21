FROM python:3.6.6
COPY . /app
WORKDIR /app
ENV PIPENV_DONT_LOAD_ENV=1
RUN pip install pipenv
RUN pipenv run pip install -e .
RUN pipenv install --dev
EXPOSE 80
CMD ["pipenv", "run", "python", "flask_project/main.py"]