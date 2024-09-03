# E-Commerce API Overview

## Description

This API is an e-commerce solution built with FastAPI and MongoDB. It is designed to handle user management, products,
and shopping carts, using JWT authentication and a Domain-Driven Design (DDD) architecture.

## Environment Setup

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running with Docker

1. Build and start the services:
    ```bash
    docker-compose up --build
    ```
2. Access the API at [http://localhost:8000](http://localhost:8000)

## Architecture

The project follows Domain-Driven Design (DDD) principles to ensure clear separation of concerns and easy scalability.

- **Users**: User management, authentication, and authorization.
- **Products**: Product management and stock control.
- **Shopping Carts**: Management of shopping carts and their items.

## API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

- [Swagger UI](http://localhost:8000/docs)
- [Redoc](http://localhost:8000/redoc)

## Testing

To run the tests:

```bash
pytest
