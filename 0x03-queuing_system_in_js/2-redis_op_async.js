import { createClient } from 'redis';
const { promisify } = require('util');

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

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.error('Error:', err);
    }
}