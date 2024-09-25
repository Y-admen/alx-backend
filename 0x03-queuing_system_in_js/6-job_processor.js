const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});

queue.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});

queue.on('connect', () => {
    console.log('Redis client connected to the server');
});