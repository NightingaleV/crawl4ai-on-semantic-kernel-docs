FROM python:3.11-slim

# Build argument for port with default value
ARG PORT=8001
ENV PORT=${PORT}

WORKDIR /app

# Copy the application code
COPY . .

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxcomposite1 libxrandr2 libgbm1 libpangocairo-1.0-0 libasound2 libwayland-client0 libxkbcommon0 && rm -rf /var/lib/apt/lists/*


# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN crawl4ai-setup
RUN playwright install --with-deps

# Expose the port from build argument
EXPOSE ${PORT}

# Command to run the application
#CMD ["sh", "-c", "uvicorn pydantic_ai_expert_endpoint:app --host 0.0.0.0 --port ${PORT}"]
#CMD ["sh", "-c", "crawl4ai-setup && playwright install"]