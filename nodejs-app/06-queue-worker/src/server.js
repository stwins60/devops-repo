const Queue = require('bull');

const emailQueue = new Queue('email', {
  redis: {
    host: 'localhost',
    port: 6379,
  },
});

emailQueue.process(async (job) => {
  console.log(`Processing email job: ${job.id}`);
  console.log(`Sending email to: ${job.data.to}`);
  
  // Simulate email sending
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  return { sent: true, to: job.data.to };
});

// Add test jobs
emailQueue.add({ to: 'user@example.com', subject: 'Test' });

console.log('Worker started');
