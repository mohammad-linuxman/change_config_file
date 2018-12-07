import os

def fun_changefiles(g):

    o=g;
    i=[]

    path1 = '/home/mohammad/Desktop/project/'+g+'/menu.php';
    path2 = '/home/mohammad/Desktop/project/'+g+'/radio_info.php';
    path3 = '/home/mohammad/Desktop/temp.txt';

    ###################################################
    # 1: read from temp file for check Duplicate path and log it
    f3 = open(path3 , 'r+')
    lines3 = f3.readlines()
    f3.close()

    f3 = open(path3,"r")
    for line3 in lines3:
        i.append(line3[:-1])

        f3.close()
        #print(i);

    if os.path.exists(path1) == False or os.path.exists(path2) == False :
        print ('\n');
        print('Error: This  path is not exist' );

        worksheet[addr_cell_write] = 'Error: not exist';
        workbook.save("trial.xls")

        log = open('/home/mohammad/Desktop/log.txt',"a")
        log.write('Error: This  path is not exist -->' )
        log.write(o)
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
        log.write('\n')
        return 1;


            ####################################################################
            # change for menu.php


    f1 = open(path1)
    lines1 = f1.readlines()
    f1.close()

    f1 = open(path1,"w")
    for line1 in lines1:
        if line1 not in (lines1[int(0)] , lines1[int(1)] ) :
            f1.write(line1)
    f1.close()

                    ############################################################
                    # change for radio_info.php
    f2 = open(path2)
    lines2 = f2.readlines()
    f2.close()

    f2 = open(path2,"w")
    for line2 in lines2:
        if line2 not in (lines2[int(0)] , lines2[int(1)] ) :
            f2.write(line2)
    f2.close()

                            ####################################################
                            #o=g;
    worksheet[addr_cell_write] = 'successfully: ' + val_cell_read;
    workbook.save("trial.xls")

    log = open('/home/mohammad/Desktop/log.txt',"a")
    log.write(o)
    log.write(' :changing is created successfully')
    #log.write(' with content: ')
    log.write('\n')
    print ('\n');
    print('successfully completed');

    return 1;
########################
########################
########################

i=['a', 'b' ,'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'];
import openpyxl
workbook = openpyxl.load_workbook('salam.xlsx')
worksheet = workbook.get_sheet_by_name('Sheet1')

columns=worksheet.columns
rows=worksheet.rows
len_rows=len(rows)
len_columns=len(columns)




for num in range (len_rows):
    #addr_cell = i[num]+str(2);
    addr_cell_read = 'a'+str(num+1);
    addr_cell_write = 'c'+str(num+1);
    val_cell_read = worksheet[addr_cell_read].value;
    fun_changefiles(val_cell_read)
    print('info -->' , 'ip:' ,val_cell_read , ', cell_add:' , addr_cell_read );
    #worksheet[addr_cell_write] = val_cell_read;
    #workbook.save("trial.xls")
print ('\n');
print ('\n');
print ('((( ___thank you for choice this program__)))');
