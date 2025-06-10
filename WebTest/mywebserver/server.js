const express = require('express');
const path = require('path');
const app = express();
const port = 9500;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/api/data', (req, res) => {
    console.log('Received data:', req.body);
    res.json({ status: 'OK', received: req.body });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
