import { createClient } from 'redis';

const client = createClient();

client.connect().then(() => {
    console.log('Connected to Redis');
}).catch(console.error);