# Copyright 2018 sukki-quant. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from suQuant.server.price import price
from suQuant.server.order import Order

import numpy as np

class Server(object):
    """
    基礎的 Server 物件
    """

    def __init__(self):
        pass
        # TODO 放 Price move 後的東西
        # self.ask_buffer = np.zeros(shape=(1,2)) # 放最近的ask
        # self.bid_buffer = np.zeros(shape=(1,2)) # 放最近的bid
