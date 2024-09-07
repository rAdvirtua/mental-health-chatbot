const express = require('express');
const axios = require('axios');
const app = express();
app.use(express.json());
app.use(express.static('public')); // Serve HTML file from public folder

// Serve favicon.ico
app.get('/favicon.ico', (req, res) => {
  res.sendFile('public/favicon.ico');
});

// Route to interact with Python chatbot API
app.post('/chat', async (req, res) => {
  try {
    const { question } = req.body;
    console.log('Received request:', { question });
    const flaskResponse = await axios.post('http://localhost:5000/chat', {
      question,
    });
    console.log('Received response from Flask:', flaskResponse.data);
    // Send response back to HTML website in the correct format
    res.json({ botResponse: flaskResponse.data.response });
  } catch (error) {
    console.error('Error communicating with Flask app:', error.message);
    res.status(500).send('Error communicating with Flask app');
  }
});

app.listen(3000, () => {
  console.log('Node.js server is running on http://localhost:3000');
});