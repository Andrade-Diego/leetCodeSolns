var searchMatrix = function(matrix, target) {
    let i = 0;
    let found = false;

    while(i < matrix.length){
        var left = 0;
        var right = matrix[0].length - 1 ;
        while (left <= right && !found){
            middle = Math.floor((right + left) / 2);
            if (target == matrix[i][middle]){
                found = true;
            }
            else if (target > matrix[i][middle]){
                left = middle + 1;
            }
            else if (target < matrix[i][middle]){
                right = middle - 1;
            }
        }
        if (found){
            return found;
        }
        else {
            i++;
        }
    }
    return found;
};
let testMatrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]];
let testTarget = 14;
console.log("Target is found in matrix: %s",searchMatrix(testMatrix, testTarget));