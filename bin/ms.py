import json
import sys

f=open(sys.argv[2], "r"); script = json.load(f)

line = 0
checkline = 0
var = None
dev = False

def devlog(msg):
    if dev == True:
        print("[DEVLOG]: " + str(msg))
    else:
        pass
if sys.argv[1] == "--devrun":
    dev=True
    print("Developer mode enabled!")
    print("Developer mode is a WIP right now.\n----------------------------------------\n")
elif sys.argv[1] == "--run":
    pass
else:
    print("Argument 1 must be \"--run\" or \"--devrun\".")
    sys.exit()

while True:
    checkline = checkline + 1
    if str(checkline) in script:
        pass
    else:
        print("err: No end function in the script.")
        sys.exit()
    if "end" in script[str(checkline)]:
        if "declare" in script:
            var = script['declare']
            break
        else:
            print("err: No declare value in the script.\nDid you forget to add \"declare\": {}\"?")
            sys.exit()
    else:
        pass
        


while True:
    f=open(sys.argv[2], "r"); script = json.load(f)
    line = line + 1
    if str(line) in script:
        if 'writeln' in script[str(line)]:
            devlog(f"Written line.")
            exec(f"print({script[str(line)]['writeln']})")
        elif 'scanln' in script[str(line)]:
            if 'out' in var:
                devlog(f"Written line.")
                exec(f"var['out'] = input({script[str(line)]['scanln']})")
                devlog(f"Logged line to var['out'].")
            else:
                print("err: 'out' variable needed to use the 'scanln' function.")
                sys.exit()
        elif 'end' in script[str(line)]:
            devlog(f"Ended script with 'end' function.")
            print(script[str(line)]['end'])
            sys.exit()
        elif 'norun' in script[str(line)]:
            devlog(f"norun detected. Ignoring line.")
            pass
        elif 'log' in script[str(line)]:
            exec(f"devlog(\"[Script]: \" + {str(script[str(line)]['log'])})")
        else:
            print(f"err: no declared function in line.\nLn {str(line)} | ==> {script[str(line)]}")
            sys.exit()
    with open(sys.argv[2], 'w') as f:
        json.dump(script, f, indent=4)
