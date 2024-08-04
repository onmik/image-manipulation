import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import numpy as np
import arithm

#---------------- Generalised hyperbolic stretch -------------------------------
class Ghs:
    def __init__(self, image):
        self.image = image
        self.x = np.linspace(0, 1 ,100)
        
    def ghs(self, D, b, SP, LP, HP, plot=False):
        if plot:
            image = self.x
        else: 
            image = self.image
        
        if D == 0:
            return image
        elif b == -1:                       
            qlp = -1 * np.log1p(D * (SP - LP))
            q0 = qlp - D * LP / (1 + D * (SP - LP))
            qwp = np.log1p(D * (HP - SP))
            q1 = qwp + D * (1 - HP) / (1 + D * (HP - SP))
            q = 1 / (q1 - q0)
            
            b1 = (1 + D * (SP - LP)) / (D * q)

            a2 = (-q0) * q
            b2 = -q
            c2 = 1 + D * SP
            d2 = -D

            a3 = (-q) * q
            b3 = q
            c3 = 1 - D * SP
            d3 = D

            a4 = (qwp - q0 - D * HP / (1 + D * (HP - SP))) * q
            b4 = q * D / (1 + D * (HP - SP))

        elif (b < 0):
            qlp = -(1 - np.sign(1 - D * b * (SP - LP)) * np.power(np.abs(1 - D * b * (SP - LP)), 
                                 (b + 1) / b)) / (b + 1)
            q0 = qlp - D * LP * (np.sign(1 - D * b * (SP - LP)) * np.power(np.abs(1 - D * b * (SP - LP)), 1 / b))
            qwp = -(np.sign(1 - D * b * (HP - SP)) * np.power(np.abs(1 - D * b * (HP - SP)), 
                             (b + 1) / b) - 1) / (b + 1)
            q1 = qwp + D * (1 - HP) * (np.sign(1 - D * b * (HP - SP)) * np.power(np.abs(1 - D * b * (HP - SP)),
                                               1 / b))
            q = 1 / (q1 - q0)

            b1 = D * (np.sign(1 - D * b * (SP - LP)) * np.power(np.abs(1 - D * b * (SP - LP)),
                                   1 / b)) * q

            a2 = -(1 / (b + 1) + q0) * q
            b2 = q / (b + 1)
            c2 = 1 - D * b * SP
            d2 = D * b
            e2 = (b + 1) / b

            a3 = (1 / (b + 1) - q0) * q
            b3 = -q / (b + 1)
            c3 = 1 + D * b * SP
            d3 = -D * b
            e3 = (b + 1.0) / b

            a4 = (qwp - q0 - D * HP * (np.sign(1 - D*b*(HP - SP)) * np.power(np.abs(1 - D*b*(HP - SP)), 
                                                    1 / b))) * q
            b4 = D * (np.sign(1 - D * b * (HP - SP)) * np.power(np.abs(1 - D * b * (HP - SP)),1 / b)) * q

        elif(b ==0):
            qlp = np.exp(-D * (SP - LP))
            q0 = qlp - D * LP * qlp
            qwp = 2 - np.exp(-D * (HP - SP))
            q1 = qwp + D * (1 - HP) * (2 - qwp)
            q = 1 / (q1 - q0)

            b1 = D * qlp * q

            a2 = -q0 * q
            b2 = q
            c2 = -D * SP
            d2 = D
            e2 = 0

            a3 = (2 - q0) * q
            b3 = -q
            c3 = D * SP
            d3 = -D
            e3 = 0

            a4 = (qwp - q0 - D * HP * (2 - qwp)) * q
            b4 = D * (2 - qwp) * q

        else: # (b > 0)
            qlp = np.sign(1 + D * b * (SP - LP)) * np.power(np.abs(1 + D * b * (SP - LP)), -1 / b)
            q0 = qlp - D * LP * (np.sign(1 + D * b * (SP - LP)) * np.power(np.abs(1 + D * b * (SP - LP)),
                                         -(1.0 + b) / b))
            qwp = 2 - np.sign(1 + D * b * (HP - SP)) * np.power(np.abs(1 + D * b * (HP - SP)), -1 / b)
            q1 = qwp + D * (1 - HP) * (np.abs(1 + D * b * (HP - SP)) * np.power(np.abs(1 + D * b * (HP - SP)),
                                                                                -(1 + b) / b))
            q = 1 / (q1 - q0)
                    
            b1 = D * (np.sign(1 + D * b * (SP - LP)) * np.power(np.abs(1 + D * b * (SP - LP)), 
                                                                -(1 + b) / b)) * q
                
            a2 = -q0 * q
            b2 = q
            c2 = 1 + D * b * SP
            d2 = -D * b
            e2 = -1/b
                
            a3 = (2 - q0) * q
            b3 = -q
            c3 = 1 - D * b * SP
            d3 = D * b
            e3 = -1 / b
                
            a4 = (qwp-q0-D * HP * (np.sign(1 + D * b * (HP - SP)) * np.power(np.abs(1 + D * b * (HP - SP)), 
                                     -(b + 1) / b))) * q
            b4 = (D * (np.sign(1 + D * b * (HP - SP)) * np.power(np.abs(1 + D * b * (HP - SP)), 
                                    -(b + 1) / b))) * q
              
        if b == -1:             
            res1 = a2 + b2 * np.log(c2 + d2 * image)
            res2 = a3 + b3 * np.log(c3 + d3 * image)
        elif b < 0 or b > 0:
            res1 = a2 + b2 * (np.sign(c2 + d2 * image) * np.power(np.abs(c2 + d2 * image), e2))
            res2 = a3 + b3 * (np.sign(c3 + d3 * image) * np.power(np.abs(c3 + d3 * image), e3))
        else:
            res1 = a2 + b2 * np.exp(c2 + d2 * image)
            res2 = a3 + b3 * np.exp(c3 + d3 * image)
                          
        return np.where(image < LP, b1 * image, 
                        np.where(image < SP, res1, 
                                 np.where(image < HP, res2,
                                          a4 + b4 * image)))
    
                
    def plot(self, D=0, b=0, SP=0, LP=0, HP=1):
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
        
        if self.ghs.__code__.co_argcount == 7:
            axD = fig.add_axes([0.63, 0.4, 0.25, 0.02])
            axb = fig.add_axes([0.63, 0.35, 0.25, 0.02])
            axSP = fig.add_axes([0.63, 0.3, 0.25, 0.02])
            axLP = fig.add_axes([0.63, 0.25, 0.25, 0.02])
            axHP = fig.add_axes([0.63, 0.2, 0.25, 0.02])
            
            b_slider = Slider(
                ax=axb,
                label="b ",
                valmin=-5,
                valmax=15,
                valinit=b
                )
            
        else:
            axD = fig.add_axes([0.63, 0.4, 0.25, 0.02])
            axSP = fig.add_axes([0.63, 0.35, 0.25, 0.02])
            axLP = fig.add_axes([0.63, 0.3, 0.25, 0.02])
            axHP = fig.add_axes([0.63, 0.25, 0.25, 0.02])
        
        
        D_slider = Slider(
            ax=axD,
            label="D ",
            valmin=0,
            valmax=50,
            valinit=D
            )

             
        SP_slider = Slider(
            ax=axSP,
            label="SP ",
            valmin=0,
            valmax=1,
            valinit=SP
            )
             
        LP_slider = Slider(
            ax=axLP,
            label="LP ",
            valmin=0,
            valmax=1,
            valinit=LP
            )
             
        HP_slider = Slider(
            ax=axHP,
            label="HP ",
            valmin=0,
            valmax=1,
            valinit=HP
            )
        
        
        def update(val):
            if self.ghs.__code__.co_argcount == 7:
                ax2.cla()
                ax1.imshow(self.ghs(D_slider.val, b_slider.val, SP_slider.val, LP_slider.val, HP_slider.val), 
                          vmin=0, vmax=1, cmap='gray')
                ax2.hist(self.ghs(D_slider.val, b_slider.val, SP_slider.val, LP_slider.val, HP_slider.val).ravel(), 256, (0, 1))
                ax4.cla()
                ax4.plot(self.x, self.ghs(D_slider.val, b_slider.val, SP_slider.val, LP_slider.val, HP_slider.val, True))
            else:
                ax2.cla()
                ax1.imshow(self.ghs(D_slider.val, SP_slider.val, LP_slider.val, HP_slider.val), 
                          vmin=0, vmax=1, cmap='gray')
                ax2.hist(self.ghs(D_slider.val, SP_slider.val, LP_slider.val, HP_slider.val).ravel(), 256, (0, 1))
                ax4.cla()
                ax4.plot(self.x, self.ghs(D_slider.val, SP_slider.val, LP_slider.val, HP_slider.val, True))

            fig.canvas.draw_idle()
        
        D_slider.on_changed(update)
        SP_slider.on_changed(update)
        LP_slider.on_changed(update)
        HP_slider.on_changed(update)
        if self.ghs.__code__.co_argcount == 7:
            b_slider.on_changed(update)

        resetax = fig.add_axes([0.5, 0., 0.1, 0.05])
        button_reset = Button(resetax, 'Reset', hovercolor='0.5')

        applyax = fig.add_axes([0.3, 0., 0.1, 0.05])
        button_apply = Button(applyax, 'Apply', hovercolor='0.5')

        def reset(event):
            D_slider.reset()
            SP_slider.reset()
            LP_slider.reset()
            HP_slider.reset()
            if self.ghs.__code__.co_argcount == 7:
                b_slider.reset()
            
        button_reset.on_clicked(reset)

        def apply(event):
            if self.ghs.__code__.co_argcount == 7:
                self.image = self.ghs(D_slider.val, b_slider.val, SP_slider.val, LP_slider.val, HP_slider.val)
                b_slider.reset()
            else:
                self.image = self.ghs(D_slider.val, SP_slider.val, LP_slider.val, HP_slider.val)

            D_slider.reset()
            SP_slider.reset()
            LP_slider.reset()
            HP_slider.reset()
            
        button_apply.on_clicked(apply)
        
        plt.show()
        return self.image
        
