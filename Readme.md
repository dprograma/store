# Store Management API Documentation

## Overview

This documentation provides details on installationa/setup and the API endpoints for managing items and suppliers in the inventory system. The API allows for the creation, retrieval, updating, and deletion of items and suppliers, as well as querying suppliers for a given item and items for a given supplier.

## Installation and Setup

1. Clone the repository.
    ```bash
    git clone https://github.com/dprograma/store.git
    ```
2. Create a virtual environment
    ```bash
    python3 -m venv venv
    ```
3. Activate the virtual environment
    ```bash
    source venv/bin/activate # for Mac/Linux
    venv\Scripts\activate # for Windows
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Make bash file for static validation executable
    ```
    chmod +x static_validation.sh
    ```
6. Run static validation (isort, black, migration, pylint, mypy, pytest)
    ```
    ./static_validation.sh
    ```
4. Run the development server:
    ```bash
    python manage.py runserver
    ```

# API Endpoints

## Base URL

All API endpoints are prefixed with `/api/`.


## Endpoints

### Items

#### List all items

- **URL:** `/api/items/`
- **Method:** `GET`
- **Description:** Retrieve a list of all items in the store.
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": [
            {
                "id": 1,
                "name": "Item 1",
                "description": "Description for item 1",
                "price": 10.00,
                "suppliers": [1, 2]
            },
            ...
        ]
    }
    ```

#### Retrieve a single item

- **URL:** `/api/items/{id}/`
- **Method:** `GET`
- **Description:** Retrieve a single item by its ID.
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": {
            "id": 1,
            "name": "Item 1",
            "description": "Description for item 1",
            "price": 10.00,
            "suppliers": [1, 2]
        }
    }
    ```

#### Create a new item

- **URL:** `/api/items/`
- **Method:** `POST`
- **Description:** Create a new item.
- **Request Body:**
    ```json
    {
        "name": "New Item",
        "description": "This is a new item",
        "price": 15.00,
        "suppliers": [1, 2]
    }
    ```
- **Response:**
    - `201 Created` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": {
            "id": 3,
            "name": "New Item",
            "description": "This is a new item",
            "price": 15.00,
            "suppliers": [1, 2]
        }
    }
    ```

#### Update an existing item

- **URL:** `/api/items/{id}/`
- **Method:** `PUT`
- **Description:** Update an existing item.
- **Request Body:**
    ```json
    {
        "name": "Updated Item",
        "description": "This is an updated item",
        "price": 20.00,
        "suppliers": [1, 2]
    }
    ```
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": {
            "id": 1,
            "name": "Updated Item",
            "description": "This is an updated item",
            "price": 20.00,
            "suppliers": [1, 2]
        }
    }
    ```

#### Delete an item

- **URL:** `/api/items/{id}/`
- **Method:** `DELETE`
- **Description:** Delete an item.
- **Response:**
    - `204 No Content` on success
    ```json
    {
        "status": "success",
        "response_code": "00"
    }
    ```

### Suppliers

#### List all suppliers

- **URL:** `/api/suppliers/`
- **Method:** `GET`
- **Description:** Retrieve a list of all suppliers in the store.
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": [
            {
                "id": 1,
                "name": "Supplier 1",
                "contact": "Contact details for supplier 1"
            },
            ...
        ]
    }
    ```

#### Retrieve a single supplier

- **URL:** `/api/suppliers/{id}/`
- **Method:** `GET`
- **Description:** Retrieve a single supplier by its ID.
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": {
            "id": 1,
            "name": "Supplier 1",
            "contact": "Contact details for supplier 1"
        }
    }
    ```

#### Create a new supplier

- **URL:** `/api/suppliers/`
- **Method:** `POST`
- **Description:** Create a new supplier.
- **Request Body:**
    ```json
    {
        "name": "New Supplier",
        "contact": "Contact details for the new supplier"
    }
    ```
- **Response:**
    - `201 Created` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": {
            "id": 3,
            "name": "New Supplier",
            "contact": "Contact details for the new supplier"
        }
    }
    ```

#### Update an existing supplier

- **URL:** `/api/suppliers/{id}/`
- **Method:** `PUT`
- **Description:** Update an existing supplier.
- **Request Body:**
    ```json
    {
        "name": "Updated Supplier",
        "contact": "Updated contact details for the supplier"
    }
    ```
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": {
            "id": 1,
            "name": "Updated Supplier",
            "contact": "Updated contact details for the supplier"
        }
    }
    ```

#### Delete a supplier

- **URL:** `/api/suppliers/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a supplier.
- **Response:**
    - `204 No Content` on success
    ```json
    {
        "status": "success",
        "response_code": "00"
    }
    ```

### Suppliers for a specific item

#### Retrieve suppliers for a given item

- **URL:** `/api/items/{id}/suppliers/`
- **Method:** `GET`
- **Description:** Retrieve suppliers associated with a specific item.
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": [
            {
                "id": 1,
                "name": "Supplier 1",
                "contact": "Contact details for supplier 1"
            },
            ...
        ]
    }
    ```

### Items for a specific supplier

#### Retrieve items for a given supplier

- **URL:** `/api/supplier/{id}/items/`
- **Method:** `GET`
- **Description:** Retrieve items associated with a specific supplier.
- **Response:**
    - `200 OK` on success
    ```json
    {
        "status": "success",
        "response_code": "00",
        "response": [
            {
                "id": 1,
                "name": "Item 1",
                "description": "Description for item 1",
                "price": 10.00
            },
            ...
        ]
    }
    ```

## Error Responses

### General Error Response

- **Response:**
    ```json
    {
        "status": "error",
        "response_code": "99",
        "response": "Error message"
    }
    ```

- **Response Codes:**
    - `99` represents the error code for all failed requests.

## Models and Serializers

### Item Model

- **Fields:**
    - `id`: Integer, primary key
    - `name`: String, name of the item
    - `description`: String, description of the item
    - `price`: Decimal, price of the item
    - `suppliers`: Many-to-many relationship with Supplier model

### Supplier Model

- **Fields:**
    - `id`: Integer, primary key
    - `name`: String, name of the supplier
    - `contact`: String, contact details of the supplier

### Item Serializer

- **Fields:**
    - `id`
    - `name`
    - `description`
    - `price`
    - `suppliers`

### Supplier Serializer

- **Fields:**
    - `id`
    - `name`
    - `contact`

