image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return False
        oricolor = image[sr][sc]
        if oricolor == newColor:
            return image
        if len(image) == 0 or len(image[0]) == 0:
            return 0
        self.fill(image, sr, sc, oricolor, newColor)
        return image


    def fill(self, image, sr, sc, oricolor, newcolor):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return
        if image[sr][sc] == oricolor:
            image[sr][sc] = newcolor
            self.fill(image, sr + 1, sc, oricolor, newcolor)
            self.fill(image, sr - 1, sc, oricolor, newcolor)
            self.fill(image, sr, sc + 1, oricolor, newcolor)
            self.fill(image, sr, sc - 1, oricolor, newcolor)

ans = Solution()
print(ans.floodFill(image,sr,sc,newColor))
