from pgl import GWindow, GRect
#1a
def create_histogram_array(data:list[int])->list[int]:
    histlist = [0] * 10
    for num in data:
        for i in range(10):
            if num == i:
                histlist[i] = histlist[i] + 1
    return histlist
    
#1b
def print_histogram(hist:list[int]) -> None:
    astlist=["*"*h for h in hist]
    for i in range(len(hist)):

        chr=str(i)+": "+str(astlist[i])
        print(chr)
    return astlist

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    gw = GWindow(width,height)
    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    for i in range(len(hist)):
        if hist[i] != 0:
            w = width//10
            h = (height//(max(hist))) * hist[i]
            my_rect(w*i,height - h,w,h,"red")


# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test
