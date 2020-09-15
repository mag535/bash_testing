# imports small python files I made

#%% IMPORTS & VARS

from fib import Fibber


#%% MAIN

print("starting...\n")

if __name__ == "__main__":
	# objects
	Fool = Fibber(50)
	
	# other code
	Fool.create_sequence()
	#Fool.uno_card('*', '*')
	Fool.twist('.')
