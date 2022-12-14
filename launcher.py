import os
import subprocess

main_path =os.path.realpath("./main.py")
#main_path = "D:\\Polytechnique\\MA1\\ProjH402\\SpheroV2\\main.py"
print(main_path)

Bolt_name = ["SB-C7C7","SB-3CE4","SB-7F73","SB-31F6","SB-645E","SB-89C3","SB-9D95","SB-6D85","SB-AA77","SB-80F2","SB-719D"]

squadof = 2
for i in range (squadof): 
    subprocess.call('python '+main_path+ ' ' +Bolt_name[i], creationflags=subprocess.CREATE_NEW_CONSOLE)

