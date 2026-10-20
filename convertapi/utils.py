from concurrent.futures import ThreadPoolExecutor

# Uploads wait on the network, so threads are enough, and unlike processes they share the caller's
# configuration (api_credentials, base_uri, ...) whatever multiprocessing start method Python uses.
def map_in_parallel(f, values, pool_size):
    if pool_size < 2:
        return list(map(f, values))

    with ThreadPoolExecutor(max_workers = pool_size) as pool:
        return list(pool.map(f, values))
