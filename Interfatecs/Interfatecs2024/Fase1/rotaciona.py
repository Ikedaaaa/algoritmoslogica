import math
coords, degrees = tuple(map(int, input().split()))

coordinates_list = []
for coord in range(coords):
    coordinates_list.append(list(map(int, input().split())))

cos = math.cos(math.radians(degrees))
sin = math.sin(math.radians(degrees))

for point in coordinates_list:
    x = (cos*point[0]) + (-sin*point[1])
    y = (sin*point[0]) + (cos*point[1])
    print(f"{x:.2f} {y:.2f}")

# math.cos() returns the cosine of a given number in radians.
# the input number is in degrees.
# to calculate it correctly, it's needed to convert from degrees to radians
# if not, math.cos() would return the value of the cosine of 40 radians, not 40 degrees
# for that, math.radians(40) is used to convert 40 degrees to radians