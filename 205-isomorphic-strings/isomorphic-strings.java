class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> mapST = new HashMap<>();
        HashMap<Character, Character> mapTS = new HashMap<>();

        for(int i=0; i<s.length(); i++){

            char eleS = s.charAt(i);
            char eleT = t.charAt(i);

            if(mapST.containsKey(eleS)){
                if(mapST.get(eleS) != eleT)
                    return false;
            }
            else
                mapST.put(eleS, eleT);

            if(mapTS.containsKey(eleT)){
                if(mapTS.get(eleT) != eleS)
                    return false;
            }
            else
                mapTS.put(eleT, eleS);
        }
        return true;
    }
}