op=input("ENTER YOUR MYSQL PASSWORD : ")
pas=op
da="ST"
def choice0():
    import mysql.connector as s
    con=s.connect(host="localhost",
                  user="root",
                  password=pas)
    cursor=con.cursor()
    query="create database if not exists ST"
    cursor.execute(query)
    con.commit()
    con.close()
    print("*"*60)
    print("SETUP-1 COMPLETED SUCESSFULLY")
def choice1():
    print("*"*60)
    t=int(input("Enter 1 to Create Student_personal Table\n"
                "\n"
                "Enter 2 to Create Student_professional Table\n"
                "\n"
                "Enter 3 To Create Review Table\n"
                "\n"
                "Enter 4 to Create Time Table\n"
                "\n"
                "Enter 5 to Create Teacher Table\n"
                "\n"
                "Enter 6 to Create Result Table\n"
                "\n"
                "Enter 7 to Create PT-1 Table\n"
                "\n"
                "Enter 8 to Create TERM-1 Table\n"
                "\n"
                "Enter 9 to Create PT-2 Table\n"
                "\n"
                "Enter 10 to Create TERM-2 Table\n"
                "\n"
                "Enter your Choice: "))
    if t==1:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists student_personal(Addm_no int primary key,st_name char(30),class varchar(5),section varchar(20),father_name char(20),mother_name char(20),st_email varchar(30),st_mobileno bigint(11),st_address varchar(40),D_O_B date,password varchar(10) unique key default 1234)"
        cursor.execute(query)
        con.commit()
        con.close()
        print("*"*60)
        print("SETUP-2(A) COMPLETED SUCESSFULLY")
    elif t==2:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists student_professional(Addm_no int,st_Tfees int(10),st_Pfees int(10),foreign key(Addm_no) references student_personal(Addm_no))"
        cursor.execute(query)
        con.commit()
        con.close()
        print("*"*60)
        print("SETUP-2(B) COMPLETED SUCESSFULLY")
    elif t==3:
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database=da)
                    cursor=con.cursor()
                    print("*"*60)
                    query="create table if not exists review(Addm_no int,st_name char(10),review int(1),foreign key(Addm_no) references student_personal(Addm_no))"
                    cursor.execute(query)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("SETUP-2(C) COMPLETED SUCESSFULLY")
    elif t==4:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists time(Addm_no int,login_time datetime,logout_time datetime,foreign key(addm_no) references student_personal(Addm_no))"
        cursor.execute(query)
        con.commit()
        con.close
        print('*'*60)
        print("SETUP-2(D) COMPLETED SUCESSFULLY")
    elif t==5:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists Teacher(Teacher_id int,Teacher_name char(20),Subject char(30),mobile_no bigint,email_id varchar(30),address varchar(30),password varchar(10))"
        cursor.execute(query)
        con.commit()
        con.close
        print('*'*60)
        print("SETUP-2(E) COMPLETED SUCESSFULLY")
    elif t==6:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists result(Addm_no int,st_name char(20),class varchar(10),section varchar(10),st_father char(20),st_mother char(20),d_o_b date,foreign key(addm_no) references student_personal(Addm_no))"
        cursor.execute(query)
        con.commit()
        con.close
        print('*'*60)
        print("SETUP-2(F) COMPLETED SUCESSFULLY")
    elif t==7:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists pti(Addm_no int,class varchar(10),section varchar(10),acc float,eco float,i_p float,phy_edu float,math float,eng float,b_st float,foreign key(addm_no) references student_personal(Addm_no))"
        cursor.execute(query)
        con.commit()
        con.close
        print('*'*60)
        print("SETUP-2(G) COMPLETED SUCESSFULLY")
    elif t==8:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists termi(Addm_no int,class varchar(10),section varchar(10),acci float,ecoi float,i_pi float,phy_edui float,mathi float,engi float,b_sti float,foreign key(addm_no) references student_personal(Addm_no))"
        cursor.execute(query)
        con.commit()
        con.close
        print('*'*60)
        print("SETUP-2(H) COMPLETED SUCESSFULLY")
    elif t==9:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists ptii(Addm_no int,class varchar(10),section varchar(10),acciii float,ecoiii float,i_piii float,phy_eduiii float,mathiii float,engiii float,b_stiii float,foreign key(addm_no) references student_personal(Addm_no))"
        cursor.execute(query)
        con.commit()
        con.close
        print('*'*60)
        print("SETUP-2(I) COMPLETED SUCESSFULLY")
    elif t==10:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*60)
        query="create table if not exists termii(Addm_no int,class varchar(10),section varchar(10),accii float,ecoii float,i_pii float,phy_eduii float,mathii float,engii float,b_stii float,foreign key(addm_no) references student_personal(Addm_no))"
        cursor.execute(query)
        con.commit()
        con.close
        print('*'*60)
        print("SETUP-2(J) COMPLETED SUCESSFULLY")
        
