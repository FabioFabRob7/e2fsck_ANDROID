import subprocess

print("///////////////////////\n/  e2fsck_ANDROID.py  /\n/   by FabioFabRob7   /\n///////////////////////\n")
input("First of all you need to have a smartphone with root permissions. When you have root, hit enter. . .")
def OS():
    OS_select = input("Select your PC OS:\n1) Windows\n2) Linux\n")
    if OS_select == "1":
        print("Connection via ADB Shell")
        subprocess.call(["adb.exe", "devices"])
        print("Get root")
        subprocess.call(["adb.exe", "root"])
        print("/ mounting")
        subprocess.call(["adb.exe", "shell", "mount", "/"])
        print("File system checker start!")
        subprocess.call(["adb.exe", "shell", "e2fsck", "-p", "/"])
        print("Finish!!!")
    elif OS_select == "2":
        ADB_FB_L()
        print("Connection via ADB Shell")
        subprocess.call(["adb", "devices"])
        print("Get root")
        subprocess.call(["adb", "root"])
        print("/ mounting")
        subprocess.call(["adb", "shell", "mount", "/"])
        print("File system checker start!")
        subprocess.call(["adb", "shell", "e2fsck", "-p", "/"])
        print("Finish!!!")
    else:
        OS()

def ADB_FB_L():
    ADB_FASTBOOT_value = input("ADB (Android Debug Bridge) and Fastboot will be downloaded, you want to continue Y/N:")
    if ADB_FASTBOOT_value == "y" or ADB_FASTBOOT_value == "Y":
        subprocess.call(["sudo","apt","install","adb","fastboot"])
    elif ADB_FASTBOOT_value == "n" or ADB_FASTBOOT_value == "N":
        exit
    else:
        ADB_FB_L()

OS()
