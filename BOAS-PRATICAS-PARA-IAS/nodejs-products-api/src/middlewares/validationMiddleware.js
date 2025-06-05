// filepath: d:\BootCampDIO\BOAS-PRATICAS-PARA-IAS\inline-completions\nodejs-products-api\src\middlewares\validationMiddleware.js

const { body, validationResult } = require('express-validator');

// Middleware to validate product creation
const validateProductCreation = [
    body('name')
        .isString()
        .withMessage('Name must be a string')
        .notEmpty()
        .withMessage('Name is required'),
    body('price')
        .isNumeric()
        .withMessage('Price must be a number')
        .notEmpty()
        .withMessage('Price is required'),
    body('description')
        .optional()
        .isString()
        .withMessage('Description must be a string'),
    (req, res, next) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }
        next();
    }
];

// Middleware to validate product updates
const validateProductUpdate = [
    body('name')
        .optional()
        .isString()
        .withMessage('Name must be a string'),
    body('price')
        .optional()
        .isNumeric()
        .withMessage('Price must be a number'),
    body('description')
        .optional()
        .isString()
        .withMessage('Description must be a string'),
    (req, res, next) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }
        next();
    }
];

module.exports = {
    validateProductCreation,
    validateProductUpdate
};