def choice2():
    j=int(input("Enter 1 for see student personal details\n"
                "\n"
                "Enter 2 for see student professional details\n"
                "\n"
                "Enter 3 for see student time_period details\n"
                "\n"
                "Enter 4 for see teachers details\n"
                "\n"
                "Enter 5 for see student result\n"
                "\n"
                "Enter your choice: "))
    if j==1:
        import mysql.connector as s
        import numpy as np
        import pandas as pd
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        n=int(input("Enter add no: "))
        query="select * from student_personal where Addm_no={}".format(n)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            PP=pd.DataFrame(reo,
                  index=['sno1'],
                  columns=['ADDM_NO','NAME','CLASS','SECTION','F_NAME','M_NAME','EMAIL','MOBILE_NO','ADDRESS','D.O.B','PASSWORD'])
            print(PP)
            
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY FIND IT")
    elif j==2:
                    import mysql.connector as s
                    import numpy as np
                    import pandas as pd
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    n=int(input("Enter add no: "))
                    query="select * from student_professional where Addm_no={}".format(n)
                    cursor.execute(query)
                    f=cursor.fetchall()
                    for i in f:
                        reo={(i)}
                        opoo=pd.DataFrame(reo,
                                          index=['sno1'],
                                          columns=['ADDM_NO','TOTAL_FEES','PENDING_FEES'])
                        print(opoo)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY FIND IT")
    elif j==3:
                    import mysql.connector as s
                    import numpy as np
                    import pandas as pd
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    n=int(input("Enter add no: "))
                    query="select * from time where Addm_no={}".format(n)
                    cursor.execute(query)
                    f=cursor.fetchall()
                    for i in f:
                        reo={(i)}
                        opoo=pd.DataFrame(reo,
                                          index=['sno1'],
                                          columns=['ADDM_NO','LOGIN_TIME','LOGOUT_TIME'])
                        print(opoo)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY FIND IT")
    elif j==4:
                    import mysql.connector as s
                    import pandas as pd
                    import numpy as np
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    n=int(input("Enter Teacher ID: "))
                    query="select * from teacher where Teacher_id={} ".format(n)
                    cursor.execute(query)
                    f=cursor.fetchall()
                    for i in f:
                        reo={(i)}
                        PP=pd.DataFrame(reo,
                                        index=['sno1'],
                                        columns=['TEACHER_ID','NAME','SUBJECT','MOBILE NO.','EMAIL-ID','ADDRESS','PASSWORD'])
                        print(PP)
                        
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY FIND IT")
    elif j==5:
                    import mysql.connector as s
                    import numpy as np
                    import pandas as pd
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database="st")
                    cursor=con.cursor()
                    print("*"*30)
                    a=input("Enter student Addm no.: ")
                    print("*"*30)
                    query="select * from result where addm_no={}".format(a)
                    cursor.execute(query)
                    f=cursor.fetchall()
                    for i in f:
                        reo={(i)}
                        pp=pd.DataFrame(reo,
                                        index=['sno'],
                                        columns=['ADDM_NO','NAME','CLASS','SECTION','FATHER_NM','MOTHER_NM','D.O.B'])
                    op="select acc,eco,i_p,phy_edu,math,eng,b_st from termii where addm_no={}".format(a)
                    cursor.execute(op)
                    f=cursor.fetchall()
                    for p in f:
                        reo={(p)}
                        ip=pd.DataFrame(reo,
                                        index=['sno'],
                                        columns=['ACCOUNT','ECONOMICS','I.P','PHY_EDU','MATH','ENGLISH','B.ST'])
                        
                    p=pp.join(ip)
                    print (p)
                    con.commit()
                    con.close()
                    print("*"*60)

        
def choice3():
    pas="aryan@2005"
    o=int(input("Enter 1. for insert into student_personal values\n""\n""Enter 2. for insert into student_professional values\n""\n""Enter 3 for insert into teacher values\n"'\n'"Enter your choice:"))
    if o==1:
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    eno=int(input("Enter student Add_no: "))
                    print("*"*30)
                    ename=input("Enter name Of student: ")
                    print("*"*30)
                    cl=input("Enter a class: ")
                    print("*"*30)
                    se=input("Enter a section: ")
                    print("*"*30)
                    father=input("Enter name Of father: ")
                    print("*"*30)
                    mother=input("Enter name Of mother: ")
                    print("*"*30)
                    em=input("Enter a Email-id: ")
                    print("*"*30)
                    mo=int(input("Enter a mobile.no: "))
                    print("*"*30)
                    ad=input("enter a address: ")
                    print("*"*30)
                    dob=input("Enter D.O.B Of student: ")
                    print("*"*30)
                    pas=input("Enter your password: ")
                    
                    query="insert into student_personal values({},'{}','{}','{}','{}','{}','{}',{},'{}','{}','{}')".format(eno,ename,cl,se,father,mother,em,mo,ad,dob,pas)
                    quer="insert into time(addm_no) value({})".format(eno)
                    cursor.execute(query)
                    cursor.execute(quer)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY ENTERED")
    elif o==2:
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                              user="root",
                              password=pas,
                              database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    e=int(input("Enter a student no: "))
                    print("*"*30)
                    s=int(input("Enter a student Tfees: "))
                    print("*"*30)
                    b=int(input("Enter a student Pfees: "))
                    print("*"*30)
                    query="insert into student_professional values({},{},{})".format(e,s,b)
                    cursor.execute(query)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY ENTERED")
    elif o==3:
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    tid=int(input("Enter Teacher id: "))
                    print("*"*30)
                    tname=input("Enter name Of Teacher: ")
                    print("*"*30)
                    sub=input("Enter name Of Subject: ")
                    print("*"*30)
                    mob=input("Enter Your mobile no.: ")
                    print("*"*30)
                    em=input("Enter a Email-id: ")
                    print("*"*30)
                    add=input("enter a address: ")
                    print("*"*30)
                    pas=input("Enter your password: ")
                    query="insert into teacher values({},'{}','{}',{},'{}','{}','{}')".format(tid,tname,sub,mob,em,add,pas)
                    cursor.execute(query)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY REGISTERED")
