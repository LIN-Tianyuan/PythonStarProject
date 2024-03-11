from collections import deque
from math import comb


def parse_land_plan(land_plan_str):
    return [list(row) for row in land_plan_str.strip().split('\n')]


def find_fields(land_plan):
    # Find the number of fields in the land plan.
    rows, cols = len(land_plan), len(land_plan[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Four directions: down, up, right, left
    fields_count = 0

    for row in range(rows):
        for col in range(cols):
            if land_plan[row][col] == 'H' and not visited[row][col]:
                fields_count += 1
                # Mark all connected cells in the same field as visited
                queue = deque([(row, col)])
                while queue:
                    r, c = queue.pop()
                    for dr, dc in directions:
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < rows and 0 <= cc < cols and land_plan[rr][cc] == 'H' and not visited[rr][cc]:
                            visited[rr][cc] = True
                            queue.appendleft((rr, cc))
    return fields_count


def calculate_arrangements(fileds_count):
    # Number of possible arrangements
    mod = 1234567
    arrangements = sum(comb(fileds_count, k) for k in range(0, fileds_count + 1, 2)) % mod
    return arrangements

def get_fields_count_and_arrangements(land_plan_str):
    land_plan = parse_land_plan(land_plan_str)
    fields_count = find_fields(land_plan)
    arrangements = calculate_arrangements(fields_count)
    return fields_count, arrangements

example_land_plan_str = """
H N N H
N H N H
N H N N
"""
fields_count, arrangements = get_fields_count_and_arrangements(example_land_plan_str)
print(f"Example: Le nombre de champs est: {fields_count}, Le nombre de l'organisation possible est: {arrangements}")

file_path1 = 'exo2_A.txt'
file_path2 = 'exo2_B.txt'
file_path3 = 'exo2_C.txt'
with open(file_path1, 'r') as file:
    land_plan_str_a = file.read()

with open(file_path2, 'r') as file:
    land_plan_str_b = file.read()

with open(file_path3, 'r') as file:
    land_plan_str_c = file.read()

fields_count_a, arrangements_a = get_fields_count_and_arrangements(land_plan_str_a)
print(f"Exo2_A : Le nombre de champs est: {fields_count_a}, Le nombre de l'organisation possible est: {arrangements_a}")

fields_count_b, arrangements_b = get_fields_count_and_arrangements(land_plan_str_b)
print(f"Exo2_B : Le nombre de champs est: {fields_count_b}, Le nombre de l'organisation possible est: {arrangements_b}")

fields_count_c, arrangements_c = get_fields_count_and_arrangements(land_plan_str_c)
print(f"Exo2_C : Le nombre de champs est: {fields_count_c}, Le nombre de l'organisation possible est: {arrangements_c}")