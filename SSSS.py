rom web3 import Web3
import time
import random
from decimal import Decimal
from loguru import logger
from tqdm import tqdm
from sys import stderr

time_delay_min = 120  # Min delay between each account
time_delay_max = 180  # Max delay between each account
repeats = 99 # How much runs this script will do. Must be > 0
amount = {"min": 0.0004, "max": 0.00043} # Amount to bridge min/max. Min value maust be 0.0004 and higher or tx fail!

DADA