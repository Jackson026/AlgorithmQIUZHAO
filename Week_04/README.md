学习笔记
<br/>
## 递归代码模版
class Recrusion(object):

    public void recur(int level, int param) {
        // terminator 
        if (level > MAX_LEVEL) {
        // process result 
            return; }
        // process current logic 
        process(level, param);
        // drill down 
        recur( level: level + 1, newParam);
        // restore current status 
    }
## 分治代码模版<br/>
class Divid_conquer(object):

    def divide_conquer(problem, param1, param2, ...): 
        # recursion terminator 
        if problem is None: 
            print_result 
        return
        # prepare data 
        data = prepare_data(problem) 
            subproblems = split_problem(problem, data) 
        # conquer subproblems 
        subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
        subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
        subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
        … 
        # process and generate the final result 
        result = process_result(subresult1, subresult2, subresult3, …) 
        # revert the current level states
### 感触
1. 人肉递归低效、很累<br/>
2. 找到最近最简方法，将其拆解成可重复解决的问题<br/>
3. 数学归纳法思维（抵制人肉递归的诱惑）<br/>

## 动态规划关键点
动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构） <br/>
共性：找到重复子问题<br/>
差异性：最优子结构、中途可以淘汰次优解<br/>

1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], …)<br/>
2. 储存中间状态：opt[i]<br/>
3. 递推公式（美其名曰：状态转移方程或者 DP 方程） <br/>
Fib: opt[i] = opt[n-1] + opt[n-2] <br/>
二维路径：opt[i,j] = opt[i+1][j] + opt[i][j+1] (且判断a[i,j]是否空地<br/>
## 字符串问题<br/>
转换为二维数组的形式思考问题<br/>