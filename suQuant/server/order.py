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

UNINIT = -1
ORDER_STATUS_DEAL = 2

ORDER_TYPE_BUY       = 0
ORDER_TYPE_SELL      = 1
ORDER_TYPE_BUYLIMIT  = 2
ORDER_TYPE_SELLLIMIT = 3
ORDER_TYPE_BUYSTOP   = 4
ORDER_TYPE_SELLSTOP  = 5

class Order(object):
    """
    基本的掛單物件
    """
    def __init__(self):
        self.status      = UNINIT
        self.order_type  = UNINIT
        self.open_time   = UNINIT
        self.close_time  = UNINIT
        self.order_size  = UNINIT
        self.magic       = UNINIT
        self.open_price  = UNINIT
        self.close_price = UNINIT
        self.take_profit = UNINIT
        self.stop_loss   = UNINIT

    def buy(self,open_price,order_size,magic,open_time,stop_loss=0,take_profit=0):
        self.status      = ORDER_STATUS_DEAL
        self.order_type  = ORDER_TYPE_BUY
        self.open_time   = open_time
        self.order_size  = order_size
        self.magic       = magic
        self.open_price  = open_price
        self.take_profit = take_profit
        self.stop_loss   = stop_loss

    def sell(self,open_price,order_size,magic,open_time,stop_loss=0,take_profit=0):
        self.status      = ORDER_STATUS_DEAL
        self.order_type  = ORDER_TYPE_SELL
        self.open_time   = open_time
        self.order_size  = order_size
        self.magic       = magic
        self.open_price  = open_price
        self.take_profit = take_profit
        self.stop_loss   = stop_loss
