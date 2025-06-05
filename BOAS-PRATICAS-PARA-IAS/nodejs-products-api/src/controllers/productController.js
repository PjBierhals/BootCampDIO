const Product = require('../models/product'); // Import the Product model

class ProductController {
    // Method to create a new product
    async createProduct(req, res) {
        try {
            const { name, price, description } = req.body; // Destructure the request body

            // Create a new product instance
            const product = new Product({ name, price, description });
            await product.save(); // Save the product to the database

            res.status(201).json({ message: 'Product created successfully', product }); // Respond with success message and product data
        } catch (error) {
            res.status(500).json({ message: 'Error creating product', error }); // Handle errors
        }
    }

    // Method to retrieve all products
    async getAllProducts(req, res) {
        try {
            const products = await Product.find(); // Fetch all products from the database
            res.status(200).json(products); // Respond with the list of products
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving products', error }); // Handle errors
        }
    }

    // Method to update a product by ID
    async updateProduct(req, res) {
        const { id } = req.params; // Get the product ID from the request parameters
        const { name, price, description } = req.body; // Destructure the request body

        try {
            const product = await Product.findByIdAndUpdate(id, { name, price, description }, { new: true }); // Update the product

            if (!product) {
                return res.status(404).json({ message: 'Product not found' }); // Handle case where product is not found
            }

            res.status(200).json({ message: 'Product updated successfully', product }); // Respond with success message and updated product data
        } catch (error) {
            res.status(500).json({ message: 'Error updating product', error }); // Handle errors
        }
    }

    // Method to delete a product by ID
    async deleteProduct(req, res) {
        const { id } = req.params; // Get the product ID from the request parameters

        try {
            const product = await Product.findByIdAndDelete(id); // Delete the product

            if (!product) {
                return res.status(404).json({ message: 'Product not found' }); // Handle case where product is not found
            }

            res.status(200).json({ message: 'Product deleted successfully' }); // Respond with success message
        } catch (error) {
            res.status(500).json({ message: 'Error deleting product', error }); // Handle errors
        }
    }
}

module.exports = ProductController; // Export the ProductController class