import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import numpy as np

class AsinhStretch:
    def __init__(self, image):
        self.image = image
        self.x = np.linspace(0, 1 ,100)
        
    def asinh(self, black, stretch, plot=False):
        if plot:
            image = self.x
        else:
            image = self.image
        
        if stretch == 0:
            out = image
        else:
            out = ((image - black) * np.arcsinh(image * stretch)) / (image * np.arcsinh(stretch))
        return out
    
   # matplotlib GUI (slow down precedure)- applying stretch wihout matplotlib widgets is much faster
    def plot_asinh(self, s=0, b=0):
        fig = plt.figure(figsize=(12, 6))
        sub = fig.add_gridspec(2,2,width_ratios=[1.8,1])
        ax1 = fig.add_subplot(sub[:,0])
        ax2 = fig.add_subplot(sub[0,1])
        ax3 = fig.add_subplot(sub[1,1])
        ax4 = fig.add_subplot(sub[0,1])
        ax5 = fig.add_subplot(sub[0,1])
        ax3.axis("off")
        ax4.axis("off")
        ax5.axis("off")
        
        ax1.imshow(self.image, vmin=0, vmax=1, cmap='gray')
        ax2.hist(self.image.ravel(), 256, (0, 1))
        ax4 = ax2.twinx()
        ax4.plot(self.x, self.x)
        ax5.plot(self.x, self.x)

        fig.subplots_adjust(bottom=0.1)

        axstretch = fig.add_axes([0.63, 0.4, 0.25, 0.02])
        stretch_slider = Slider(
            ax=axstretch,
            label="stretch ",
            valmin=0,
            valmax=1000,
            valinit=s
        )

        axblack = fig.add_axes([0.63, 0.3, 0.25, 0.02])
        black_slider = Slider(
            ax=axblack,
            label="b ",
            valmin=0,
            valmax=0.2,
            valinit=b
        )
        
        
        def update(val):
            ax2.cla()
            ax1.imshow(self.asinh(black_slider.val, stretch_slider.val), vmin=0, vmax=1, cmap='gray')
            ax2.hist(self.asinh(black_slider.val, stretch_slider.val).ravel(), 256, (0, 1))
            ax4.cla()
            ax4.plot(self.x, self.asinh(black_slider.val, stretch_slider.val, True))
            fig.canvas.draw_idle()
            
        stretch_slider.on_changed(update)
        black_slider.on_changed(update)

        # matplotlib.widgets.Button
        resetax = fig.add_axes([0.5, 0., 0.1, 0.05])
        button_reset = Button(resetax, 'Reset', hovercolor='0.5')

        applyax = fig.add_axes([0.3, 0., 0.1, 0.05])
        button_apply = Button(applyax, 'Apply', hovercolor='0.5')

        def reset(event):
            stretch_slider.reset()
            black_slider.reset()
            
        button_reset.on_clicked(reset)

        def apply(event):
            self.image = self.asinh(black_slider.val, stretch_slider.val)
            stretch_slider.reset()
            black_slider.reset()

        button_apply.on_clicked(apply)

        plt.show()
        return self.image
    

class Mtf():
    def __init__(self, image):
        self.image = image
        self.x = np.linspace(0, 1 ,100)
    
    def mtf(self, midtones, shadows, highlights, plot=False):
        if plot:
            image = self.x
        else:
            image = self.image
            
        xp = (image - shadows) / (highlights - shadows)
        return ((midtones - 1) * xp) / ((2 * midtones - 1) * xp - midtones)
    
    def plot_mtf(self, m=0.5, s=0, h=1):
        fig = plt.figure(figsize=(12, 6))
        sub = fig.add_gridspec(2,2,width_ratios=[1.8,1])
        ax1 = fig.add_subplot(sub[:,0])
        ax2 = fig.add_subplot(sub[0,1])
        ax3 = fig.add_subplot(sub[1,1])
        ax4 = fig.add_subplot(sub[0,1])
        ax5 = fig.add_subplot(sub[0,1])
        ax3.axis("off")
        ax4.axis("off")
        ax5.axis("off")
        
        ax1.imshow(self.image, vmin=0, vmax=1, cmap='gray')
        ax2.hist(self.image.ravel(), 256, (0, 1))
        ax4 = ax2.twinx()
        ax4.plot(self.x, self.x)
        ax5.plot(self.x, self.x)

        fig.subplots_adjust(bottom=0.1)

        axmidtones = fig.add_axes([0.63, 0.4, 0.25, 0.02])
        midtones_slider = Slider(
            ax=axmidtones,
            label="midtones ",
            valmin=0,
            valmax=1,
            valinit=m
        )

        axshadows = fig.add_axes([0.63, 0.3, 0.25, 0.02])
        shadows_slider = Slider(
            ax=axshadows,
            label="shadows",
            valmin=0,
            valmax=1,
            valinit=s
        )
        
        axhighlights = fig.add_axes([0.63, 0.2, 0.25, 0.02])
        highlights_slider = Slider(
            ax=axhighlights,
            label="highlights",
            valmin=0,
            valmax=1,
            valinit=h
        )
        
        def update(val):
            ax2.cla()
            ax1.imshow(self.mtf(midtones_slider.val, shadows_slider.val, highlights_slider.val), vmin=0, vmax=1, cmap='gray')
            ax2.hist(self.mtf(midtones_slider.val, shadows_slider.val, highlights_slider.val).ravel(), 256, (0, 1))
            ax4.cla()
            ax4.plot(self.x, self.mtf(midtones_slider.val, shadows_slider.val, highlights_slider.val, True))
            
            fig.canvas.draw_idle()
            
        midtones_slider.on_changed(update)
        shadows_slider.on_changed(update)
        highlights_slider.on_changed(update)

        # `matplotlib.widgets.Button` 
        resetax = fig.add_axes([0.5, 0., 0.1, 0.05])
        button_reset = Button(resetax, 'Reset', hovercolor='0.5')

        applyax = fig.add_axes([0.3, 0., 0.1, 0.05])
        button_apply = Button(applyax, 'Apply', hovercolor='0.5')

        def reset(event):
            midtones_slider.reset()
            shadows_slider.reset()
            highlights_slider.reset()
            
        button_reset.on_clicked(reset)

        def apply(event):
            self.image = self.mtf(midtones_slider.val, shadows_slider.val, highlights_slider.val)
            midtones_slider.reset()
            shadows_slider.reset()
            highlights_slider.reset()

        button_apply.on_clicked(apply)
        
        plt.show()
        return self.image

