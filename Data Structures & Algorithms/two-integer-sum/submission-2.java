class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> ma = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int diff = target - num;
            if(ma.containsKey(diff)){
                return new int[] {ma.get(diff), i};
            }
            ma.put(num, i);
        }
        return new int[0];
    }
}
