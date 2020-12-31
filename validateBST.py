def isValidBST(root, lowerLimit = -math.inf, upperLimit = math.inf):
    valid = True
    if root.left:
        if root.left.val < root.val and root.left.val > lowerLimit:
            valid =  self.isValidBST(root.left, lowerLimit, root.val)
        else:
            valid = False

    if root.right and valid:
        if root.right.val > root.val and root.right.val < upperLimit:
            valid = self.isValidBST(root.right, root.val, upperLimit)
        else:
            valid =  False
    
    return valid