#---------------- Inverse generalized hyperbolic stretch ----------------------
class InverseGhs(Ghs):
    def __init__(self, image):
        super().__init__(image)
        
    def ghs(self, D, b, SP, LP, HP, plot=False):
        if plot:
            image = self.x
        else: 
            image = self.image
            
        if D == 0:
            return image
        
        elif b == -1:
            qlp = -1 * np.log1p(D * (SP - LP))
            q0 = qlp - D * LP / (1 + D * (SP - LP))
            qwp = np.log1p(D * (HP - SP))
            q1 = qwp + D * (1 - HP) / (1 + D * (HP - SP))
            q = 1 / (q1 - q0)
            
            LPT = (qlp - q0) * q
            SPT = q0 * q
            HPT = (qwp - q0) * q

            b1 = (1 + D * (SP - LP)) / (D * q)
                
            a2 = (1 + D * SP) / D
            b2 = -1 / D
            c2 = -q0
            d2 = -1 / q
            
            a3 = -(1 - D * SP) / D
            b3 = 1 / D
            c3 = q0
            d3 = 1 / q
            
            a4 = HP + (q0 - qwp) * (1 + D * (HP - SP)) / D
            b4 = (1 + D * (HP - SP)) / (q * D)
            
        elif b < 0:
            b = -b
            qlp = (1 - arithm.pow((1 + D * b * (SP - LP)), (b - 1) / b)) / (b - 1)
            q0 = qlp - D * LP * (arithm.pow((1 + D * b * (SP - LP)), -1 / b))
            qwp = (arithm.pow((1 + D * b * (HP - SP)), (b - 1) / b) - 1) / (b - 1)
            q1 = qwp + D * (1 - HP) * (arithm.pow((1 + D * b * (HP - SP)), -1 / b))
            q = 1 / (q1 - q0)
            LPT = (qlp - q0) * q
            SPT = q0 * q
            HPT = (qwp - q0) * q
            
            b1 = arithm.pow(1 + D * b * (SP - LP), 1 / b) / (q * D)
            
            a2 = (1 + D * b * SP) / (D * b)
            b2 = -1 / (D * b)
            c2 = -q0 * (b - 1) + 1
            d2 = (1 - b) / q
            e2 = b / (b - 1)
    
            a3 = (D * b * SP - 1) / (D * b)
            b3 = 1 / (D * b)
            c3 = 1 + q0 * (b - 1)
            d3 = (b - 1) / q
            e3 = b / (b - 1)
            
            a4 = (q0 - qwp) / (D * arithm.pow((1 + D * b * (HP - SP)), -1 / b)) + HP
            b4 = 1 / (D * arithm.pow((1 + D * b * (HP - SP)), -1 / b) * q)
                
        elif b == 0:
            qlp = np.exp(-D * (SP - LP))
            q0 = qlp - D * LP * np.exp(-D*(SP - LP))
            qwp = 2 - np.exp(-D * (HP -SP))
            q1 = qwp + D * (1 - HP) * np.exp(-D * (HP - SP))
            q = 1 / (q1 - q0)
                    
            LPT = (qlp-q0)*q
            SPT = (1-q0)*q
            HPT = (qwp-q0)*q
                    
            b1 = 1/(D * np.exp(-D * (SP - LP)) * q)
                
            a2 = SP
            b2 = 1 / D
            c2 = q0
            d2 = 1/q
                
            a3 = SP
            b3 = -1 / D
            c3 = (2 - q0)
            d3 = -1 / q
                
            a4 = (q0 - qwp)/(D * np.exp(-D * (HP - SP))) + HP
            b4 = 1/(D * np.exp(-D * (HP - SP)) * q)
            
        else: # b > 0
            qlp = arithm.pow(( 1 + D * b * (SP - LP)), -1/b)
            q0 = qlp - D * LP * arithm.pow((1 + D * b * (SP - LP)), -(1 + b) / b)
            qwp = 2 - arithm.pow(1 + D * b * (HP - SP), -1 / b)
            q1 = qwp + D * (1 - HP) * arithm.pow((1 + D * b * (HP - SP)), -(1 + b) / b)
            q = 1 / (q1 - q0)
                    
            LPT = (qlp-q0)*q
            SPT = (1-q0)*q
            HPT = (qwp-q0)*q
                    
            b1 = 1/(D * arithm.pow((1 + D * b * (SP - LP)), -(1 + b) / b) * q)
                    
            a2 = 1 / (D * b) + SP
            b2 = -1/(D * b)
            c2 = q0
            d2 = 1 / q
            e2 = -b
                    
            a3 = -1 / (D * b) + SP
            b3 = 1 / (D * b)
            c3 = (2 - q0)
            d3 = -1 / q
            e3 = -b
                
            a4 = (q0-qwp)/(D * arithm.pow((1 + D * b * (HP - SP)), -(b + 1) / b))+HP
            b4 = 1/((D * arithm.pow((1 + D * b * (HP - SP)), -(b + 1) / b)) * q)
            
        if b == -1:
            res1 = a2 + b2 * np.exp(c2 + d2 * image)
            res2 = a3 + b3 * np.exp(c3 + d3 * image)
        elif b < 0 or b > 0:
            res1 = a2 + b2 * arithm.pow(c2 + d2 * image, e2)
            res2 = a3 + b3 * arithm.pow(c3 + d3 * image, e3)
        else:
            res1 = a2 + b2 * np.log(c2 + d2 * image)
            res2 = a3 + b3 * np.log(c3 + d3 * image)  
        
        return np.where(image < LPT, b1 * image,
                        np.where(image < SPT, res1,
                                 np.where(image < HPT, res2,
                                          a4 + b4 * image)))

