class Solution:
    # @param A : string
    # @return an integer
    def solve(self, a):
        st = []
        for i in a:
            if i == "(":
                st.append(i)
            elif i == ")":
                if not st:
                    return 0
                else:
                    st.pop()
                    
        if not st:
            return 1
        else:
            return 0
                
