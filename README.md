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
- **Run:** cd src/ uvicorn service.server:app --reload

- Local Host address: [127.0.0.1:8000](http://127.0.0.1:8000)

### Docker Run
- **Build:** cd src/ docker-compose build
- **Run:** cd src/ docker-compose up
- **Stop:** cd src/ docker-compose down
- Local Host address: [127.0.0.1:8000](http://127.0.0.1:8000)