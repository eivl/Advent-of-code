from dataclasses import dataclass
import numpy as np


@dataclass
class Fabric:
    width: int = 1000
    heigth: int = 1000
    claim: np.int = np.empty((width, heigth), dtype=np.int)

@dataclass
class FabricSlice(Fabric):
    claim_id: str = None
    left_edge: int = 0
    top_edge: int = 0
    slice_width: int = 0
    slice_heiht: int = 0


with open('day3_input.txt') as f:
    content = f.readlines()

fabric = Fabric()

for line in content:

    _, slice_data = line.split('@')
    coords, sizes = slice_data.split(':')
    left, top = map(lambda coord: int(coord.strip()), coords.split(','))
    width, height = map(lambda size: int(size.strip()), sizes.split('x'))
    fabric.claim[left:left + width, top:top + height] += 1


# set all non-overlapping spaces to zero
fabric.claim[fabric.claim <= 1] = 0
# set all overlapping spaces to one
fabric.claim[fabric.claim >= 2] = 1
result = np.sum(fabric.claim)
print(result)
