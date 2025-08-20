import time
from contextlib import contextmanager

@contextmanager
def measure_block(name="Block"):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end - start:.4f} seconds")
