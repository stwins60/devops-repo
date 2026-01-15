const cron = require('node-cron');
const express = require('express');

const app = express();

// Schedule tasks
cron.schedule('*/1 * * * *', () => {
  console.log('Running cleanup job every minute');
});

cron.schedule('0 * * * *', () => {
  console.log('Running hourly report generation');
});

cron.schedule('0 0 * * *', () => {
  console.log('Running daily backup at midnight');
});

cron.schedule('0 0 * * 0', () => {
  console.log('Running weekly summary on Sunday');
});

app.get('/health', (req, res) => {
  res.json({ status: 'Scheduler running', jobs: 4 });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Cron scheduler running on port ${PORT}`);
  console.log('Scheduled jobs are active');
});
