from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *

pixy.init ()
pixy.change_prog ("color_connected_components");

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

def get_block_object():
  blocks = BlockArray(1)
  count = pixy.ccc_get_blocks(1, blocks)
  if count > 0:
    result = ('[BLOCK: SIG=%d X=%2d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[0].m_signature, blocks[0].m_x, blocks[0].m_y, blocks[0].m_width, blocks[0].m_height))
    output = []
    output.append(blocks[0].m_x)
    output.append(blocks[0].m_y)
    print(result)
    print(output)
    return output
  else:
    print("Nothing found")
      
