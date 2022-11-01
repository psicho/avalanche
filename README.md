# Avalanche API utils

### Swagger documentation
[127.0.0.0:8000/docs](127.0.0.0:8000/docs)

### Get Balance API
127.0.0.0:8000/api/balance/{blockchain}/{block}/{address}/

**Avalanche balance** 127.0.0.0:8000/api/balance/avalanche/{block}/{address}/

**Ethereum balance** 127.0.0.0:8000/api/balance/ethereum/{block}/{address}/

### Get Avalanche Events API
127.0.0.0:8000/api/events/{from_block}/

### Run tests and coverage report
RUN [test/run_test.sh](test/run_test.sh)

### Local Run
in src directory
run: uvicorn service.server:app --reload

url: [127.0.0.1:8000](http://127.0.0.1:8000 )

### Docker Run
RUN [src/Dockerfile](src/Dockerfile)