import redis from 'redis';

const client = redis.createClient();

client.on('error', () => {
    console.log('Redis client not connected to the server: ERROR_MESSAGE');
});

client.connect().then(
    () =>
    console.log('Redis client connected to the server')
)