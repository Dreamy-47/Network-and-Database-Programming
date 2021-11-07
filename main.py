from json import decoder
import sqlite3 as lite
import os
import json
import csv

Equip_name = ["ATK","ATK%","DEF","DEF%","HP","HP%","SPD","CC","CD","EF","ER"]
Gear_name = ["Weapon","Helmet","Armor","Necklace","Ring","Boots"]

def add_E():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EquipSystem.db")
    con = lite.connect(db_path)
    cur=con.cursor()
    js_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "setting.json")
    with open(js_path , 'r',encoding="utf8") as jfile:
        jdata = json.load(jfile)
    equip_set=[]
    val_set=[0,0,0,0,0,0,0,0,0,0,0,0,0,"",""]
    total_value=0
    gear = 0
    while(True):
        print("Select type of gear:")
        print(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gear_menu.txt")).read())
        print('-'*17)
        gear = int(input("> ")[0])-1
        if(gear>=6 or gear<0):
            print("wrong gear number")
            print('-'*17)
            continue
        print("what main type does this equip have?")
        print(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "equip_typemenu.txt")).read())
        print('-'*17)
        main_opt = int(input("> ")[0])-1
        if(main_opt>=11 or main_opt<0):
            print("wrong type number")
            print('-'*17)
            continue
        val_set[0] = int(input(f"{Equip_name[main_opt]}  Value:"))
        val_set[-1] = Equip_name[main_opt]
        val_set[-2] = Gear_name[gear]
        break
    
    print('-'*17)
    print("what type does this equip have? (select 4 types)")
    print(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "equip_typemenu.txt")).read())
    print('-'*17)
    for i in range(4):
        opt = int(input("> ")[0])
        for V in equip_set:
            if opt == V or opt >11:
                print("this type has been exist")
                i = i-1
                break
        equip_set.append(opt)
        val = int(input(f"{Equip_name[opt-1]}  Value:"))
        val_set[opt] = val
        total_value += val*jdata["easy_show"][str(opt)]
    val_set[-3] = total_value
    command = '''Insert into equip (main_val,ATK_N,AATK,DEF_N,DDEF,HP_N,HHP,SPD,CC,CD,EF,ER,TV,gear,main_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    #for i in range(11):
        #val_set[i] = str(val_set[i])
    #command = f"Insert into equip (ATK_N,AATK,DEF_N,DDEF,HP_N,HHP,SPD,CC,CD,EF,ER,TV)\
    #    Values( {val_set[0]}, {val_set[1]}, {val_set[2]}, {val_set[3]}, {val_set[4]}, \
    #       {val_set[5]}, {val_set[6]}, {val_set[7]}, {val_set[8]}, {val_set[9]}, {val_set[10]}, {(total_value)} "
    
    
    #print (command,val_set)
    cur.execute(command,val_set)
    print("-"*17)
    print("Score :", total_value)
    print( "Successfully add equip")
    print("-"*17)
    con.commit()
    con.close()

def show_E():
    print('-'*17)
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EquipSystem.db")
    con = lite.connect(db_path)
    cur=con.cursor()
    print("choose one:")
    print(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gear_menu.txt")).read())
    print(" 7) all")
    opt = int(input("> ")[0])
    print('-'*17)
    command = ""
    if opt != 7 :
        command = f"select * from equip where gear = '{Gear_name[opt-1]}'"
        #print (command)
    else:
        command = "select * from equip"
    gear_list = cur.execute(command) 
    for row in gear_list:
        print("ID:",row[0])
        print("Gear:",row[-2])
        print("Main type:",row[1])
        print("Value :",row[-1])
        print("Total Value:",row[-3])
        #if(row[1]>0):
            #print("ATK :",row[1])
        if int(row[2])>0:
            print("ATK :",row[2])
        if int(row[3])>0:
            print("ATK% :",row[3])
        if int(row[4])>0:
            print("DEF :",row[4])
        if int(row[5])>0:
            print("DEF% :",row[5])
        if int(row[6])>0:
            print("HP :",row[6])
        if int(row[7])>0:
            print("HP% :",row[7])
        if int(row[8])>0:
            print("SPD :",row[8])
        if int(row[9])>0:
            print("CC :",row[9])
        if int(row[10])>0:
            print("CD :",row[10])
        if int(row[11])>0:
            print("EF :",row[11])
        if int(row[12])>0:
            print("ER :",row[12])
        print("-"*17)
    con.close()
    

    
def remove_E():
    print("-"*17)
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EquipSystem.db")
    con = lite.connect(db_path)
    cur=con.cursor()
    print("input ID")
    did = int(input("> "))
    command = f"DELETE  from equip WHERE equip_uid = {did}"
    cur.execute(command)
    con.commit()
    print( "Successfully delete equip")
    print("-"*17)
    con.close()

def add_file():
    print("-"*17)
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EquipSystem.db")
    con = lite.connect(db_path)
    cur=con.cursor()
    csv_path = input("input csv name:")
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), csv_path+".csv")
    with open(csv_path,'r') as csv_file:
        for rows in (csv.reader(csv_file,delimiter=',')):
            #print(rows[-1])
            if rows:
                print(rows)
                cur.execute("INSERT INTO equip (main_type,ATK_N,AATK,DEF_N,DDEF,HP_N,HHP,SPD,CC,CD,EF,ER,TV,gear,main_val) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    con.commit()
    con.close()
    print("loading file success")
    print('-'*17)

def out_file():
    print("-"*17)
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EquipSystem.db")
    con = lite.connect(db_path)
    cur=con.cursor()
    command = "select * from equip"
    cur.execute(command) 
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.csv"),'w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        #csv_out.writerow([d[0] for d in cur.description])
        for result in cur:
            csv_out.writerow(result[1:])
    con.close()
    print("output file success")
    print("-"*17)

def main( ):
  while True:
    print("Welcome Equip System")
    print("-"*17)
    print("menu")
    print("    1)add a new equip and get score")
    print("    2)show equip")
    print("    3)remove equip")
    print("    4)add file")
    print("    5)output file")
    print("    6)exit")
    print("-"*17)
    opt = int(input("> ")[0])
    if opt == 1:
        add_E()
    elif opt == 2:
        show_E()
    elif opt == 3:
        remove_E()
    elif opt ==4:
        add_file()
    elif opt == 5:
        out_file()
    elif opt == 6:
        break
    else:
      print('Non-support operation')

if __name__ == "__main__":
  main( )