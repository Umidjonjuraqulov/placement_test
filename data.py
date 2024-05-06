import pandas as pd
from constants import *

def read_test(level: str = "A1"):
    df = pd.read_csv(A1_ENGLISH_TEST_LINK)

    return df