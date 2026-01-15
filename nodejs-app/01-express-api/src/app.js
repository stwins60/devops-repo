const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const userRoutes = require('./routes/users');

const app = express();

app.use(cors());
app.use(morgan('dev'));
app.use(express.json());

app.use('/api/users', userRoutes);

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

module.exports = app;
