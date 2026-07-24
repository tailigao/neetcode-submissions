class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int number : nums){
            set.add(number);
        }
        if (set.size() < nums.length) {
            return true;
        }
            return false;
        
    }
}