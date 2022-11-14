import time
import tkinter as tk
import math
#map是个二维数组，用来存储地图信息
#map[j][i]表示地图中第j行第i列的元素
#'#'表示墙壁 'S'表示起点 'E'表示终点 '*'表示通路
def blue(x,y):
    canvas.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill='blue')
    window.update()
    time.sleep(0.05)
def pink(x,y):
    canvas.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill='pink')
    window.update()
    time.sleep(0.05)
def start():
    canvas.create_rectangle(point['start_x']*20, point['start_y']*20, point['start_x']*20+20, point['start_y']*20+20, fill='red')
    window.update()
def end():
    canvas.create_rectangle(point['end_x']*20, point['end_y']*20, point['end_x']*20+20, point['end_y']*20+20, fill='green')
    window.update()
map = [
        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
        ['#','S','*','*','*','*','*','*','*','#','*','*','*','*','*','*','*','*','*','#'],
        ['#','*','#','#','#','#','#','#','*','*','*','#','#','#','#','#','*','#','*','#'],
        ['#','*','#','*','*','*','*','#','#','#','#','#','*','*','*','*','*','#','*','#'],
        ['#','*','#','*','#','#','#','#','*','*','*','#','#','#','#','#','*','#','*','#'],
        ['#','*','*','*','#','*','*','#','#','#','*','*','*','*','*','*','*','#','*','#'],
        ['#','#','#','*','#','*','#','#','*','#','#','#','#','#','#','*','#','#','#','#'],
        ['#','*','*','*','*','*','#','*','*','#','*','*','*','*','*','*','*','*','*','#'],
        ['#','*','#','#','#','*','#','*','*','#','*','#','#','#','#','#','#','#','#','#'],
        ['#','*','*','*','*','*','*','*','*','#','*','*','*','*','*','*','#','*','*','#'],
        ['#','*','*','*','*','*','*','*','*','#','*','*','*','*','*','*','#','*','*','#'],
        ['#','*','#','*','#','#','*','#','#','#','#','*','*','*','#','*','*','E','#','#'],
        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
        ]
#注意，开始和结束坐标需要额外输入一次，所有函数调用都使用point字典中的坐标
point={'start_x':1,'start_y':1,'end_x':17,'end_y':11}
#创建一个窗口
window=tk.Tk()
window.title('A*Maze')
window.geometry("500x450")
#创建一个画布
canvas = tk.Canvas(window, width=500, height=450, bg='grey')
#画出地图
for j in range(len(map)):
    for i in range(len(map[j])):
        if map[j][i] == '#':#墙壁黑色
            canvas.create_rectangle(i*20, j*20, i*20+20, j*20+20, fill='black')
        elif map[j][i] == '*':#通路白色
            canvas.create_rectangle(i*20, j*20, i*20+20, j*20+20, fill='white')
start()
end()
#将画布放置在窗口中
canvas.pack()
window.update()
time.sleep(4)
circle_list=[[0,-1],[0,1],[-1,0],[1,0]]
#open_set是一个优先队列，用来存放待处理的节点,数据为x,y,优先级
#初始化open_set和close_set
open_set = [[point['start_x'],point['start_y'],0]]
close_set = []
parent={str(point['start_x'])+','+str(point['start_y']):[point['start_x'],point['start_y']]}
#如果open_set不为空
while(open_set):
    n=open_set[0]#从open_set中选取优先级最高的节点n
    if(n[0]==point['end_y'] and n[1]==point['end_x']):
        road=[n[0],n[1]]
        while(road[0]!=point['start_y'] or road[1]!=point['start_x']):
            pink(road[1],road[0])
            road=parent[str(road[0])+','+str(road[1])]
        start()
        end()
        break
    else:
        for i,j in circle_list:#遍历节点n所有的邻近节点
            m=[n[0]+i,n[1]+j]#邻近节点
            if map[m[0]][m[1]]=='#':
                continue
                #计算节点m的优先级
            g = abs(m[0]-point['start_y'])+abs(m[1]-point['start_x'])
            h = abs(m[0]-point['end_y'])+abs(m[1]-point['end_x'])
            f = h
            m.append(f)  # type: ignore
            for close in close_set:
                if m==close:
                    break
            else:
                if(m not in open_set):
                    key=str(m[0])+','+str(m[1])
                    parent[key]=n
                    open_set.append(m)#节点m加入open_set中
                    blue(m[1],m[0])
        close_set.append(n)
        del open_set[0]
    open_set.sort(key=lambda x:x[2])#根据优先级排序
else :
    print('no path')
#启动消息循环,避免窗口一闪而过
window.mainloop()