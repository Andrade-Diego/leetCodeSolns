def inorderTraversal(root):
    vals = []
    if root:
        if root.left:
            vals.extend(inorderTraversal(root.left))
        vals.append(root.val)
        if root.right:
            vals.extend(inorderTraversal(root.right))
    return vals
