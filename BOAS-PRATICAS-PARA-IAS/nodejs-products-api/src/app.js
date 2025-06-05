const express = require('express'); // Import the Express framework
const bodyParser = require('body-parser'); // Import body-parser to parse incoming request bodies
const productRoutes = require('./routes/productRoutes'); // Import the product routes

const app = express(); // Create an instance of an Express application

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Use the product routes for any requests to /api
app.use('/api', productRoutes);

// Define a port for the server to listen on
const PORT = process.env.PORT || 3000;

// Start the server and listen on the defined port
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log a message when the server starts
});