from scripts.functions import *

def Start():
    while True:
        chosen_preset = detect_enabled()
        print("\n" + colors.regular.red + "███████╗███╗░░░███╗░█████╗░░░███╗░░██╗░░░░░  ██████╗░░█████╗░███╗░░░███╗██████╗░██████╗░██████╗░\n██╔════╝████╗░████║██╔══██╗░████║░░██║░░░░░  ██╔══██╗██╔══██╗████╗░████║██╔══██╗╚════██╗██╔══██╗\n█████╗░░██╔████╔██║███████║██╔██║░░██║░░░░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝░█████╔╝██████╔╝\n██╔══╝░░██║╚██╔╝██║██╔══██║╚═╝██║░░██║░░░░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗░╚═══██╗██╔══██╗\n███████╗██║░╚═╝░██║██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝██████╔╝██║░░██║\n╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝" + colors.off)
        print("\nMenu: Chosen preset is [" + colors.regular.green + f"{chosen_preset}" + colors.off + "]\n" + colors.regular.yellow + "1. Presets.\n2. Create new preset" + colors.bold.red + "\n3. ATTACK!" + colors.regular.red + "\n4. Exit." + colors.off)
        choice = input(colors.regular.yellow + "Enter your choice: " + colors.regular.purple)
        print(colors.off, end="")
        if choice == "1":
            presetslist()
        elif choice == "2":
            create_preset()
        elif choice == "3":
            spam()
        elif choice == "4":
            print("\n" + colors.regular.yellow + "Bye!" + colors.off)
            sleep(1.5)
            break
        else:
            print("\n" + colors.bold.red + "Invalid choice!" + colors.off)
            sleep(1.5)
    