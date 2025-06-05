// filepath: d:\BootCampDIO\BOAS-PRATICAS-PARA-IAS\inline-completions\nodejs-products-api\src\routes\productRoutes.js
const express = require('express');
const ProductController = require('../controllers/productController');
const validationMiddleware = require('../middlewares/validationMiddleware');

const router = express.Router();
const productController = new ProductController();

// Route to create a new product with input validation
router.post('/products', validationMiddleware.validateProductCreation, productController.createProduct.bind(productController));

// Route to delete a product by ID
router.delete('/products/:id', productController.deleteProduct.bind(productController));

// Route to get all products
router.get('/products', productController.getAllProducts.bind(productController));

// Route to update a product by ID with input validation
router.put('/products/:id', validationMiddleware.validateProductUpdate, productController.updateProduct.bind(productController));

module.exports = router;