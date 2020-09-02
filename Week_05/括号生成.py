class Solution:
    def generateParenthesis(self, n: int):
        res=[]
        def helper(l,r,s):
            if l==0 and r==0:
                res.append(s)
                return
            if l>0:
                helper(l-1,r,s+'(')
            if r>l:
                helper(l,r-1,s+')')
        helper(n,n,'')
        return res