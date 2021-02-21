def postorderTraversal(root):
    vals = []
    if root:
        if root.left:
            vals.extend(postorderTraversal(root.left))
        if root.right:
            vals.extend(postorderTraversal(root.right))
        vals.append(root.val)
    return vals
