import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SEASHELL3=(205,197,191)
BURLYWOOD1=(255,211,155)
LIGHTCYAN1=(224,255,255)


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class Snowflake():
	'''
	==========================================TASK ONE=========================================
	This class will be used to create the Snowflake objects.
	It takes as a parameter: 
		* size - an integer that tells us how big we want the snowflake to be
		* position - a tupe that tells us the coordinates of the snowflake (x,y) 
		* wind - a boolean that lets us know if there is any wind or not. 
				wind is automatically set to False.
	'''
	def __init__(self, size, position, wind=False):
		self.size=size
		self.position=position
		self.wind=wind

		# define the __init__ function here! 
	
	def fall(self, speed):
		"""
		==========================================TASK TWO=========================================
		This class updates the y position of the Snowflake by the speed at which it is falling to 
		simulate a falling snowflake. If wind == True, the x direction of the snowflake changes
		by a random amount in the same direction, simulating wind blowing the snowflakes horizontally. 
		
		fall takes as a parameter:
			* speed - an integer that represnts the speed at which the snowflake is falling 
					in the y-direction.  
					A positive integer will have the snowflake falling down the screen. 
					A negative integer will have the snowflake falling up the screen. 
		"""
		# x=0
		# y=0
		# y=y+
		new_y= self.position[1] + speed #calculate new y position by adding speed to it
		
		# position = position + speed
		if self.wind==True:
			new_x= self.position[0] + random.randint(0,10)
		else:
			new_x = self.position[0]
		# self.yposition+=speed 
		# # if self.wind == True:
		# 	self.speed += self.position - 50

		new_position = [new_x, new_y] #make a new position list
		# new_position.append(position[0],new_y) #add my old x position
		self.position=new_position

		
	def draw(self):
		"""
		==========================================TASK THREE=========================================
		Draws this Snowflake on the screen using the pygame.draw.circle method and this 
		Snowflake's attributes.
		"""

		# Hannah and Maria - this line should work now! The problem was that you updated the object Snowflake
		# to take a xposition and a yposition but you still called it on lines 109-110 with the position parameter.
		# I've updated those lines too so it should work. Good work so far!
		pygame.draw.circle(screen,WHITE,self.position, self.size)
		
		

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 1

# this list will hold our snowflakes
snow_list = []

# my_snowflake= Snowflake(10, (100,100))
snow_list= []


# maria=Snowflake(10, 0,(random.randint(0,700)),False)
# hannah=Snowflake(10, 0,(random.randint(0,700)),False)
# -------- Main Program Loop -----------
while not done:
	my_snowflake= Snowflake((random.randint(1,6)), (random.randint(0,700),0))
	snow_list.append(my_snowflake)
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here

	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BLUE)
	for i in snow_list:
		i.draw()
		i.fall(10)

	# --- Drawing code should go here
	# Begin Snow

	'''
	==========================================TASK FOUR=========================================
	Create an instance of your Snowflake object with a random x position and y position = 0 
	(because snowflakes fall from the sky!). Add this new Snowflake to the list snow_list.
	'''
	# maria=Snowflake( 5, 0,[random.randint(0,700),0], wind=False)
	# hannah=Snowflake( 5, 0,[random.randint(0,700),0], wind=False)
	# maria=Snowflake( 5, 0,(random.randint(0,700)),False)
	# hannah=Snowflake( 5, 0,(random.randint(0,700)),False)



	'''
	==========================================TASK FIVE=========================================
	For every flake in snow_list, draw the flake and then call fall() to have it update its 
	position to simulate a fall. 
	'''

	my_snowflake.draw()
	my_snowflake.fall(10)

	# End Snow

	# --- Update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
