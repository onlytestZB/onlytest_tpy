import numpy as np
import pandas as pd
test = pd.DataFrame([[1, 3],[2, 3]])
test_t = test.div(test.sum(1).astype(float),axis=0)
print(test_t)