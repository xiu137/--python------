# 迷宫寻路

**注意：**项目中A星算法文件 和 默认算法文件夹 是完全独立的两个不同的内容

我看了网上的一些迷宫相关的算法，虽说相比我写的或许更加清晰，而我个人还是认为对于这种低要求的作业内容没有必要面向对象，而且为了方便其他人阅读代码~~和搬运~~，我也刻意的降低了代码的数量，对于有每一步有寻路优化的A星算法代码压缩到100行以内，而无需优化的简易寻路方式我压缩到50行

对于整体代码逻辑来说，都是

1. 创建页面

2. 构建画布

3. 初始化（根据初始地图来构建画布）

4. 迷宫算法开始寻路（必要时调用画布的函数在对应位置更新画布）

5. 结束

### 普通寻路算法

此函数用于

```python
def fill(x, y, color):
```




### A星算法

A星算法在寻找结果的过程中会自行判断并在下一次更加偏好地寻找更加接近终点的点

代码中有两个列表open_set和close_set

```python
open_set = [[point['start_x'],point['start_y'],0]]
close_set = []
```

优先级计算：

使用曼哈顿距离来计算优先级

```python
g = abs(m[0]-point['start_y'])+abs(m[1]-point['start_x'])
h = abs(m[0]-point['end_y'])+abs(m[1]-point['end_x'])
f = g + h
m.append(f)#将优先级添加至坐标后面
```

当然也可以用直线距离来计算优先级


```python
g = abs(math.pow(m[0]-point['start_y'],2)+math.pow(m[1]-point['start_x'],2))
h = abs(math.pow(m[0]-point['end_y'],2)+math.pow(m[1]-point['end_x'],2))
f = g + h
m.append(f)#将优先级添加至坐标后面
```

[关于A星算法](https://zhuanlan.zhihu.com/p/54510444#:~:text=*%20%E5%88%9D%E5%A7%8B%E5%8C%96open_set%E5%92%8C,m%E5%8A%A0%E5%85%A5open_set%E4%B8%AD)	




* 初始化open_set和close_set；
* 将起点加入open_set中，并设置优先级为0（优先级最高）；
* 如果open_set不为空，则从open_set中选取优先级最高的节点n：
    * 如果节点n为终点，则：
        * 从终点开始逐步追踪parent节点，一直达到起点；
        * 返回找到的结果路径，算法结束；
    * 如果节点n不是终点，则：
        * 将节点n从open_set中删除，并加入close_set中；
        * 遍历节点n所有的邻近节点：
            * 如果邻近节点m在close_set中，则：
                * 跳过，选取下一个邻近节点
            * 如果邻近节点m也不在open_set中，则：
                * 设置节点m的parent为节点n
                * 计算节点m的优先级
                * 将节点m加入open_set中