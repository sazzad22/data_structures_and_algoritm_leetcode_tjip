/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

//we define two pointers L at 0 and R at 1.
// L is for finding zero elements and R is for finding non zero elements.
//we start a loop to iterate through.
//inside loop if we find R == 0 we move R forward
// if we find L == 0 we swap it with R that has a non zero value.
// if L is a non zero valu then we move both L and R forward.
//thus zero elements moves toward the end of the array
// TC:O(N)
// SC:O(1)
var moveZeroes = function(nums) {
    //two pointers
    //base case
    const n= nums.length
    if(n < 2){
        return;
    }
    //define pointers
    //here the L is for finding zero elements and R is for finding non zero elements.
    let L= 0,R = 1;
    
    while(R<n){
        if(nums[L] != 0){ //whether nums[R] zero or not we move both forward
            L++;
            R++;
        } else if(nums[R] ==0 ){
            R++;
        } else{
            let temp = nums[R];
            nums[R]= nums[L];
            nums[L]= temp;
        }
    }
    
};