import multiprocessing

def map_in_parallel(f, values, pool_size):
    pool = multiprocessing.Pool(pool_size)
    results = pool.map_async(f, values)
    pool.close()
    pool.join()

    return results.get()
