# Queuing System in JS

## What is Redis?
Redis (REmote DIctionary Server) is an open-source, in-memory data structure store used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, and sorted sets. Redis is known for its high performance, flexibility, and ease of use.

### what is in-memory data?
In-memory data refers to data that is stored directly in the main memory (RAM) of a computer, rather than on traditional disk storage. This approach allows for much faster data access and manipulation because accessing data in RAM is significantly quicker than reading from or writing to a disk.


#### Key Concepts and Installation

``` shell
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```
1. Extract the Tarball
Command:

``` shell
tar xzf redis-6.0.10.tar.gz

Explanation:
```
Tarball: A tarball is a compressed archive file (similar to a ZIP file) that contains multiple files bundled together.
Extracting: The tar xzf command extracts the contents of the tarball (redis-6.0.10.tar.gz) into the current directory.
2. Navigate to the Redis Directory
Command:

``` shell
cd redis-6.0.10
```

Explanation:

Change Directory: The cd command changes the current working directory to redis-6.0.10, where the extracted files are located.
3. Compile Redis
Command:

``` shell
make
```

Explanation:

Compilation: The make command reads the Makefile and compiles the Redis source code into executable binaries. This process involves translating the source code into machine code that can be executed by the computer.
4. Start Redis Server
Command:

``` shell
src/redis-server &
```

Explanation:

Starting the Server: This command starts the Redis server in the background. The & symbol allows the server to run as a background process, freeing up the terminal for other commands.
5. Verify Redis Server
Command:
``` shell
src/redis-cli ping
```
Expected Output:

PONG

Explanation:

Ping Command: The ping command checks if the Redis server is running and responsive. A successful response returns PONG.

**Hashes** are a data structure that stores a mapping of fields to values, similar to a dictionary or a JSON object.
