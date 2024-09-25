import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

client.connect().then(() => {
    () =>
    console.log('Redis client connected to the server')
})

function setNewSchool(schoolName, value) {
    client.set()
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error('Error:', err);
        } else {
            console.log(reply);
        }
    });
}