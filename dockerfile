FROM python:3.9-slim
WORKDIR /app
COPY app.py .
COPY movie_list.pkl .
COPY similarity.pkl .

RUN pip install streamlit pickleshare==0.7.5
EXPOSE 8501

CMD ["streamlit", "run", "app.py","--server.address=0.0.0.0"]
