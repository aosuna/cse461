#Adrian Osuna
#CSE 461 - Dr. Gomez
#Lab 2

import random
import numpy

cylinders = 4096
block_size = 512 #also the bytes per block
number_heads = 8
blocks_per_track = 64
blocks_per_cylinder = blocks_per_track * number_heads #size equal to 4096
bytes_per_cylinder = blocks_per_track * block_size
tracks_per_cylinder = block_size * number_heads #reads are 4k or 4096 bytes
addresses = tracks_per_cylinder * blocks_per_track 
avg_seek_time = 0.01
rotation_speed = 7200 #rotations per minute
average_rotational_latency = 0.0042 # 1/2 rotational latency
maximum_bandwidth = bytes_per_cylinder / average_rotational_latency
page_size = 4096 #set page size to 4K
MAX = (blocks_per_cylinder / block_size) - 1

