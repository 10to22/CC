// server.js
const express = require('express');
const app = express();
const path = require('path');

app.use(express.json());

// Serve the static frontend files
app.use(express.static(path.join(__dirname, 'frontend/build')));

// API endpoint for sending and receiving messages
let messages = [];

app.get('/api/messages', (req, res) => {
  res.json(messages);
});

app.post('/api/messages', (req, res) => {
  const { message } = req.body;
  messages.push(message);
  res.status(201).json({ message: 'Message sent successfully' });
});

// Serve the frontend app
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend/build', 'index.html'));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
