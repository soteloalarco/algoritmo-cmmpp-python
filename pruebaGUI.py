from tkinter import *

root = Tk()

def test_Val(inStr,acttyp):
    if acttyp == '1':  # insert
        #if not inStr[len(inStr)-1]=='.':
            #return False
        print(len(inStr))

        if (not inStr[len(inStr)-1].isdigit() and not inStr[len(inStr)-1]=='.'):
            return False

    return True

entry = Entry(root, validate="key")
entry['validatecommand'] = (entry.register(test_Val),'%P','%d')
entry.pack()

root.mainloop()