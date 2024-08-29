import graphics as gr
import tkinter as tr
window = gr.GraphWin('HanoyTowers', 600, 600)


osnovanie = gr.Rectangle(gr.Point(100, 500), gr.Point(500, 600)).draw(window)
osnovanie.setFill('black')
stolb1 = gr.Line(gr.Point(150, 500), gr.Point(150, 200)).draw(window)
stolb2 = gr.Line(gr.Point(300, 500), gr.Point(300, 200)).draw(window)
stolb3 = gr.Line(gr.Point(450, 500), gr.Point(450, 200)).draw(window)

block1 = gr.Rectangle(gr.Point(100, 500), gr.Point(200, 480)).draw(window)
block1.setFill('red')

block2 = gr.Rectangle(gr.Point(125, 480), gr.Point(175, 460)).draw(window)
block2.setFill('green')
block3 = gr.Rectangle(gr.Point(140, 460), gr.Point(160, 440)).draw(window)
block3.setFill('yellow')


array_of_columns = [[block1,block2,block3], [], []]


def block_color(block):
    if sqware(block) == 2000.0:
        return 'red'
    elif sqware(block) == 1000.0:
        return 'green'
    elif sqware(block) == 400.0:
        return 'yellow'


def redraw_blocks(block, arr_out, arr_in):
    if array_of_columns.index(arr_out) == 2 and array_of_columns.index(arr_in) == 0:
        block.move(-300, 0)
    elif array_of_columns.index(arr_out) > array_of_columns.index(arr_in):
        block.move(-150, 0)    
    elif array_of_columns.index(arr_out) == 0 and array_of_columns.index(arr_in) == 2:
        block.move(300, 0)
    elif array_of_columns.index(arr_out) < array_of_columns.index(arr_in):
        block.move(150, 0)

    

arr1 = tr.PhotoImage(file = r"strelka_vlevo.jpg")
arr2 =tr.PhotoImage(file = r"strelka_vpravo.jpg")

button1 = tr.Button(window, image=arr1, command = lambda: Block_move(array_of_columns[0][-1], array_of_columns[0], array_of_columns[2])).place(x=100, y=200)
button2 = tr.Button(window, image=arr2, command = lambda: Block_move(array_of_columns[0][-1], array_of_columns[0], array_of_columns[1])).place(x=160, y=200)
button3 = tr.Button(window, image=arr1, command = lambda: Block_move(array_of_columns[1][-1], array_of_columns[1], array_of_columns[0])).place(x=250, y=200)
button4 = tr.Button(window, image=arr2, command = lambda: Block_move(array_of_columns[1][-1], array_of_columns[1], array_of_columns[2])).place(x=310, y=200)
button5 = tr.Button(window, image=arr1, command = lambda: Block_move(array_of_columns[2][-1], array_of_columns[2], array_of_columns[1])).place(x=400, y=200)
button6 = tr.Button(window, image=arr2, command = lambda: Block_move(array_of_columns[2][-1], array_of_columns[2], array_of_columns[0])).place(x=460, y=200)


def sqware(block):
    return abs(block.p2.x-block.p1.x)*abs(block.p2.y-block.p1.y)


def Block_move(block, s_out, s_in):
    block_index_out = s_out.index(block)
    if not s_out:
        print('Нечего перекладывать!')
    elif not s_in:
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
        print(f'Переложили {b} иЗ {s_out} в {s_in}')
        block_index_in = s_in.index(block)
        redraw_blocks(block, s_out, s_in)
    elif sqware(s_in[-1]) > sqware(s_out[-1]):
        print('Переложили')
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
        print(f'Переложили {b} из {s_out} в {s_in}')
        block_index_in = s_in.index(block)
        redraw_blocks(block, s_out, s_in)
    else:
        print('Так не пойдет!')
    if len(s_in) == 3:
        print('Победа!') 



window.getMouse()
window.close()