import smtplib
from datetime import datetime
from time import sleep
import os

current_script_path = os.path.abspath(__file__)
project_folder_path = os.path.dirname(os.path.dirname(current_script_path))
presets_file_path = os.path.join(project_folder_path, "presets", "presets.txt")

class colors:
    off = "\033[0m"
    
    class regular:
        black="\033[0;30m"
        red= "\033[0;31m"
        green="\033[0;32m"
        yellow= "\033[0;33m"
        blue= "\033[0;34m"
        purple= "\033[0;35m"
        cyan= "\033[0;36m"
        white= "\033[0;37m"

    class bold:
        black="\033[1;30m"
        red="\033[1;31m"
        green="\033[1;32m"
        yellow="\033[1;33m"
        blue="\033[1;34m"
        purple="\033[1;35m"
        cyan="\033[1;36m"
        white="\033[1;37m"
   

def spam():
    try:
        save = []
        default = "None"
        def_en = True
        with open(presets_file_path, 'r', encoding="utf-8") as save_file:
            save.append(save_file.read().replace("\n", "::"))
        split_splited_save = []
        do_Break = False
        for x in range(0, len(save)):
            splited_save = save[x].split("::")
            for y in range(0, len(splited_save)):
                if do_Break: break
                split_splited_save = splited_save[y].split(":")
                if split_splited_save[6] == "True":
                    do_Break = True
                    break
        print("\n" + colors.bold.green + "Using preset \"" + colors.regular.purple + f"{split_splited_save[0]}" + colors.bold.green + "\"." + colors.off)
        count = int(split_splited_save[1])
        server = smtplib.SMTP(split_splited_save[4], int(split_splited_save[5]))
        server.starttls()
        server.login(split_splited_save[2], split_splited_save[3])
        enemy = input("\n" + colors.bold.green + "Input your " + colors.regular.red + "ENEMY" + colors.bold.green + " Mail: " + colors.regular.purple)
        print(colors.off, end="")
        text = input("\n" + colors.bold.green + "Input text of your messages: " + colors.regular.purple)
        print(colors.off, end="")
        while count > 0:
            server.sendmail(split_splited_save[2], enemy, text)
            count -= 1
            date = datetime.today()
            print(colors.bold.green + "Message sent at " + colors.regular.purple + f"{date}" + colors.bold.green + "." + colors.off)
    except Exception as e:
        print(colors.regular.red + f"Error: {e}" + colors.off)

def presetslist():
    try:
        print("\n", end="")
        saved_pres = []
        do_Enable = False
        save_num = str
        save_apply = []
        with open(presets_file_path, 'r', encoding="utf-8") as pres_file:
            saved_pres.append(pres_file.read().replace("\n", "::"))
        with open(presets_file_path, 'r', encoding="utf-8") as pres_file:
            i = 1
            o = 0
            output = ""
            for line in pres_file:
                preset = line.split(":")
                output = colors.regular.green + str(i) + '| '  + "Name: " + colors.bold.purple + f"{preset[0]}" + colors.regular.green + ", Count of messages: " + colors.bold.purple + f"{preset[1]}" + colors.regular.green + ", Sender Mail: " + colors.bold.purple + f"{preset[2]}" + colors.regular.green + ", Password: " + colors.bold.purple + f"{preset[3]}" + colors.regular.green + ", SMTP Server: " + colors.bold.purple + f"{preset[4]}" + colors.regular.green + ", SMTP Port: " + colors.bold.purple + f"{preset[5]}" + colors.regular.green + ", Enabled: " + colors.bold.purple + f"{preset[6]}" + colors.regular.green + "." + colors.off
                i += 1
                o += 1
                print(output)
            if output == "":
                print(colors.bold.red + "There is no Presets!" + colors.off)
                sleep(1.5)
            else:
                print("\n" + colors.regular.purple + "TIP: To enable preset Enter number from 1 to endless." + colors.off)
                print("\n" + colors.bold.green + "If you wanna to disable preset enter \"" + colors.bold.purple + "disable" + colors.bold.green + "\"." + colors.off)
                print("\n" + colors.bold.green + "If you wanna to remove preset enter \"" + colors.bold.purple + "remove" + colors.bold.green + "\"." + colors.off)
                save_num = input("\n" + colors.regular.yellow + "Enter the number of preset(enter \"" + colors.bold.purple + "cancel" + colors.regular.yellow + "\" to cancel): " + colors.regular.purple)
                print(colors.off, end="")
                if save_num == "cancel":
                    print("\n" + colors.bold.green + "Successfully canceled!" + colors.off)
                    sleep(1.5)
                elif save_num == "remove":
                    del_num = input("\n" + colors.regular.yellow + "Enter the number of preset: " + colors.regular.purple)
                    print(colors.off, end="")
                    save_apply = saved_pres[0].split("::")
                    save_apply.pop((int(del_num) - 1))
                    save_apply = "\n".join(save_apply)
                    with open(presets_file_path, "w", encoding="utf-8") as save_file:
                        save_file.write(save_apply)
                    print("\n" + colors.bold.green + "Successfully removed preset." + colors.off)
                    sleep(1.5)
                elif save_num == "disable":
                    dis_num = input("\n" + colors.regular.yellow + "Enter the number of preset: " + colors.regular.purple)
                    dis_num = int(dis_num)
                    dis_num -= 1
                    save_apply = saved_pres[0].split("::")
                    save_for_dis = save_apply[dis_num].split(":")
                    save_for_dis[6] = "False"
                    save_apply[dis_num] = ":".join(save_for_dis)
                    save_apply = "\n".join(save_apply)
                    with open(presets_file_path, "w", encoding="utf-8") as apply:
                        apply.write(save_apply)
                    print("\n" + colors.bold.green + "Successfully disabled preset with name \"" + colors.bold.purple + f"{save_for_dis[0]}" + colors.bold.green + "\"." + colors.off)
                    sleep(1.5)
                else:
                    do_Enable = True
        if do_Enable:
            saves = saved_pres[0].split("::")
            save_num = int(save_num)
            save_num -= 1
            for x in range(0, len(saves)):
                some_save = saves[x].split(":")
                if some_save[6] == "True": some_save[6] = "False"
                saves[x] = ":".join(some_save)
            save_apply = saves[save_num].split(":")
            save_apply[6] = "True"
            saves[save_num] = ":".join(save_apply)
            saving = "\n".join(saves)
            with open(presets_file_path, "w", encoding="utf-8") as save_file:
                save_file.write(saving)
            print(colors.bold.green + "\n" + f"Successfully enabled preset number {save_num + 1}" + colors.off)
            sleep(1.5)
    except Exception as e:
        print(colors.regular.red + f"Error: {e}" + colors.off)

