# imports small python files I made

#%% IMPORTS & VARS

from fib import Fibber


#%% MAIN

print("starting...")

if __name__ == "__main__":
	print("I hope this runs...")
	# objects
	Fool = Fibber(100)
	
	# other code
	Fool.create_sequence()
	Fool.uno_card()
