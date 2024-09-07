const express = require('express');
const axios = require('axios');
const app = express();

app.use(express.json());

// Route to interact with Python chatbot API
app.post('/chat', async (req, res) => {
    try {
        const { context, question } = req.body;
        const response = await axios.post('http://localhost:5000/chat', {
            context: context || '',
            question
        });
        res.json({ botResponse: response.data.response });
    } catch (error) {
        res.status(500).send("Error communicating with chatbot");
    }
});

app.listen(3000, () => {
    console.log('Node.js server is running on http://localhost:3000');
});
    