# --------------------------- Modified asinh stretch ---------------------------
class Asinh(Ghs):
    def __init__(self, image):
        super().__init__(image)
        
    def ghs(self, D, SP, LP, HP, plot=False):
        if plot:
            image = self.x
        else: 
            image = self.image
        
        if D ==0:
            return image
        else:
            qlp = -np.log(D * (SP - LP) + arithm.pow((D * D * (SP - LP) * (SP - LP) + 1), 0.5))
            q0 = qlp - LP * D * arithm.pow((D * D * (SP - LP) * (SP - LP) + 1), -0.5)
            qwp = np.log(D * (HP - SP) + arithm.pow((D * D * (HP - SP) * (HP - SP) + 1), 0.5))
            q1 = qwp + (1 - HP) * D * arithm.pow((D * D * (HP - SP) * (HP - SP) +1), -0.5)
            q = 1 / (q1 - q0)
        
            a1 = 0
            b1 = D * arithm.pow((D * D * (SP - LP) * (SP - LP) + 1),-0.5)*q
            
            a2 = -q0 * q
            b2 = -q
            c2 = -D
            d2 = D * D
            e2 = SP
        
            a3 = -q0 * q
            b3 = q
            c3 = D
            d3 = D * D
        
            e3 = SP
            a4 = (qwp - HP * D * arithm.pow((D * D * (HP - SP) * (HP - SP) + 1), -0.5) - q0) * q
            b4 = D * arithm.pow((D * D * (HP - SP) * (HP - SP) + 1), -0.5) * q
        
        
            val = c2 * (image - e2) + np.sqrt(d2 * (image - e2) * (image - e2) + 1)
            res1 = a2 + b2 * np.log(val)
            val = c3 * (image - e3) + np.sqrt(d3 * (image - e3) * (image - e3) + 1)
            res2  =a3 + b3 * np.log(val)
            
            return np.where(image < LP, a1 + b1 * image,
                           np.where(image < SP, res1,
                                    np.where(image < HP, res2, 
                                             a4 + b4 * image)))

