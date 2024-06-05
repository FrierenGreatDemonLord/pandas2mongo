from datetime import datetime
from typing import Union
import pandas as pd
import numpy as np


def to_base_type(x: Union[None, np.integer, np.floating, pd.Timestamp]) -> Union[None, int, float, datetime]:
    if pd.isna(x):
        return None
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, np.floating):
        return float(x)
    if isinstance(x, pd.Timestamp):
        return x.to_pydatetime()

    return x