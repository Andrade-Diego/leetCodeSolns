def floodFill(image, sr, sc, newColor):
    old_color = image[sr][sc]
    seen = set()
    def fillSearch(r, c):
        seen.add((r,c))
        if image[r][c] == old_color:
            image[r][c] = newColor
        else:
            return
        if ((r + 1, c) not in seen) and (r + 1 < len(image)):
            fillSearch(r + 1, c)
        if ((r - 1, c) not in seen) and (r - 1 >= 0):
            fillSearch(r - 1, c)
        if ((r, c + 1) not in seen) and (c + 1 < len(image[0])):
            fillSearch(r, c + 1)
        if ((r, c - 1) not in seen) and (c - 1 >= 0):
            fillSearch(r, c - 1)
    fillSearch(sr, sc)
    return image


image = [[1,1,1],[1,1,0],[1,0,1]]
r = 1
c = 1
newColor = 2
print(f"(TEST)\n\tImage: {image}\n\t(r, c): ({r}, {c})\n\tnew color: {newColor}\n\tResult: {floodFill(image, r, c, newColor)}")