def choice4():
    e=int(input("Enter 1 To Update student Name\n"
                "\n"
                "Enter 2 To update student pending fees\n"
                "\n"
                "Enter 3 To Update student phone number\n"
                "\n"
                "Enter 4 to back\n"
                "\n"
                "Enter your choice: "))
    if e==1:
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                              user="root",
                              password=pas,
                              database=da)
                    cursor=con.cursor()
                    print("*"*30)
                   
                    a=input("Enter Updated student Name: ")
                    print("*"*30)
                    b=input("Enter student No: ")
                    query="Update student_personal set st_name='{}' where Addm_no={}".format(a,b)
                    cursor.execute(query)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY UPDATED")
    elif e==2:
                    import mysql.connector as s
                    import numpy as np
                    import pandas as pd
                    con=s.connect(host="localhost",
                              user="root",
                              password=pas,
                              database=da)
                    cursor=con.cursor()
                    print("*"*30)
                   
                    a=input("Enter Updated student Pfees: ")
                    print("*"*30)
                    b=input("Enter add No: ")
                    query="Update student_professional set st_Pfees='{}' where Addm_no={}".format(a,b)
                    cursor.execute(query)
                    print("*"*30)
                    cursor.execute("select * from student_professional")
                    f=cursor.fetchall()
                    for i in f:
                            reo={(i)}
                            PP=pd.DataFrame(reo,
                                        index=['sno1'],
                                        columns=['ADDM_NO','TOTAL_FEES','PENDING_FEES'])
                    print(PP)
            
                    con.commit()
                    con.close()
                    
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY UPDATED")
    elif e==3:
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                              user="root",
                              password=pas,
                              database=da)
                    cursor=con.cursor()
                    print("*"*30)
                   
                    a=int(input("Enter Updated student Phone_no: "))
                    print("*"*30)
                    b=input("Enter student No: ")
                    query="Update student_personal set st_mobileno={} where Addm_no={}".format(a,b)
                    cursor.execute(query)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY UPDATED")
    elif e==4:
                    exit
