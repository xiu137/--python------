from collections import deque
import time
import tkinter
import json

squire=30
def fill(x, y, color):
    canvas.create_rectangle(x*squire,y*squire,x*squire+squire,y*squire+squire,fill=color)
    frame.update()
    time.sleep(0.1)

with open('always_right\\puzzle.json') as f:
    data = json.load(f)
    map = data['map']
    size = data['size']
    start= data['start']
    end = data['end']
    
frame=tkinter.Tk()
frame.title('走迷宫')
frame.geometry(str(size["length"]*squire)+'x'+str(size["width"]*squire))
canvas=tkinter.Canvas(frame,width=size["length"]*squire,height=size["width"]*squire,bg='white')
canvas.pack()
for i in range(len(map)):#画出地图
    for j in range(len(map[i])):
        if map[i][j]==1:
            canvas.create_rectangle(i*squire,j*squire,i*squire+squire,j*squire+squire,fill='black')
fill (start["start_x"],start["start_y"],'red')
fill (end["end_x"],end["end_y"],'green')
time.sleep(1)

list=deque()
list.append((start["start_x"],start["start_x"]))
while list:
    x,y=list.pop()
    list.append((x,y))
    map[x][y]=2
    if([x,y]==[end["end_x"],end["end_y"]]):
        break
    for i in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if map[i[0]][i[1]]==0:
            list.append(i)
            fill(i[0],i[1],'blue')
            break
    else:
        fill(x,y,'yellow')
        list.pop()
print("end")
fill (end["end_x"],end["end_y"],'green')
frame.mainloop()