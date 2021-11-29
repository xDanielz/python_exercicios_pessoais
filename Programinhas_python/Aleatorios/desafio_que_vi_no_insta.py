sharp_dist = [0, 0, 1, 0, 0, 1, 3, 1, 0, 0, 1, 3, 5, 7, 5, 3, 1, 0]
wall_dist = [1, 2, 1, 2, 3, 2, 1, 2, 3, 5, 4, 3, 2, 1, 2, 3, 4, 5]
k = 0

while True:
    print(f"{'#':>{wall_dist[k]}}{' ' * sharp_dist[k]}#" if sharp_dist[k] > 0 else f"{'#':>{wall_dist[k]}}")
    if k == 0 or k == 3:
        print()
    k += 1
    if k == len(sharp_dist):
        break
