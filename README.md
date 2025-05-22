# Simple endpoint creation using FastAPI

This is a simple FastAPI application that demonstrates how to create an endpoint that returns a JSON response. The application includes a single endpoint `/hello` that returns a greeting message.


## Prerequisites
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the server)
- Pydantic (for data validation)
- Requests (for testing the endpoint)

## Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd simple-endpoint
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application
To run the FastAPI application, use the following command:
```bash
python main.py
```

## The application will start running on `http://localhost:8000`
Show the API documentation by navigating to `http://localhost:8000/docs` in your web browser. You can test the `/hello` endpoint directly from the documentation interface.