def detect_enabled():
    try:
        save = []
        default = "None"
        def_en = True
        with open(presets_file_path, 'r', encoding="utf-8") as save_file:
            save.append(save_file.read().replace("\n", "::"))
        if save[0] != "":
            for x in range(0, len(save)):
                splited_save = save[x].split("::")
                for y in range(0, len(splited_save)):
                    split_splited_save = splited_save[y].split(":")
                    if split_splited_save[6] == "True":
                        def_en = False
                        return split_splited_save[0]
        if def_en:return default
    except Exception as e:
        print(colors.regular.red + f"Error: {e}" + colors.off)

def create_preset():
    try:
        save = []
        with open(presets_file_path, 'r', encoding="utf-8") as save_file:
            save.append(save_file.read().replace("\n", "::"))
        name = input("\n" + colors.regular.yellow + "Please enter name of preset: " + colors.regular.purple)
        countOfMessages = input("\n" + colors.regular.yellow + "Please enter count of messages: " + colors.regular.purple)
        countOfMessages = int(countOfMessages)
        countOfMessages = str(countOfMessages)
        user_mail = input("\n" + colors.regular.yellow + "Please enter your email: " + colors.regular.purple)
        user_pass = input("\n" + colors.regular.yellow + "Please enter your trusted application password: " + colors.regular.purple)
        smtp_server = input("\n" + colors.regular.yellow + "Please enter SMTP Server you want: " + colors.regular.purple)
        smtp_port = input("\n" + colors.regular.yellow + "Please enter SMTP(TLS) Port you want: " + colors.regular.purple)
        smtp_port = int(smtp_port)
        smtp_port = str(smtp_port)
        newPreset = []
        newPreset.append(name)
        newPreset.append(countOfMessages)
        newPreset.append(user_mail)
        newPreset.append(user_pass)
        newPreset.append(smtp_server)
        newPreset.append(smtp_port)
        newPreset.append("False")
        save.append(":".join(newPreset))
        if save[0] != "":
            save_joined = "::".join(save)
            save_joined = save_joined.replace("::", "\n")
        else: save_joined = "".join(save)
        with open(presets_file_path, "w", encoding="utf-8") as end:
            end.write(save_joined)
        print("\n" + colors.bold.green + "Successfully added preset with name \"" + colors.regular.purple + f"{name}" + colors.bold.green + "\"" + colors.off)
        sleep(1.5)
    except Exception as e:
        print(colors.regular.red + f"Error: {e}" + colors.off)