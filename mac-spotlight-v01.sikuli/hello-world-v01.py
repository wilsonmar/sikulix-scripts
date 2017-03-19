#AppPath = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" # on Windows only.
#App.open(PathFirefox)
#openApp("Safari")
#switchApp("Safari")
click("1489860625202.png") # Spotlight search on Apple menu
wait(1)
click("mac-spotlight-entry.png")
wait(3)
# ERROR: Script does not type the beginning of the text:
click()
type("hello world")
wait(1)
# exit() # stop here
