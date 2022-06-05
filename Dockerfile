FROM python:3.8-alpine

ENV DATABASE_URL=postgresql://user:password@db:5432/db
COPY . /

WORKDIR /

RUN pip install -r requirements.txt

CMD ["sh", "-c", "./wait_for db:5432 -- alembic upgrade head && uvicorn main:app --host=0.0.0.0 --workers=3"]
EXPOSE 8000