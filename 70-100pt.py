#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=1,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right" , background ="pink")
       	    self.right.grid(row=2,column=2)
       	    #bind for 2nd button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    #bind for 3rd button 
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left" , background ="yellow")
       	    self.left.grid(row=2,column=0)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    #bind for 4th button
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down" , background ="purple")
       	    self.down.grid(row=3,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	def rightClicked(self, event):
	    global oval 
	    global player
	    drawpad.move(player,20,0)	
	def leftClicked(self, event):
	    global oval 
	    global player
	    drawpad.move(player,-20,0)	
	def downClicked(self, event):
	    global oval 
	    global player
	    drawpad.move(player,0,20)	
	    
	      	
#moving things
circle = drawpad.create_oval(100,500,120,400,fill='green')     	  	  
direction = 1
def animation():
    global direction
    x1,y1,x2,y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width():
        direction=-1 
    drawpad.move(circle,direction,0)
    drawpad.after(5, animation)
animation()
	      	  	  	
circle2 = drawpad.create_oval(150,300,100,200,fill='green')     	  	  
direction = 1
def animation2():
    global direction
    x1,y1,x2,y2 = drawpad.coords(circle2)
    if x2 > drawpad.winfo_width():
        direction=-1 
    drawpad.move(circle2,direction,0)
    drawpad.after(5, animation2)
animation2()

circle3 = drawpad.create_oval(200,400,160,300,fill='green')     	  	  
direction = 1
def animation3():
    global direction
    x1,y1,x2,y2 = drawpad.coords(circle3)
    if x2 > drawpad.winfo_width():
        direction=-1 
    drawpad.move(circle3,direction,0)
    drawpad.after(5, animation3)
animation3()		
	      	  	  			
	      	  	  					
app = MyApp(root)
root.mainloop()