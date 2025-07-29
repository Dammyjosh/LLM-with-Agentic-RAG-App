# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Create Streamlit config directory and file to set server options
RUN mkdir -p /root/.streamlit
RUN echo "[server]" > /root/.streamlit/config.toml && \
    echo "headless = true" >> /root/.streamlit/config.toml && \
    echo "enableCORS = false" >> /root/.streamlit/config.toml && \
    echo "enableXsrfProtection = false" >> /root/.streamlit/config.toml && \
    echo "port = 8501" >> /root/.streamlit/config.toml && \
    echo "address = \"0.0.0.0\"" >> /root/.streamlit/config.toml

# Expose port 8501 for Streamlit
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "app.py"]





