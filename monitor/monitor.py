import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

class Plot:
    def __init__(self, title=None) -> None:
        self.x = []
        self.y = []
        self.title = title
    
    def update_plot(self, x, y):
        # update plot data
        self.x.append(x)
        self.y.append(y)

class LiveMonitor:
    def __init__(self, pause=0.02, sns_active=False) -> None:
        if sns_active:
            sns.set_theme()

        self.plot_list:list[Plot] = []
        self.pause = pause
        
        self.LIVE = False
        self.TERMINATED = False
        
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('close_event', self.__on_close)
        
        

    def __on_close(self, event):
        # user terminate the program
        self.TERMINATED = True
        plt.close()

    def __update_plots(self):
        # clear current figure
        plt.clf()
        # Update the plot.
        for plot in self.plot_list:
            plt.plot(plot.x, plot.y)
        
        plt.legend([p.title for p in self.plot_list])

    def update(self):
        '''Update the monitor'''
        # if terminated keep it terminated
        if self.TERMINATED:
            return
        
        # generate plot
        if not self.LIVE:
            self.LIVE = True
            self.__update_plots()
            plt.ion()
            return
        
        self.__update_plots()
        plt.draw()
        plt.pause(0.02)

    def keep_showing(self):
        '''Keep the window on screen'''
        # reset parameters
        self.LIVE = False
        self.TERMINATED = False
        # show plot
        plt.ioff()
        self.__update_plots()
        plt.show()


if __name__ == "__main__":
    # lv = LivePlot(pause=0)
    live = LiveMonitor(pause=0)

    p1 = Plot(title="A")
    p2 = Plot(title="B")
    live.plot_list = [p1, p2]
    for i in range(100):
        a = i
        b = 2*i**0.5

        # monitor live graph
        p1.update_plot(a,b)
        p2.update_plot(b,a)
        live.update()
    
    live.keep_showing()