import os

def fun_changefiles(g):

    o=g;
    i=[]

    path1 = '/home/mohammad/Desktop/project/'+g+'/menu.php';
    path2 = '/home/mohammad/Desktop/project/'+g+'/radio_info.php';
    path3 = '/home/mohammad/Desktop/temp.txt';

    ###################################################
    # 1: read from temp file for check Duplicate path and log it
    #f3 = open(path3 , 'a') #"a" - Append - will create a file if the specified file does not exist
    #f3.close()
    #f3 = open(path3 , 'r')
    #lines3 = f3.readlines()
    #f3.close()

    #f3 = open(path3,"r")
    #for line3 in lines3:
    #    i.append(line3[:-1])

    #    f3.close()
        #print(i);

    if os.path.exists(path1) == False or os.path.exists(path2) == False :
        print ('\n');
        print('Error: This  path is not exist' );

        worksheet[addr_cell_write] = 'Error: not exist';
        workbook.save("trial.xls")

        log = open('/home/mohammad/Desktop/log.txt',"a")
        log.write('Error: This  path is not exist -->' )
        log.write(o)
        log.write(', cell_add:')
        log.write(addr_cell_read)
        log.write('\n')
        return 1;



    if g not in i :
        #i.append(g)
        f3 = open(path3,"a")
        f3.write(g)
        f3.write('\n')
        #print(i);
    else:
        print ('\n');
        print('Error: This  path has already been entered' );

        worksheet[addr_cell_write] = 'Error: Duplicate path';
        workbook.save("trial.xls")

        log = open('/home/mohammad/Desktop/log.txt',"a")
        log.write('Error: This  path has already been entered -->' )
        log.write(o)
        log.write(', cell_add:')
        log.write(addr_cell_read)
        log.write('\n')
        return 1;


    ####################################################################
    # change for menu.php

    with open("/home/mohammad/Desktop/project/192.168.1.1/menu.php" , 'r') as infile:
        readline=[]
        for line in infile:
            readline.append(line)
        #f1 = open(path1)
        #lines1 = f1.readlines()
        #f1.close()
    ali=0;
    f1 = open(path1,"w")
    for line1 in readline:
        ali=ali+1;
        print(ali);
        p=readline[2114];
        q=readline[2115];
        if line1 not in (p , q ) :
            f1.write(line1)
    f1.close()

    ##################################################################
    # change for radio_info.php
    #f2 = open(path2)
    #lines2 = f2.readlines()
    #f2.close()

    #f2 = open(path2,"w")
    #for line2 in lines2:
    #    if line2 not in (lines2[int(0)] , lines2[int(1)] ) :
    #        f2.write(line2)
    #f2.close()

    #################################################################
    #o=g;
    worksheet[addr_cell_write] = 'successfully: ' + val_cell_read;
    workbook.save("trial.xls")

    log = open('/home/mohammad/Desktop/log.txt',"a")
    log.write(o)
    log.write(' :changing is created successfully')
    log.write(', cell_add:')
    log.write(addr_cell_read)
    #log.write(' with content: ')
    log.write('\n')
    print ('\n');
    print('successfully completed');

    #return 1;
########################
########################
########################

i=['a', 'b' ,'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'];
import openpyxl
###
input_excel_path = input('pls enter src excel path(for EXP: /home/mohammad/Desktop/salam.xlsx): ');
if os.path.exists(input_excel_path) == False :
    print ('\n');
    print('Error: This  enter is not exist' );
    exit()
workbook = openpyxl.load_workbook(input_excel_path)
sheet= input('pls enter sheet name (important it is case sensitive for EXP:Sheet1 ) : ')
worksheet = workbook.get_sheet_by_name(sheet)

input_excel_src_column = input('pls enter src column  (for EXP : a ) : ');
input_excel_log_column = input('pls enter log column (for EXP : a ) : ');
info = '\n'+'Information ::: '+'\n'+'input_excel_path :' + input_excel_path+'\n'+'sheet name :' + sheet+'\n'+'src column: '+input_excel_src_column+'\n'+'log column: '+input_excel_log_column;
OK = input(info+"\nif you confirm this info pls click Enter")
addr_cell_log = input_excel_log_column + str(1);
#val_cell_log = worksheet[input_excel_log_column].value;
worksheet[addr_cell_log] = 'log';
workbook.save("trial.xls")
####



columns=worksheet.columns
rows=worksheet.rows
len_rows=len(rows)
len_columns=len(columns)




for num in range (len_rows - 1):
    #addr_cell = i[num]+str(2);
    addr_cell_read = input_excel_src_column + str(num+2);
    addr_cell_write = input_excel_log_column + str(num+2);
    val_cell_read = worksheet[addr_cell_read].value;
    val_cell_read = str(val_cell_read)
    #val_cell_read = val_cell_read[:-3]
    fun_changefiles(val_cell_read)
    print('info -->' , 'ip:' ,val_cell_read , ', cell_add:' , addr_cell_read );
    #worksheet[addr_cell_write] = val_cell_read;
    #workbook.save("trial.xls")
print ('\n');
print ('\n');
print ('((( ___thank you for choice this program__)))');
#print (val_cell_read);
