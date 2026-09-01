class RandomizedSet {

    HashSet<Integer> set;
    ArrayList<Integer> list;

    public RandomizedSet() {
        set = new HashSet<>();
        list = new ArrayList<>();
    }
    
    public boolean insert(int val) {

        if (!set.contains(val)) {
            set.add(val);
            list.add(val);
            return true;
        }
        return false;
    }
    
    public boolean remove(int val) {

        if (set.contains(val)) {
            set.remove(val);
            list.remove(Integer.valueOf(val));
            return true;
        }
        return false;
    }
    
    public int getRandom() {

        int index = (int)(Math.random() * list.size());
        return list.get(index);
    }
}