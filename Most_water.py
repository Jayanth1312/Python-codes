from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0
    max_height = len(height)
    while left < right:
        min_height = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, min_height)

        if height[left] <= height[right]:
            left += 1

        else:
            right -= 1

        if max_water > max_height * (right - left):
            break

    return max_water


if __name__ == "__main__":
    height = list(map(int, input().split()))
    print(maxArea(height))