def choice5():
    b=int(input("Enter 1 To find qarter fees\n"
                "\n"
                "Enter 2 To Find total fees\n"
                "\n"
                "Enter 3 to back\n"
                "\n"
                "Enter Your Choice:"))
    if b==1:
                    import mysql.connector as s
                    import numpy as np
                    import pandas as pd
                    con=s.connect(host="localhost",
                              user="root",
                              password=pas,
                              database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    g=int(input("Enter a quarter number: "))
                    query="select Addm_no,st_Tfees/4*{} as quater from student_professional".format(g)
                    cursor.execute(query)
                    f=cursor.fetchall()
                    for i in f:
                        reo={(i)}
                        PP=pd.DataFrame(reo,
                                        index=['sno1'],
                                        columns=['ADDM_NO','TOTAL_FEES_QUATERLY'])
                        print(PP)
            
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY FIND IT")
    elif b==2:
                    import mysql.connector as s
                    import numpy as np
                    import pandas as pd
                    con=s.connect(host="localhost",
                              user="root",
                              password=pas,
                              database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    f=int(input("Enter a Number Of Month: "))
                    query="select Addm_no ,st_Tfees*{} as annual_Fees from student_professional".format(f)
                    cursor.execute(query)
                    f=cursor.fetchall()
                    for i in f:
                        reo={(i)}
                        PP=pd.DataFrame(reo,
                                        index=['sno1'],
                                        columns=['ADDM_NO','TOTAL_FEES_ANNUALY'])
                        print(PP)
            
                    con.commit()
                    con.close()
                    
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY FIND IT")
    
                    
def choice6():
    h=int(input("Enter 1 for Delete from student_personal\n"
                "\n"
                "Enter 2 for Delete from student_professional\n"
                "\n"
                "Enter 3 for Delete from time\n"
                "\n"
                "Enter 4 to back\n"
                "\n"
                "Enter your choice:"))
    if h==1:
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                                  user="root",
                                  password=pas,
                                  database=da)
                    cursor=con.cursor()
                    print("*"*30)
                    n=int(input("Enter add no: "))
                    query="delete from student_personal where Addm_no={}".format(n)
                    cursor.execute(query)
                    con.commit()
                    con.close()
                    print("*"*60)
                    print("CONGRATULATION SUCESSFULLY DELETE IT")
    elif h==2:
                
                        import mysql.connector as s
                        con=s.connect(host="localhost",
                                      user="root",
                                      password=pas,
                                      database=da)
                        cursor=con.cursor()
                        print("*"*30)
                        n=int(input("Enter add no: "))
                        query="delete from student_professional where Addm_no={}".format(n)
                        cursor.execute(query)
                        con.commit()
                        con.close()
                        print("*"*60)
                        print("CONGRATULATION SUCESSFULLY DELETE IT")
    elif h==3:
                        import mysql.connector as s
                        con=s.connect(host="localhost",
                                      user="root",
                                      password=pas,
                                      database=da)
                        cursor=con.cursor()
                        print("*"*30)
                        n=int(input("Enter add no: "))
                        query="delete from time where Addm_no={}".format(n)
                        cursor.execute(query)
                        con.commit()
                        con.close()
                        print("*"*60)
                        print("CONGRATULATION SUCESSFULLY DELETE IT")
    
def choice7():
    j=int(input("Enter 1 for see personal detail\n"
                "\n"
                "Enter 2 for see professional details\n"
                "\n"
                "Enter 3 to back\n"
                "\n"
                "Enter your choice:"))
    if j==1:
        import mysql.connector as s
        import pandas as pd
        import numpy as np
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        n=input("Enter student password: ")
        query="select * from student_personal where password='{}' ".format(n)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            PP=pd.DataFrame(reo,
                            index=['sno1'],
                            columns=['ADDM_NO','NAME','FATHER NAME','MOTHER NAME','EMAIL','MOBILE_NO','ADDRESS','D.O.B','PASSWORD'])
            print(PP)
            
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY FIND IT")
    elif j==2:
        import mysql.connector as s
        import pandas as pd
        import numpy as np
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        n=int(input("Enter student add_no: "))
        query="select * from student_professional where Addm_no={} ".format(n)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            PP=pd.DataFrame(reo,
                            index=['sno1'],
                            columns=['ADDM_NO','TOTAL_FEES','PENDING_FEES'])
            print(PP)
            
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY FIND IT")
   
    
def choice8():
    e=int(input("Enter 1 To Update Mobile Number\n""\n""Enter 2 To Update Email-ID\n""\n""Enter 3 To Update Password\n""\n""Enter your choice: "))
    if e==1:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter Updated mobile no: ")
        print("*"*30)
        b=input("Enter your password: ")
        query="Update student_personal set st_mobileno={} where password='{}'".format(a,b)
        cursor.execute(query)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY UPDATED")
    elif e==2:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter Updated email-id: ")
        print("*"*30)
        b=input("Enter your password: ")
        query="Update student_personal set st_email='{}' where password='{}'".format(a,b)
        cursor.execute(query)
        print("*"*30)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY UPDATED")
    elif e==3:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter Updated password: ")
        print("REMEMBER YOUR PASSWORD")
        print("*"*30)
        b=input("Enter Old Password No: ")
        query="Update student_personal set password='{}' where password='{}'".format(a,b)
        cursor.execute(query)
        print("*"*30)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY UPDATED")
def choice9():
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        n=input("Enter add_no no: ")
        p=input("Enter Your password: ")
        query="delete from time where addm_no={}".format(n)
        query2="delete from student_professional where addm_no ={}".format(n)
        query3="delete from student_personal where password='{}'".format(p)
        cursor.execute(query)
        cursor.execute(query2)
        cursor.execute(query3)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY DELETE IT")

def choice10():
    import mysql.connector as s
    con=s.connect(host="localhost",
                  user="root",
                  password=pas,
                  database=da)
    cursor=con.cursor()
    print("*"*30)
    p=int(input("Enter your ID: "))
    n=input("Enter a Name: ")
    r=int(input("Enter a Rating From 5 star"))
    query="insert into review values({},'{}',{})".format (p,n,r)
    cursor.execute(query)
    con.commit()
    con.close()
    print("*"*60)
    print("THANK YOU FOR GIVING RATING")

def choice12():
    pas="aryan@2005"
    import mysql.connector as s
    con=s.connect(host="localhost",
                  user="root",
                  password=pas,
                  database=da)
    cursor=con.cursor()
    print("*"*30)
    eno=int(input("Enter student Add_no: "))
    print("*"*30)
    ename=input("Enter name Of student: ")
    print("*"*30)
    clas=input("Enter Class Of student: ")
    print("*"*30)
    sec=input("Enter Section Of student: ")
    print("*"*30)
    father=input("Enter name Of father: ")
    print("*"*30)
    mother=input("Enter name Of mother: ")
    print("*"*30)
    em=input("Enter a Email-id: ")
    print("*"*30)
    mo=int(input("Enter a mobile.no: "))
    print("*"*30)
    ad=input("enter a address: ")
    print("*"*30)
    dob=input("Enter D.o.B of Student: ")
    print("*"*30)
    pas=input("Enter your password: ")
    query="insert into student_personal values({},'{}','{}','{}','{}','{}','{}',{},'{}','{}','{}')".format(eno,ename,clas,sec,father,mother,em,mo,ad,dob,pas)
    quer="insert into time(addm_no) value({})".format(eno)
    cursor.execute(query)
    cursor.execute(quer)
    con.commit()
    con.close()
    print("*"*60)
    print("CONGRATULATION SUCESSFULLY ENTERED")

def choice13():
    pas="aryan@2005"
    import mysql.connector as s
    con=s.connect(host="localhost",
                  user="root",
                  password=pas,
                  database=da)
    cursor=con.cursor()
    print("*"*30)
    tid=int(input("Enter Teacher id: "))
    print("*"*30)
    tname=input("Enter name Of Teacher: ")
    print("*"*30)
    sub=input("Enter name Of Subject: ")
    print("*"*30)
    mob=input("Enter Your mobile no.: ")
    print("*"*30)
    em=input("Enter a Email-id: ")
    print("*"*30)
    add=input("enter a address: ")
    print("*"*30)
    pas=input("Enter your password: ")
    query="insert into teacher values({},'{}','{}',{},'{}','{}','{}')".format(tid,tname,sub,mob,em,add,pas)
    cursor.execute(query)
    con.commit()
    con.close()
    print("*"*60)
    print("CONGRATULATION SUCESSFULLY REGISTERED")
def choice14():
        import mysql.connector as s
        import pandas as pd
        import numpy as np
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        n=int(input("Enter Teacher ID: "))
        query="select * from teacher where Teacher_id={} ".format(n)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            PP=pd.DataFrame(reo,
                            index=['sno1'],
                            columns=['TEACHER_ID','NAME','SUBJECT','MOBILE NO.','EMAIL-ID','ADDRESS','PASSWORD'])
            print(PP)
            
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY FIND IT")
def choice15():
    o=int(input("Enter 1 To Update Mobile no.\n"
                 "\n"
                 "Enter 2 To Update Email-id\n"
                 "\n"
                 "Enter your choice: "))
                 
    if o==1:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter Updated Mobile No.: ")
        print("*"*30)
        b=input("Enter your ID: ")
        query="Update Teacher set mobile_no={} where Teacher_id={}".format(a,b)
        cursor.execute(query)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY UPDATED")

    elif o==2:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter Updated Email-Id: ")
        print("*"*30)
        b=input("Enter your ID: ")
        query="Update Teacher set email_id='{}' where Teacher_id={}".format(a,b)
        cursor.execute(query)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY UPDATED")
def choice16():
     o=int(input("Enter 1 for insert Deatils into Result\n"
                 "\n"
                 "Enter 2. for insert Details into PT-1\n"
                 "\n"
                 "Enter 3. for insert Details into TERM-1\n"
                 "\n"
                 "Enter 4. for insert Details into PT-2\n"
                 "\n"
                 "Enter 5. for insert Details into TERM-2\n"
                 "\n"
                 "Enter your choice:"))
     if o==1:
         import mysql.connector as s
         con=s.connect(host="localhost",
                       user="root",
                       password=pas,
                       database=da)
         cursor=con.cursor()
         print("*"*30)
         eno=int(input("Enter student Add_no: "))
         print("*"*30)
         ename=input("Enter name Of student: ")
         print("*"*30)
         cl=input("Enter Class: ")
         print("*"*30)
         sec=input("Enter Section: ")
         print("*"*30)
         stf=input("Enter a Student father name: ")
         print("*"*30)
         stm=input("Enter a Student Mother name: ")
         print("*"*30)
         dob=input("Enter a Student D.O.B: ")
         query="insert into result values({},'{}','{}','{}','{}','{}','{}')".format(eno,ename,cl,sec,stf,stm,dob)
         cursor.execute(query)
         con.commit()
         con.close()
         print("*"*60)
         print("CONGRATULATION SUCESSFULLY ENTERED")
     elif o==2:
         import mysql.connector as s
         con=s.connect(host="localhost",
                       user="root",
                       password=pas,
                       database=da)
         cursor=con.cursor()
         print("*"*30)
         eno=int(input("Enter student Add_no: "))
         print("*"*30)
         cl=input("Enter Class: ")
         print("*"*30)
         sec=input("Enter Section: ")
         print("*"*30)
         acc=input("Enter a Student Accounts Marks: ")
         print("*"*30)
         eco=input("Enter a Student Economics Marks: ")
         print("*"*30)
         ip=input("Enter a Student I.P Marks: ")
         print("*"*30)
         phy=input("Enter a Student Phy. Education Marks: ")
         print("*"*30)
         math=input("Enter a Student Math Marks: ")
         print("*"*30)
         eng=input("Enter a Student English Marks: ")
         print("*"*30)
         bst=input("Enter a Student B.ST Marks: ")
         query="insert into pti values({},'{}','{}',{},{},{},{},{},{},{})".format(eno,cl,sec,acc,eco,ip,phy,math,eng,bst)
         cursor.execute(query)
         con.commit()
         con.close()
         print("*"*60)
         print("CONGRATULATION SUCESSFULLY ENTERED")

     elif o==3:
        import mysql.connector as s
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database=da)
        cursor=con.cursor()
        print("*"*30)
        eno=int(input("Enter student Add_no: "))
        print("*"*30)
        cl=input("Enter Class: ")
        print("*"*30)
        sec=input("Enter Section: ")
        print("*"*30)
        acc=input("Enter a Student Accounts Marks: ")
        print("*"*30)
        eco=input("Enter a Student Economics Marks: ")
        print("*"*30)
        ip=input("Enter a Student I.P Marks: ")
        print("*"*30)
        phy=input("Enter a Student Phy. Education Marks: ")
        print("*"*30)
        math=input("Enter a Student Math Marks: ")
        print("*"*30)
        eng=input("Enter a Student English Marks: ")
        print("*"*30)
        bst=input("Enter a Student B.ST Marks: ")
        query="insert into termi values({},'{}','{}',{},{},{},{},{},{},{})".format(eno,cl,sec,acc,eco,ip,phy,math,eng,bst)
        cursor.execute(query)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY ENTERED")
     elif o==4:
         import mysql.connector as s
         con=s.connect(host="localhost",
                       user="root",
                       password=pas,
                       database=da)
         cursor=con.cursor()
         print("*"*30)
         eno=int(input("Enter student Add_no: "))
         print("*"*30)
         cl=input("Enter Class: ")
         print("*"*30)
         sec=input("Enter Section: ")
         print("*"*30)
         acc=input("Enter a Student Accounts Marks: ")
         print("*"*30)
         eco=input("Enter a Student Economics Marks: ")
         print("*"*30)
         ip=input("Enter a Student I.P Marks: ")
         print("*"*30)
         phy=input("Enter a Student Phy. Education Marks: ")
         print("*"*30)
         math=input("Enter a Student Math Marks: ")
         print("*"*30)
         eng=input("Enter a Student English Marks: ")
         print("*"*30)
         bst=input("Enter a Student B.ST Marks: ")
         query="insert into ptii values({},'{}','{}',{},{},{},{},{},{},{})".format(eno,cl,sec,acc,eco,ip,phy,math,eng,bst)
         cursor.execute(query)
         con.commit()
         con.close()
         print("*"*60)
         print("CONGRATULATION SUCESSFULLY ENTERED")
     elif o==5:
         import mysql.connector as s
         con=s.connect(host="localhost",
                       user="root",
                       password=pas,
                       database=da)
         cursor=con.cursor()
         print("*"*30)
         eno=int(input("Enter student Add_no: "))
         print("*"*30)
         cl=input("Enter Class: ")
         print("*"*30)
         sec=input("Enter Section: ")
         print("*"*30)
         acc=input("Enter a Student Accounts Marks: ")
         print("*"*30)
         eco=input("Enter a Student Economics Marks: ")
         print("*"*30)
         ip=input("Enter a Student I.P Marks: ")
         print("*"*30)
         phy=input("Enter a Student Phy. Education Marks: ")
         print("*"*30)
         math=input("Enter a Student Math Marks: ")
         print("*"*30)
         eng=input("Enter a Student English Marks: ")
         print("*"*30)
         bst=input("Enter a Student B.ST Marks: ")
         query="insert into termii values({},'{}','{}',{},{},{},{},{},{},{})".format(eno,cl,sec,acc,eco,ip,phy,math,eng,bst)
         cursor.execute(query)
         con.commit()
         con.close()
         print("*"*60)
         print("CONGRATULATION SUCESSFULLY ENTERED")
