import pandas as pd
import numpy as np
import os
import platform
import pyarrow.parquet as pq
def load_csv2arr(path):
    return np.array(np.read_csv('../'+path))
def load_par2arr():
    return np.array(pq.read_pandas('../'+path).to_pandas())
