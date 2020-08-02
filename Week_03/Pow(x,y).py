
# 递归
# 计算 x 的 n 次幂函数

def myPow(self, x: float, n: int) -> float:
    def quick(N):
        if N == 0:
            return 1.0
        y = quick(N // 2)
        return y * y if N % 2 == 0 else y * y * x

    return quick(n) if n >= 0 else 1.0 / quick(-n)




def myPow(self, x: float, n: int) -> float:
    if n==0:
        return 1
    if n==1:
        return x
    if n<0:
        n=-n
        half = self.myPow(x,n//2)
        if n%2 == 0:
            return 1/(half*half)
        else:
            return 1/(half*half*x)
    else:
        half = self.myPow(x,n//2)
        if n%2 == 0:
            return half*half
        else:
            return half*half*x