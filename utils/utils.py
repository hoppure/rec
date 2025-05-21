import os
import random

import numpy as np


def init_seed():
    np.random.seed(42)
    random.seed(42)


def project_path():
    return os.path.join(
        os.path.dirname(  # /opt/mlops/src/tuils
            os.path.abspath(__file__)  # /opt/mlops/src/utils/utils.py
        ),
        "..",  # /opt/mlops/src
        ".."  # /opt/mlops  --> project_path
    )


# def model_path():
## 작성중