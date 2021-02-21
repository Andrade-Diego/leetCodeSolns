def preorderTraversal(root):
    vals = []

    if not root: return vals

    vals.append(root.val)

    if root.left:
        vals.extend(preorderTraversal(root.left))
    if root.right:
        vals.extend(preorderTraversal(root.right))
    return vals
