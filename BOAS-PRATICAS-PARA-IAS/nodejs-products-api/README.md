# Node.js Products API

This project is a RESTful API for managing products using Node.js and Express. It provides endpoints for creating, retrieving, updating, and deleting products, along with input validation to ensure data integrity.

## Project Structure

```
nodejs-products-api
├── src
│   ├── controllers
│   │   └── productController.js  # Contains the ProductController class with methods for handling product-related requests.
│   ├── models
│   │   └── product.js              # Defines the Product model representing the product data structure.
│   ├── routes
│   │   └── productRoutes.js        # Sets up the routes for the product management API.
│   ├── middlewares
│   │   └── validationMiddleware.js  # Contains middleware functions for validating incoming request data.
│   └── app.js                      # Entry point of the application, initializes the Express app and sets up middleware and routes.
├── package.json                     # Configuration file for npm, listing dependencies and scripts.
└── README.md                       # Documentation for the project, including setup instructions and API usage.
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd nodejs-products-api
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the application:**
   ```bash
   npm start
   ```

## API Endpoints

### Create a Product
- **Endpoint:** `POST /products`
- **Request Body:**
  ```json
  {
    "name": "Product Name",
    "price": 100,
    "description": "Product Description"
  }
  ```
- **Response:**
  - **201 Created** on success with the created product object.

### Get All Products
- **Endpoint:** `GET /products`
- **Response:**
  - **200 OK** with an array of product objects.

### Update a Product
- **Endpoint:** `PUT /products/:id`
- **Request Body:**
  ```json
  {
    "name": "Updated Product Name",
    "price": 150,
    "description": "Updated Product Description"
  }
  ```
- **Response:**
  - **200 OK** on success with the updated product object.

### Delete a Product
- **Endpoint:** `DELETE /products/:id`
- **Response:**
  - **204 No Content** on success.

## Testing the API

You can use tools like Insomnia or Postman to test the API endpoints. Make sure to set the appropriate HTTP methods and request bodies as specified above.

## License

This project is licensed under the MIT License.