def choice17():
    o=int(input("Enter 1 to see student personal details\n"
                "\n"
                "Enter 2 to see student PT-1 Marksheet\n"
                "\n"
                "Enter 3 to see student Term-1 Marsheet\n"
                "\n"
                "Enter 4 to see student PT-2 Marksheet\n"
                "\n"
                "Enter 5 to see student Term-2 Marksheet\n"
                "\n"
                "Enter your choice: "))
    if o==1:
        import mysql.connector as s
        import numpy as np
        import pandas as pd
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database="st")
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter student Addm no.: ")
        print("*"*30)
        query="select * from result where addm_no={}".format(a)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            pp=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ADDM_NO','NAME','CLASS','SECTION','FATHER_NM','MOTHER_NM','D.O.B'])

            print(pp)
        con.commit()
        con.close()
        print("*"*60)
        print("CONGRATULATION SUCESSFULLY UPDATED")


    elif o==2:
        import mysql.connector as s
        import numpy as np
        import pandas as pd
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database="st")
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter student Addm no.: ")
        print("*"*30)
        query="select * from result where addm_no={}".format(a)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            pp=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ADDM_NO','NAME','CLASS','SECTION','FATHER_NM','MOTHER_NM','D.O.B'])
        op="select acc,eco,i_p,phy_edu,math,eng,b_st from pti where addm_no={}".format(a)
        cursor.execute(op)
        f=cursor.fetchall()
        for p in f:
            reo={(p)}
            ip=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ACCOUNT','ECONOMICS','I.P','PHY_EDU','MATH','ENGLISH','B.ST'])
            
        p=pp.join(ip)
        print (p)
        con.commit()
        con.close()
        print("*"*60)
    elif o==3:
        import mysql.connector as s
        import numpy as np
        import pandas as pd
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database="st")
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter student Addm no.: ")
        print("*"*30)
        query="select * from result where addm_no={}".format(a)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            pp=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ADDM_NO','NAME','CLASS','SECTION','FATHER_NM','MOTHER_NM','D.O.B'])
        op="select acc,eco,i_p,phy_edu,math,eng,b_st from termi where addm_no={}".format(a)
        cursor.execute(op)
        f=cursor.fetchall()
        for p in f:
            reo={(p)}
            ip=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ACCOUNT','ECONOMICS','I.P','PHY_EDU','MATH','ENGLISH','B.ST'])
            
        p=pp.join(ip)
        print (p)
        con.commit()
        con.close()
        print("*"*60)
    elif o==4:
        import mysql.connector as s
        import numpy as np
        import pandas as pd
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database="st")
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter student Addm no.: ")
        print("*"*30)
        query="select * from result where addm_no={}".format(a)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            pp=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ADDM_NO','NAME','CLASS','SECTION','FATHER_NM','MOTHER_NM','D.O.B'])
        op="select acc,eco,i_p,phy_edu,math,eng,b_st from ptii where addm_no={}".format(a)
        cursor.execute(op)
        f=cursor.fetchall()
        for p in f:
            reo={(p)}
            ip=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ACCOUNT','ECONOMICS','I.P','PHY_EDU','MATH','ENGLISH','B.ST'])
            
        p=pp.join(ip)
        print (p)
        con.commit()
        con.close()
        print("*"*60)
    elif o==5:
        import mysql.connector as s
        import numpy as np
        import pandas as pd
        con=s.connect(host="localhost",
                      user="root",
                      password=pas,
                      database="st")
        cursor=con.cursor()
        print("*"*30)
        a=input("Enter student Addm no.: ")
        print("*"*30)
        query="select * from result where addm_no={}".format(a)
        cursor.execute(query)
        f=cursor.fetchall()
        for i in f:
            reo={(i)}
            pp=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ADDM_NO','NAME','CLASS','SECTION','FATHER_NM','MOTHER_NM','D.O.B'])
        op="select acc,eco,i_p,phy_edu,math,eng,b_st from termii where addm_no={}".format(a)
        cursor.execute(op)
        f=cursor.fetchall()
        for p in f:
            reo={(p)}
            ip=pd.DataFrame(reo,
                            index=['sno'],
                            columns=['ACCOUNT','ECONOMICS','I.P','PHY_EDU','MATH','ENGLISH','B.ST'])
            
        p=pp.join(ip)
        print (p)
        con.commit()
        con.close()
        print("*"*60)



