import math
coords, degrees = tuple(map(int, input().split()))

coordinates = []
for coord in range(coords):
    coordinates.append(list(map(int, input().split())))

radians = degrees * (3.1415/180)
cos = math.cos(radians)
sin = math.sin(radians)

for point in coordinates:
    x = (cos*point[0]) + (-sin*point[1])
    y = (sin*point[0]) + (cos*point[1])
    print(f"{x:.2f} {y:.2f}")