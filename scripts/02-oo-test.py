from pyvicon.tracker import Tracker
import numpy as np

t = Tracker("192.168.10.102:801", ["cube1", "ergo1"])

# print("=== cube ===")
# for _ in range(5):
#     print (t.get_pos("cube1"))
#
# print("=== only 1 ===")
# for _ in range(5):
#     print (t.get_pos("cube1", 0))
#
# print("=== ergo ===")
# for _ in range(5):
#     print (t.get_pos("ergo1"))
#
# print("=== only 1 ===")
# for _ in range(5):
#     print (t.get_pos("ergo1", 0))


print("=== BOTH ===")
for _ in range(10000):
    print (t.get_dist(["cube1","ergo1"]))