def choice18():
    import mysql.connector as s
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    con=s.connect(host="localhost",
                  user="root",
                  password=pas,
                  database="st")
    cursor=con.cursor()
    print("*"*30)
    a=input("Enter student Addm no.: ")
    print("*"*30)
    query="select acc,eco,i_p,phy_edu,math,eng,b_st from pti where addm_no={}".format(a)
    cursor.execute(query)
    f=cursor.fetchall()
    for i in f:
        reo=(i)

    op1="select acci,ecoi,i_pi,phy_edui,mathi,engi,b_sti from termi where  addm_no={}".format(a)
    cursor.execute(op1)
    f=cursor.fetchall()
    for p in f:
        re=(p)

    op2="select acciii,ecoiii,i_piii,phy_eduiii,mathiii,engiii,b_stiii from ptii where  addm_no={}".format(a)
    cursor.execute(op2)
    f=cursor.fetchall()
    for l in f:
        ro=(l)
          
    op3="select accii,ecoii,i_pii,phy_eduii,mathii,engii,b_stii from termii where  addm_no={}".format(a)
    cursor.execute(op3)
    f=cursor.fetchall()
    for k in f:
        eo=(k)
          
    print("*"*60)
    figure,axis=plt.subplots(2,2)
    x=(reo)
    b=['ACCOUNTANCY','ECONOMICS','I.P','PHY.EDU.','MATHS','ENGLISH','B.ST']
    axis[0,0].plot(b,x)
    axis[0,0].set_title("PT-1")

    xi=(re)
    axis[0,1].plot(b,xi)
    axis[0,1].set_title("TERM-1")

    xii=(ro)
    axis[1,0].plot(b,xii)
    axis[1,0].set_title("PT-2")

    xiii=(eo)
    axis[1,1].plot(b,xiii)
    axis[1,1].set_title("TERM-2")
    plt.show()
    m={
        'pt1':pd.Series(x),
        'term1':pd.Series(xi),
        'pt2':pd.Series(xii),
        'term2':pd.Series(xiii) }
    o=pd.DataFrame(m,index=['ACCOUNT','ECONOMICS','I.P','PHY_EDU','MATH','ENGLISH','B.ST'])
    n=pd.DataFrame(m)
    sub=('ACCOUNT','ECONOMICS','I.P','PHY_EDU','MATH','ENGLISH','B.ST')
    ss=np.arange(len(sub))
    n.plot.bar(ss,width=0.8)    
    print(o)
    plt.show()



    
    
    

