import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots() # Creating a figure and an axis.
    ax.bar(labels, values) # Creating a bar chart.
    plt.show() # Showing the plot.
    
    
def generate_pie_chart(labels, values):
    # Creating a figure and an axis.
    fig, ax = plt.subplots()
    # Creating a pie chart.
    ax.pie(values, labels=labels)
    # Making the pie chart look like a circle.
    ax.axis('equal')
    # Showing the plot.
    plt.show()
    
def generate_linear_chart(labels, values):
    # Plotting a line graph.
    plt.plot(labels, values)
    # Setting the label of the y-axis.
    plt.ylabel('Letters')
    # Setting the label of the x-axis.
    plt.ylabel('Numbers')
    # Showing the plot.
    plt.show()
    

if __name__ == "__main__":
    
    labels = ['a', 'b', 'c', 'd']
    values = [80, 100, 90, 115]
    
    generate_bar_chart(labels, values)
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)