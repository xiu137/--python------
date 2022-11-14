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

此函数用于更新画布，会在对应位置调用

```python
def fill(x, y, color):
```

然后是从puzzle.json读取地图和地图信息

```python
with open('always_right\\puzzle.json') as f:
    data = json.load(f)
    map = data['map']
    size = data['size']
    start= data['start']
    end = data['end']
```

相比于A星算法的代码中，我使用栈结构来优化代码逻辑。开始时把起点压栈每次计算下一步就是把下一步的坐标压栈，**并且把这个节点的位置改为墙以避免重复调用。**

如果此坐标为死路，则把这个坐标弹栈，回到上一个栈内的坐标。直到走到终点或者回到起点（无解）。


### A星算法

A星算法在寻找结果的过程中会自行判断并在下一次更加偏好地寻找更加接近终点的点

代码中有两个列表open_set和close_set，open_set里的是还需要遍历的坐标，而close_set是已经完成遍历的坐标。**如果需要遍历的坐标为空，则证明迷宫无解**

```python
open_set = [[point['start_x'],point['start_y'],0]]
close_set = []
```

每次遍历从open_set中调取优先级数值最低的坐标进行尝试，由于每轮循环后都会根据优先级排序，所以每次都调用open_set[0]即第一个值

```python
open_set.sort(key=lambda x:x[2])
```

完成遍历的值会添加到close_set，并且parent字典也会记录**坐标值**和其**上一步的值**

```python
parent={str(point['start_x'])+','+str(point['start_y']):[point['start_x'],point['start_y']]}
```

在遍历的坐标为终点时，函数便会调用下面的函数进行反向求解到达终点的路径，直到回到起点

```python
while(road[0]!=point['start_y'] or road[1]!=point['start_x']):
            pink(road[1],road[0])
            road=parent[str(road[0])+','+str(road[1])]
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
#### 其他链接：

[关于A星算法](https://zhuanlan.zhihu.com/p/54510444#:~:text=*%20%E5%88%9D%E5%A7%8B%E5%8C%96open_set%E5%92%8C,m%E5%8A%A0%E5%85%A5open_set%E4%B8%AD)	

#### 特殊说明：

如果此项目对你有帮助，记得点个star，感谢