class Solution:
	# @param A : string
	# @return a strings
	def simplifyPath(self, A):
        st = []
        for i in A.split("/"):
            if i == "..":
                if st:
                    st.pop()
            elif i == "." or i == "":
                continue
            else:
                st.append(i)
        return "/" + "/".join(st)