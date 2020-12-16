def maxArea(height):
    largeArea = 0
    area = 0

    #initializing the two pointers
    left = 0
    right = len(height) - 1

    while (left < right):
        area = right - left
        
        #can only contain water as high as the smaller height
        area *= height[left] if height[left] < height[right] else height[right]
        
        largeArea = area if area > largeArea else largeArea

        #want to iterate the pointer corresponding to the smaller height
        if height[left]<height[right]: left +=1
        else: right -= 1

    return largeArea

if __name__ == "__main__":
    heights = [1,8,6,2,5,4,8,3,7]
    expectedOut = 49

    print(f"(TEST)\n\tlist of heights: {heights}\n\texpected output: {expectedOut}")
    result = maxArea(heights)
    print(f"\tresult of function: {result}")
