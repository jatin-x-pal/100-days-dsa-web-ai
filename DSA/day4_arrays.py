// Day 4 - DSA(Arrays)

// Problem 1 : Find Minimum in Rotated Sorted Array

// Code(Java) :-

class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
             
                left = mid + 1;
            } else {
                
                right = mid;
            }
        }
        return nums[left];
    }
}
 //------------------------------------------------------------

// Problem 2 : Find Minimum in Rotated Sorted Array

// Code(java) :-

class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
             
                left = mid + 1;
            } else {
                
                right = mid;
            }
        }
        return nums[left];
    }
}

