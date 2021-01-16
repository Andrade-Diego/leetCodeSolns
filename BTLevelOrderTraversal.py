def levelOrder(TreeNode):
    arr = []
    if root == None:
        return []
    def traverse(root, level):
        if  len(arr) <= level:
            arr.append([root.val])
        else:
            arr[level].append(root.val)
        if root.left:
            traverse(root.left, level + 1)
        if root.right:
            traverse(root.right, level + 1)
        if not root.right and not root.left:
            return
    traverse(root, 0)
    return arr
