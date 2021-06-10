from cloudburst.client.client import CloudburstConnection
local_cloud = CloudburstConnection('127.0.0.1', 'host.docker.internal', local=True)
cloud_sq = local_cloud.register(lambda _, x: x * x, 'square')
print(cloud_sq(2).get())
print(local_cloud.register_dag('dag', ['square'], []))
print(local_cloud.call_dag('dag', { 'square': [2] }).get())

