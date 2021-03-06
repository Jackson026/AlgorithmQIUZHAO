class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        （1）思路：动态规划
                我们以dp[i][j]表示区间[i, j]之间的子串是否为回文子串，这样可以思考这样三种情况的回文子串：
                    - 子串长度为1，例如 a 一定为回文子串，即 i=j 的情况
                    - 子串长度为2，且字符相同，例如 aa 一定为回文自传，即 s[i] = s[j] and j-i = 1
                    - 子串长度大于2，符合 abcba 形式的为回文子串，根据回文子串的定义，那么 abcba 去掉两边字符，仍为回文
                    子串，即bcb，转换成方程形式即 dp[i][j] = dp[i+1][j-1] and j-i > 1 and s[i] = s[j]
                剩下的均为不符合条件，即非回文子串。

        （2）复杂度：
            - 时间复杂度：O（N^2）
            - 空间复杂度：O（N^2）
        """
        # 处理特殊情况
        str_len = len(s)
        if str_len == 0 or s is None:
            return 0
        # 定义变量储存结果
        res = 0
        # 定义和初始化dp数组
        dp = [[False for _ in range(str_len)] for _ in range(str_len)]
        # 直接先给对角线赋值为True，防止出现 dp[i][j] = dp[i + 1][j - 1] 时，前值没有，例如，i=0，j=2的时候
        for i in range(str_len):
            dp[i][i] = True
        # 遍历字符串，更新dp数组
        # 注意，由于状态转义方程第三种情况是 dp[i][j] = dp[i + 1][j - 1] ，dp取决于 i+1的状态，但是正常遍历
        # 我们肯定是先有了i的状态才能有i+1的 状态，所以，此处我们遍历以 j 为主
        for j in range(str_len):
            # 因为对角线已经赋初始值，所以直接从i+1开始遍历
            for i in range(0, j):
                # 第一种情况，子串长度为1，例如 a 一定为回文子串，因为已经处理了对角线
                # 这里可以注释
                if j - i == 0:
                    dp[i][j] = True
                # 第二种和第三种可以合并，因为对于s[i]=s[j],中间加一个字符是没有影响的，即aba肯定也是回文子串
                # 所以可以合并为 j-i >= 1 and s[i] == s[j]

                # 第二种情况，子串长度为2，且字符相同，例如 aa 一定为回文自传，即 s[i] = s[j] and j-i = 1
                elif j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                # 第三种情况，子串长度大于2，符合 abcba 形式的为回文子串否则不是，即dp[i][j]取决于dp[i + 1][j - 1] 是否
                # 是回文子串
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
        # 遍历dp数组，数True的个数
        for i in range(str_len):
            for j in range(i, str_len):
                if dp[i][j] is True:
                    res += 1
        return res
    

class Solution2:
    def countSubstrings(self, s: str) -> int:
        """
        （1）思路：中心扩展法
                这是一个比较巧妙的方法，实质的思路和动态规划的思路类似。比如对一个字符串ababa，选择最中间的a作为中心点，
            往两边扩散，第一次扩散发现left指向的是b，right指向的也是b，所以是回文串，继续扩散，同理ababa也是回文串。这个
            是确定了一个中心点后的寻找的路径，然后我们只要寻找到所有的中心点，问题就解决了。中心点一共有多少个呢？看起来
            像是和字符串长度相等，但你会发现，如果是这样，上面的例子永远也搜不到abab，想象一下单个字符的哪个中心点扩
            展可以得到这个子串？似乎不可能。所以中心点不能只有单个字符构成，还要包括两个字符，比如上面这个子串abab，
            就可以有中心点ba扩展一次得到
        （2）复杂度：
            - 时间复杂度：O（N^2）
            - 空间复杂度：O（1）
        """
        # 处理特殊情况
        str_len = len(s)
        if str_len == 0 or s is None:
            return 0
        # 定义变量储存结果，初始化时直接考虑单字符回文的情况，所以直接赋值为字符串长度
        res = str_len
        # 遍历所有的中心点，第一类，遍历所有的单中心点
        for center in range(1, str_len-1):
            # 初始定义left和right和中心点不同，因为单字符已经在res初始化时考虑了
            left, right = center-1, center+1
            while left >= 0 and right < str_len and s[left] == s[right]:
                res += 1
                left, right = left-1, right+1
        # 遍历所有的中心点，第二类，遍历所有的双中心点
        # 注意考虑两个问题，一个是双中心点本身需要考虑是否是回文，另一个是边界条件，需要考虑
        for center in range(0, str_len - 1):
            # 考虑双中心点本身是否是回文子串
            if s[center] == s[center+1]:
                res += 1
            # 初始定义left和right和中心点不同
            left, right = center-1, center+2
            while left >= 0 and right < str_len and s[left] == s[right] and s[center] == s[center+1]:
                res += 1
                left, right = left-1, right+1

        return res