# Cloudburst

[![Build Status](https://travis-ci.com/hydro-project/cloudburst.svg?branch=master)](https://travis-ci.com/hydro-project/cloudburst)
[![codecov](https://codecov.io/gh/hydro-project/cloudburst/branch/master/graph/badge.svg)](https://codecov.io/gh/hydro-project/cloudburst)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Run local in docker
### Setup
Clone this repo then run:

```bash
cd cloudburst/
git checkout setup-local-in-docker
git submodule update --init --recursive
docker build -t cloudburst_local_image .
docker run -it -p 4000:4000 -p 4010:4010 -p 4020:4020 -p 4030:4030 -p 4040:4040 -p 4050:4050 -p 5000-5011:5000-5011 -p 5500:5500 -p 6000:6000 -p 6050:6050 -p 6100:6100 -p 6150:6150 -p 6200:6200 -p 6300:6300 -p 6350:6350 -p 6400:6400 -p 6450-6454:6450-6454 -p 6460:6460 -p 6461:6461 -p 6500:6500 -p 6550:6550 -p 6600:6600 -p 6650:6650 -p 6700:6700 -p 6750:6750 -p 6760-6761:6760-6761 -p 7050:7050 -p 7100:7100 --name cloudburst_local_container cloudburst_local_image /bin/bash
```

You're now connected to the terminal of the docker container. In here we'll start anna and cloudburst.

```bash
./dockerfiles/start-cloudburst.sh
```

The docker image is now locally build and the container is also set-up.
This process can have taken half an hour, but running will be faster from now on.

Test that everything is working by running `ps`.
This should print a couple of processes, probably 7.
Two of these should be python processes and three anna.
If these processes are all running execute `python3 test.py`.
This should print 

```python
4
(True, 0)
4
```

Exit the container with `exit`.


### Running
Now that the container is set up you can simply start it with 

```bash
docker start -ai cloudburst_local_container
```

and start cloudburst again with

```bash
./dockerfiles/start-cloudburst.sh
```


## OG readme
Cloudburst is a low-latency, stateful serverless programming framework built on top of the [Anna KVS](https://github.com/hydro-project/anna). Cloudburst enables users to execute compositions of functions at low latency, and the system builds on top of Anna in order to enable stateful computation. Cloudburst is co-deployed with the [Anna caching system](https://github.com/hydro-project/anna-cache) to achieve low-latency access to shared state, and the system relies on Anna's lattice data structures to resolve conflicting updates to shared state.

## Getting Started

You can install Cloudburst's dependencies with `pip` and use the bash scripts included in this repository to run the system locally. You can find the Cloudburst client in `cloudburst/client/client.py`. Full documentation on starting a cluster in local mode can be found [here](docs/local-mode.md); documentation for the Cloudburst client can be found [here](docs/function-execution.md). An example interaction is modeled below.

```bash
$ pip3 install -r requirements.txt
$ ./scripts/start-cloudburst-local.sh n n
...
$ ./scripts/stop-cloudburst-local.sh n
```

The `CloudburstConnection` is the main client interface; when running in local mode, all interaction between the client and server happens on `localhost`. Users can register functions and execute them. The executions return `CloudburstFuture`s, which can be retrieved asynchronously via the `get` method. Users can also register DAGs (directed, acylic graphs) of functions, where results from one function will be passed to downstream functions. 

```python
>>> from cloudburst.client.client import CloudburstConnection
>>> local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
>>> cloud_sq = local_cloud.register(lambda _, x: x * x, 'square')
>>> cloud_sq(2).get()
4
>>> local_cloud.register_dag('dag', ['square'], [])
>>> local_cloud.call_dag('dag', { 'square': [2] }).get()
4
```

To run Anna and Cloudburst in cluster mode, you will need to use the cluster management setup, which can be found in the [hydro-project/cluster](https://github.com/hydro-project/cluster) repo. Instructions on how to use the cluster management tools can be found in that repo.

## License

The Hydro Project is licensed under the [Apache v2 License](LICENSE).
