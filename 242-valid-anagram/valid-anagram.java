class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length())
            return false;

        HashMap<Character,Integer> mapS = new HashMap<>();
        HashMap<Character,Integer> mapT = new HashMap<>();

        for(int i=0; i<s.length(); i++){
            if(mapS.containsKey(s.charAt(i))){
                int freq = mapS.get(s.charAt(i));
                mapS.put(s.charAt(i), freq+1);
            }
            else{
                mapS.put(s.charAt(i), 1);
            }
        }

        for(int i=0; i<t.length(); i++){
            if(mapT.containsKey(t.charAt(i))){
                int freq = mapT.get(t.charAt(i));
                mapT.put(t.charAt(i), freq+1);
            }
            else{
                mapT.put(t.charAt(i), 1);
            }
        }

         for (char ch : mapS.keySet()) {

            if (!mapT.containsKey(ch)) {
                return false;
            }

            if (!mapS.get(ch).equals(mapT.get(ch))) {
                return false;
            }
        }
        return true;     
    }
}