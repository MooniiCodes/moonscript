import sys
import os
import alias as cmds

cmds.autoexec()

# file_path = "myFile.txt"
file_path = sys.argv[1]
var = {}

class stdio:
    def input(question, output):
        exec(f"var['{output}'] = input('{question}')")
    def let(varname, value):
        exec(f"var['{varname}'] = '{value}'")

try:
    with open(file_path, 'r') as file:
        for templine in file:
            line = templine.strip()
            # Functions and stuff
            if line[-1] == ";":
                cmds.out = False
                cmd = line[:-1]
                cmds.cmd = cmd

                if line == "":
                    pass
                elif cmd[:6] == "print ":
                    exec(f"print({cmd[6:]})")
                elif cmd[:6] == "input ":
                    exec(f"stdio.input({cmd[6:]})")
                elif cmd[:4] == "let ":
                    exec(f"stdio.let({cmd[4:]})")
                elif cmd[:5] == "exec ":
                    exec(f"os.system('{cmd[5:]}')")
                else:
                    cmds.cmds()
                    if cmds.out == True:
                        print("That function does not exist.")
                        sys.exit()
            else:
                print("Error: Line must end with a semicolon.")
                sys.exit()
            
# Error handling

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"Syntax: {e}")