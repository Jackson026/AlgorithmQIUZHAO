class Solution:
    def findCircleNum(self, M) -> int:
        # M: List[List[int]]
        def union(p,i,j):
            p1=parent(p,i)
            p2=parent(p,j)
            p[p1]=p2
        def parent(p,i):
            root=i
            while root!=p[root]:
                root=p[root]
            while i!=p[i]:
                x=i;i=p[i];p[x]=root
            return root

        p=[i for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]==1:
                    union(p,i,j)
        return len(set([parent(p,i) for i in range(len(M))]))