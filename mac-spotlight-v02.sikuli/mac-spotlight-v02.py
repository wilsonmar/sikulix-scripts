# by Wilson Mar
click("mac-search.png") # Spotlight search on Apple menu
wait(1)
click("mac-spotlight-entry.png") #mac-spotlight-entry.png
wait(1)
# ERROR: Script does not type the beginning of the text:
#click()
#cursor right?
type("hello world")
wait(1)
# exit() # stop here