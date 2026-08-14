class Solution {
    // Segment Tree Node class to store characteristics of each string segment
    class Node {
        int maxLen;
        int prefLen;
        int suffLen;
        int size;

        Node(int size) {
            this.size = size;
            this.maxLen = 0;
            this.prefLen = 0;
            this.suffLen = 0;
        }
    }

    private Node[] tree;
    private char[] sArr;

    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        int n = s.length();
        this.sArr = s.toCharArray();
        this.tree = new Node[4 * n];
        
        // Build the initial Segment Tree
        build(1, 0, n - 1);
        
        int q = queryIndices.length;
        int[] ans = new int[q];
        
        // Process each update query sequentially
        for (int i = 0; i < q; i++) {
            int idx = queryIndices[i];
            char val = queryCharacters.charAt(i);
            
            update(1, 0, n - 1, idx, val);
            ans[i] = tree[1].maxLen; // The root node always holds the absolute max length
        }
        
        return ans;
    }

    private void merge(Node parent, Node left, Node right, char leftChar, char rightChar) {
        parent.size = left.size + right.size;
        
        // Inherit default segment metrics from children
        parent.prefLen = left.prefLen;
        parent.suffLen = right.suffLen;
        parent.maxLen = Math.max(left.maxLen, right.maxLen);
        
        // If characters at the boundary match, combine across the split line
        if (leftChar == rightChar) {
            parent.maxLen = Math.max(parent.maxLen, left.suffLen + right.prefLen);
            
            // Extend prefix length if the entire left block is uniform
            if (left.prefLen == left.size) {
                parent.prefLen = left.size + right.prefLen;
            }
            // Extend suffix length if the entire right block is uniform
            if (right.suffLen == right.size) {
                parent.suffLen = right.size + left.suffLen;
            }
        }
    }

    private void build(int node, int start, int end) {
        tree[node] = new Node(end - start + 1);
        if (start == end) {
            tree[node].maxLen = 1;
            tree[node].prefLen = 1;
            tree[node].suffLen = 1;
            return;
        }
        
        int mid = start + (end - start) / 2;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        merge(tree[node], tree[2 * node], tree[2 * node + 1], sArr[mid], sArr[mid + 1]);
    }

    private void update(int node, int start, int end, int idx, char val) {
        if (start == end) {
            sArr[idx] = val; // Apply point update
            return;
        }
        
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        
        // Recalculate parent values up the tree after a child state change
        merge(tree[node], tree[2 * node], tree[2 * node + 1], sArr[mid], sArr[mid + 1]);
    }
}
