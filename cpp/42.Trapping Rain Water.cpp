//..............................LEETCODE HARD PROBLEM.........................//
//...Two Pointer Approach Solution

class Solution {
public:
    int trap(vector<int>&height) {
        //Space COmplexity O(n)
        //Time Complexity O(n)
        int n = height.size();

        vector<int>left(n);
        left[0] = height[0];

        for(int i=1;i<n;i++){
            left[i] = max(left[i-1],height[i]);
        }

        vector<int>right(n);
        right[n-1] = height[n-1];

        for(int i=n-2;i>=0;i--){
            right[i] = max(right[i+1],height[i]);
        }
        
        int ans =0;
        for(int i=0;i<n;i++){
            ans += (min(right[i],left[i])-height[i]);
        }
        return ans;
    
    }
};