FROM python:3.10-slim
WORKDIR /app
COPY . /app
# ENV PYTHONPATH=/app
RUN pip install --no-cache-dir -r requirements.txt
USER root
CMD ["python", "gui/web_gui.py"]