#------------------------ Inverted modified asinh stretch ----------------------    
class InverseAsinh(Ghs):
    def __init__(self, image):
        super().__init__(image)
        
    def ghs(self, D, SP, LP, HP, plot=False):
        if plot:
            image = self.x
        else: 
            image = self.image
            
        if D == 0:
            return image
        else:
            qlp = -np.log(D * (SP - LP) + arithm.pow((D * D * (SP - LP) * (SP - LP) + 1.0), 0.5))
            q0 = qlp - LP * D * arithm.pow((D * D * (SP - LP) * (SP - LP) + 1.0), -0.5)
            qwp = np.log(D * (HP - SP) + arithm.pow((D * D * (HP - SP) * (HP - SP) + 1.0), 0.5))
            q1 = qwp + (1.0 - HP) * D * arithm.pow((D * D * (HP - SP) * (HP - SP) +1.0), -0.5)
            q = 1.0 / (q1 - q0)
        
            a1 = 0.0
            b1 = D * arithm.pow((D * D * (SP - LP) * (SP - LP) + 1.0),-0.5)*q
        
            a2 = -q0 * q
            b2 = -q
            c2 = -D
            d2 = D * D
            e2 = SP
        
            a3 = -q0 * q
            b3 = q
            c3 = D
            e3 = SP
        
            a4 = (qwp - HP * D * arithm.pow((D * D * (HP - SP) * (HP - SP) + 1.0), -0.5) - q0) * q
            b4 = D * arithm.pow((D * D * (HP - SP) * (HP - SP) + 1.0), -0.5) * q
        
            LPT = a1 + b1 * LP
            SPT = a2 + b2 * np.log(c2 * (SP - e2) + np.sqrt(d2 * (SP - e2) * (SP - e2) + 1.0))
            HPT = a4 + b4 * HP

            ex = np.exp((a2 - self.image) / b2)
            res1 = e2 - (ex - (1.0 / ex)) / (2.0 * c2)
            ex = np.exp((a3 - self.image) / b3)
            res2 = e3 - (ex - (1.0 / ex)) / (2.0 * c3)
            
            return np.where((image < LPT), (image - a1) / b1,
                           np.where((image < SPT), res1,
                                    np.where((image < HPT), res2,
                                             (image - a4) / b4)))

        










            