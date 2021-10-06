import matplotlib.pyplot as plt
import json
f = open('time_test.json')
data = json.load(f)


def draw_plot(experiment: str):
    x = [i for i in range(7, 16)]
    y = []
    y1 = []
    y2 = []
    y3 = []
    for elem in x:
        y.append(data[str(elem)][experiment]["insertion sort"])
        y1.append(data[str(elem)][experiment]["selection sort"])
        y2.append(data[str(elem)][experiment]["merge sort"])
        y3.append(data[str(elem)][experiment]["shell sort"])
    plt.plot(x, y)
    plt.title(f"{experiment} experiment (time comparison)")
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.yscale('log')
    plt.xlabel('довжина списку (2^x)')
    plt.ylabel("час (сек)")
    plt.legend(['insertion sort', 'selection sort',
                'merge sort', 'shell sort'])
    plt.show()


if __name__ == '__main__':
    plot_to_draw = input("type first/second/third/fourth: ")
    draw_plot(plot_to_draw)
