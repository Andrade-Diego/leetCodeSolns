#include <vector>
#include <iostream>
using namespace std;

int maxArea(vector<int>& height) {
    int largeArea = 0;
    int tempArea = 0;

    // make the two pointers
    int left = 0;
    int right = height.size() - 1;
    while(left < right){
        tempArea = right - left;

        // use the smaller height to calculate area
        if (height[left] < height[right])
            tempArea *= height[left];
        else
            tempArea *= height[right];
        
        if (tempArea > largeArea)
            largeArea = tempArea;
        
        // iterate pointer corresponding to the smaller height
        if(height[left] < height[right])
            left++;
        
        else
            right--;
    }
    return largeArea;
}

int main(){
    vector<int> heights{1,8,6,2,5,4,8,3,7};
    cout <<"(TEST)\n\tlist of Heights = {1, 8, 6, 2, 5, 4, 8, 3, 7}\n\texpected output = 49" << endl;
    int result = maxArea(heights);
    cout << "\tResult = " << result << endl;
}