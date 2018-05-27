import csv
import matplotlib.pyplot as plt


#color list with size 14
# color list to plot the graph
colors = ['NAVY', 'BLUE', 'AQUA', 'TEAL', 'OLIVE', 'GREEN', 'LIME',
          'YELLOW', 'ORANGE', 'RED', 'MAROON', 'FUCHSIA', 'PURPLE', 'GRAY']

# this function is the replacement of the "in" operator, because list is sorted
def binarySearch(element, dataSet):
    first = 0
    last = len(dataSet)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if dataSet[midpoint] == element:
            found = True
        else:
            if element < dataSet[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


# function to initialized margin dictionary

# margins variable which is initialized by margin function
margins = {  # vvv margin in inches
    "left":     .1,
    "bottom":     .1,
    "right":    .99,
    "top":   .99
}
def margin(l=.1, b=.1, r=.99, t=.99):
    margins['left'] = l
    margins['bottom'] = b
    margins['right'] = r
    margins['top'] = t

# function to plot the graph


def barGraphPlot(title='Graph', yLable='yLable', xLable='xlable', yRotation=None, xRotation=None, yTicksFontSize=7,
                 xTicksFontSize=7, yAxisElements=[], xAxisElements=[], ySpace=2, yTopSpace=3,textDecimal=False):
    
    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        if(textDecimal==True):
            for rect in rects:
                height = rect.get_height()
                print(height,"        in height"  )
                plt.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                        '%.3f' % height,
                        ha='center', va='bottom',rotation=90,fontsize=7)
        else:
            for rect in rects:
                height = rect.get_height()
                print(height,"        in height"  )
                plt.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                        '%d' % height,
                        ha='center', va='bottom',rotation=0,fontsize=10)




    # seting size of the frame where graph have to be ploted
    plt.rcParams['figure.figsize'] = (20, 8)

    # marging for bars in graph
    plt.margins(0.005)
    plt.subplots_adjust(**margins)
    autolabel(plt.bar(xAxisElements, yAxisElements))
    plt.xlabel(xLable,fontsize=12)
    plt.ylabel(yLable,fontsize=12)
    plt.yticks(range(0, int(max(yAxisElements))+yTopSpace,ySpace),
               rotation=yRotation, fontsize=yTicksFontSize)
    plt.xticks(range(0,len(xAxisElements)),xAxisElements,
               rotation=xRotation, fontsize=xTicksFontSize)
    plt.title(title)
    plt.grid(True,color='#4b738e', linestyle='-', linewidth=.1)
    plt.show()
