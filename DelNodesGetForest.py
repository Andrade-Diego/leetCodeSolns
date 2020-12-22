class Solution:
    def makeForest(self, root, newTree):
        if root == None:
            return False
        deleteCurr = root.val in self.toDel
        if newTree and not deleteCurr:
            self.forestList.append(root)
            
        if self.makeForest(root.left, deleteCurr): root.left = None
        if self.makeForest(root.right, deleteCurr): root.right = None

        return deleteCurr
            
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.forestList = []
        self.toDel = to_delete
        self.makeForest(root, True)
        return self.forestList