// filepath: d:\BootCampDIO\BOAS-PRATICAS-PARA-IAS\inline-completions\nodejs-products-api\src\models\product.js
class Product {
    constructor(name, price, description) {
        this.name = name; // Name of the product
        this.price = price; // Price of the product
        this.description = description; // Description of the product
    }

    // Method to validate product data
    validate() {
        const errors = [];
        if (!this.name || this.name.length < 3) {
            errors.push('Product name must be at least 3 characters long.');
        }
        if (this.price == null || this.price <= 0) {
            errors.push('Product price must be a positive number.');
        }
        if (this.description && this.description.length > 255) {
            errors.push('Product description must not exceed 255 characters.');
        }
        return errors.length > 0 ? errors : null; // Return errors if any
    }
}

module.exports = Product; // Export the Product model for use in other files