print("*"*100)

print("_________________________________________________________________________")

import time
while True:
    print("*"*100)
    print("_"*60)
    p=int(input("Enter 1. for Login as SCHOOL MANAGEMENT\n"
                "Enter 2. for Login as STUDENT\n"
                "Enter 3. for Exit\n"
                "Enter your Choice: "))
    print("_"*60)
    print("*"*60)
    if p==1:
        print("*"*30)
        b=int(input("Enter 1 to Login as School Management\n"
                    "\n"
                    "Enter 2 to Login as Teacher\n"
                    "\n"
                    "Enter Your Choice: "))

        if b==1:
            user=input("Enter Your User ID: ")
            print("*"*30)
            passwd=input("Enter Your User Password: ")
            if user=='2005' and passwd=='2005':
                while True:
                    print("*"*60)
                    print("_"*60)
                    print("*****WELCOME TO STUDENT MANAGEMENT*****")
                    print("-"*60)
                    print("*"*60)
                    choice=int(input("Enter 0 To Do Setup-1\n"
                                     "\n"
                                     "Enter 1 To Do Setup-2\n"
                                     "\n"
                                     "Enter 2 To See Details\n"
                                     "\n"
                                     "Enter 3 To Insert Details\n"
                                     "\n"
                                     "Enter 4 To Update Details\n"
                                     "\n"
                                     "ENTER 5 TO Find Fees\n"
                                     "\n"
                                     "Enter 6 To Delete Details\n"
                                     "\n"
                                     "Enter 7 TO Back\n"
                                     "\n"
                                     "Enter Your Choice: "))
                    if choice==0:
                        choice0()
                    elif choice==1:
                        choice1()
                    elif choice==2:
                        choice2()
                    elif choice==3:
                        choice3()
                    elif choice==4:
                        choice4()
                    elif choice==5:
                        choice5()
                    elif choice==6:
                        choice6()
                    elif choice==7:
                        break
                    else:
                        print("Enter correct Choice")

        elif b==2:
            while True:
                print("_"*60)
                j=int(input("ENTER 1 TO LOG IN\n"
                            "\n"
                            "ENTER 2 TO CREATE ACCOUNT\n"
                            "\n"
                            "ENTER 3 to GO BACK\n"
                            "\n"
                            "ENTER YOUR CHOICE: "))
                print("_"*60)
                
                if j==1:
                    print("_"*60)
                    user=input("ENTER YOUR USER ID: ")
                    print("_"*60)
                    passwd=input("ENTER A PASSWORD: ")
                    print("_"*60)
                    import mysql.connector as s
                    con=s.connect(host="localhost",
                                 user="root",
                                 password=pas,
                               database=da)
                    cursor=con.cursor()
                    pswd="select password from teacher where email_id='{}'".format(user)
                    cursor.execute(pswd)
                    f=cursor.fetchone()
                    for i in f:
                        if i==passwd:
                            import random
                            import smtplib
                            from email.message import EmailMessage

                            number="0123456789"
                            string=number
                            length=6
                            otp="".join(random.sample(string,length))
                            
                            def email_alert(subject,body,to):
                                msg = EmailMessage()

                                msg.set_content(body)

                                msg['subject']=subject

                                msg['to']=to

                                user = "pythonsql878@gmail.com"

                                msg['from']=user

                                password= "ntsussuacrtcyvod"

                                server =smtplib.SMTP("smtp.gmail.com",587)

                                server.starttls()

                                server.login(user,password)

                                server.send_message(msg)


                                server.quit()


                            if __name__=='__main__':
                        
                                email_alert("YOUR LOGIN OTP","Your Login OTP For a Teacher of Student Management. So, Your OTP is-"+otp,user)
                            
                            oreo=input("enter your OTP: ")
                            if otp==oreo:
                                print("YOU HAD SUCCESSFULLY LOGIN")
                                while True:
                                    print("*"*60)
                                    print("_"*60)
                                    print("***** WELCOME TO SCHOOL MANAGEMENT *****")
                                    print("_"*60)
                                    print("*"*60)

                                    d=int(input("Enter 1 To see your Details\n"
                                                "\n"
                                                "Enter 2 To Update your Details\n"
                                                "\n"
                                                "Enter 3 To Enter Student Result Details\n"
                                                "\n"
                                                "Enter 4 To See Student Result\n"
                                                "\n"
                                                "Enter 5 to See Student Performance\n"
                                                "\n"
                                                "Enter Your Choice: "))
                                    if d==1:
                                        choice14()
                                    elif d==2:
                                        choice15()
                                    elif d==3:
                                        choice16()
                                    elif d==4:
                                        choice17()
                                    elif d==5:
                                        choice18()
                                            
                    
                                
                elif j==2:
                    choice13()                
            
    elif p==2:
        while True:
            print("_"*60)
            j=int(input("ENTER 1 TO LOG IN\n"
                        "\n"
                        "ENTER 2 TO CREATE ACOOUNT\n"
                        "\n"
                        "ENTER 3 to GO BACK\n"
                        "\n"
                        "ENTER YOUR CHOICE: "))
            print("_"*60)
            if j==1:
                print("_"*60)
                user=input("ENTER YOUR USER ID: ")
                print("_"*60)
                passwd=input("ENTER A PASSWORD: ")
                print("_"*60)
                import mysql.connector as s
                con=s.connect(host="localhost",
                             user="root",
                             password=pas,
                           database=da)
                cursor=con.cursor()
                pswd="select password from student_personal where st_email='{}'".format(user)
                cursor.execute(pswd)
                f=cursor.fetchone()
                for i in f:
                    if i==passwd:
                        import random
                        import smtplib
                        from email.message import EmailMessage

                        number="0123456789"
                        string=number
                        length=6
                        otp="".join(random.sample(string,length))
                        
                        def email_alert(subject,body,to):
                            msg = EmailMessage()

                            msg.set_content(body)

                            msg['subject']=subject

                            msg['to']=to

                            user = "pythonsql878@gmail.com"

                            msg['from']=user

                            password= "ntsussuacrtcyvod"

                            server =smtplib.SMTP("smtp.gmail.com",587)

                            server.starttls()

                            server.login(user,password)

                            server.send_message(msg)


                            server.quit()


                        if __name__=='__main__':
                    
                            email_alert("YOUR LOGIN OTP","Your Login OTP For A Student Management. So, Your OTP is-"+otp,user)
                        
                        oreo=input("enter your OTP: ")
                        if otp==oreo:
                            print("YOU HAD SUCCESSFULLY LOGIN")
                            
                            print("*"*60)
                            am=input("Please Enter your add_no: ")
                            op=am
                            import mysql.connector as s
                            con=s.connect(host="localhost",
                                           user="root",
                                           password=pas,
                                           database=da)
                            cursor=con.cursor()
                            query="update time set login_time=now() where addm_no={}".format(op)
                            cursor.execute(query)
                            f=cursor.fetchall()
                            for i in f:
                                print(i)
                            con.commit()
                            con.close()
                            while True:
                                print("*"*60)
                                print("_"*60)
                                print("***** WELCOME TO SCHOOL MANAGEMENT *****")
                                print("_"*60)
                                print("*"*60)
                                print("Enter 1 To see your Details")
                                print("")
                                print("Enter 2 To Update Your Details")
                                print("")
                                print("Enter 3 To Delete your account")
                                print("")
                                print("Enter 4 TO Give review")
                                print("")
                                print("Enter 5 TO See Marksheet")
                                print("")
                                print("Enter 6 TO View Marksheet in Graph")
                                print("")
                                print("Enter 7 TO Exit")
                                print("*"*30)
                                choice=int(input("Enter Your Choice: "))
                                print("*"*30)
                                if choice==1:
                                    choice7()
                                elif choice==2:
                                    choice8()
                                elif choice==3:
                                    choice9()
                                elif choice==4:
                                    choice10()
                                elif choice==5:
                                    choice17()
                                elif choice==6:
                                    choice18()
                                elif choice==7:
                                    print("*"*60)
                                    import mysql.connector as s
                                    con=s.connect(host="localhost",
                                                  user="root",
                                                  password=pas,
                                                  database=da)
                                    cursor=con.cursor()
                                    query="update time set logout_time=now() where addm_no={}".format(op)
                                    cursor.execute(query)
                                    f=cursor.fetchall()
                                    for i in f:
                                        print(i)
                                    con.commit()
                                    con.close()
                                    
                                    break
                                else:
                                    print("Enter correct Choice")
            elif j==2:
                choice12()                        
            elif j==3 :
                    break
    elif p==3:
            break
