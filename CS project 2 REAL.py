import mysql.connector as my
mycon=my.connect(host='localhost',
                 user='root',
                 passwd='21122007',
                 database='InventoryBillingMS')


def ADD_PRODUCT():
    P_Id=int(input("Enter the Id of The Product : "))
    P_Name=input("Enter the Name of the Product : ")
    P_Price=input("Enter the Price of the Product : ")
    P_Quantity=input("Enter the number of Products Available : ")
    R1=[P_Id , P_Name , P_Price , P_Quantity]
    Sql1='insert into products values(%s,%s,%s,%s);'
    cur=mycon.cursor()
    cur.execute(Sql1,R1)
    mycon.commit()
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<><><><><><><><><><><><><><><><><>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("____________________________________________________________________Data Entered Succesfully!____________________________________________________________")
    main()

def VIEW_INVENTORY():
    Sql2='SELECT * from products;'
    cur=mycon.cursor()
    cur.execute(Sql2)
    Result=cur.fetchall()
    for i in Result:
        try:
            print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
            print("| Product ID : " , i[0]                 )
            print("| Product Name : ", i[1]                )
            print("| Price : " , i[2]                      )
            print("| Quantity : " ,i[3]                    )
            print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
            
        except EOFError:
            break
    main()
    
    



def SEARCH_PRODUCT():
    P_Id=int(input("Enter the Id of the Product :"))
    cur=mycon.cursor()
    cur.execute('Select product_id from products;')
    data=cur.fetchall()
    p_ids=[]
    for i in data:
        p_ids.append(i[0])
   
        
    if P_Id in p_ids:
        Sql3='SELECT * from products WHERE product_id=%s;'
        cur.execute(Sql3 , [P_Id])
        product=cur.fetchone()
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<><><><><><><><><><><><><><><><><>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("____________________________________________________________________Data Searched Succesfully!____________________________________________________________")
        
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
        print("| Product ID : " , product[0]           )
        print("| Product Name : ", product[1]          )
        print("| Price : " , product[2]                )
        print("| Quantity : " ,product[3]              )
        print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
            
        

    else:
        print("___________________________________________________________________________SORRY!_________________________________________________________________________")
        print("______________________________________________________________________Product Not Found!__________________________________________________________________")
    
    main()

def update_quantity():
    P_Id=int(input(" Enter the Id of the Product : "))
    New_quantity=int(input(" Enter the Quantity to be updated : "))
    sql1='UPDATE products set product_quantity = %s WHERE product_id= %s;'
    r1=[New_quantity , P_Id]
    cur=mycon.cursor()
    cur.execute(sql1 , r1)
    mycon.commit()
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<><><><><><><><><><><><><><><><><>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("____________________________________________________________________Data Updated Succesfully!____________________________________________________________")
    UPDATE_PRODUCT()

def update_price():
    P_Id=int(input(" Enter the Id of the Product : "))
    New_price=int(input(" Enter the Price to be updated : "))
    sql2='UPDATE products set product_price = %s WHERE product_id= %s;'
    r2=[New_price , P_Id]
    cur=mycon.cursor()
    cur.execute(sql2 , r2)
    mycon.commit()
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<><><><><><><><><><><><><><><><><>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("____________________________________________________________________Data Updated Succesfully!____________________________________________________________")
    UPDATE_PRODUCT()

def update_name():
    P_Id=int(input(" Enter the Id of the Product : "))
    New_name=input(" Enter the Name to be updated : ")
    sql3='UPDATE products set product_name = %s WHERE product_id= %s;'
    r3=[New_name , P_Id]
    cur=mycon.cursor()
    cur.execute(sql3 , r3)
    mycon.commit()
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<><><><><><><><><><><><><><><><><>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("____________________________________________________________________Data Updated Succesfully!____________________________________________________________")
    UPDATE_PRODUCT()
    
    

def UPDATE_PRODUCT():
    print(''' _=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_ UPDATE MENU _=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_



   ---> 1. Update Quantity                                           
   ---> 2. Update Price
   ---> 3. Update Name
   ---> 4. Return to Home

 ''')


    Choose=int(input("Enter Your Choice : "))
    print("|==============================================================<><><><><><><><><><><><><><><><><>=======================================================|")

    if Choose==1:
        update_quantity()
    if Choose==2:
        update_price()
    if Choose==3:
        update_name()
    if Choose==4:
        main()

    else:
        print("SORRY ! , Choice Not Available..." )
        print(" Please Try Again" )
        UPDATE_PRODUCT()

    main()
    



def DELETE_PRODUCT():
    cur = mycon.cursor()
    P_id = int(input("Enter the ID of the Product to delete from the bill: "))
    P_Id=int(input("Enter the Id of the Product to delete from : "))
    cur.execute('Select product_id from products;')
    data=cur.fetchall()
    p_ids=[]
    for i in data:
        p_ids.append(i[0])
        
    
    if P_Id in p_ids:
        
        sql_delete = 'DELETE FROM bill_items WHERE product_id = {};'.format(P_id)
        cur.execute(sql_delete)
        Sql4='DELETE from products WHERE product_id={}'.format(P_Id)
        cur.execute(Sql4)
        mycon.commit()
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<><><><><><><><><><><><><><><><><>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("____________________________________________________________________Data Deleted Succesfully!____________________________________________________________")
            
        
    else:
        print("___________________________________________________________________________SORRY!_________________________________________________________________________")
        print("______________________________________________________________________Product Not Found!__________________________________________________________________")
         
         
         
    main()

def GENERATE_BILL():
    C_name=input("Enter The name of the customer : ")
    Total=0
    Products=[]
    while True:
        P_Id=int(input("Enter The id of the Product to be purchased (or enter -1 to finish puchasing) : "))
        R5=[P_Id]
        if P_Id == -1:
            break
        S_Quantity=int(input("Enter the Quantity to be purchased : "))
        Sql5 = 'SELECT product_name, product_price, product_quantity FROM products WHERE product_id = %s;'
        cur=mycon.cursor()
        cur.execute(Sql5, [P_Id,])
        P = cur.fetchone()

        if P:
            P_Name, P_Price, P_Quantity = P  
            if P_Quantity >= S_Quantity:
                Total += P_Price * S_Quantity
                Products.append([P_Id, S_Quantity, P_Price])
            else:
                print("Sorry Product Quantity not Avialable ")

        else:
            print("Product Does not Exist")

    if not P:
        print("NO PRODUCTS SELECTED!")
        print("____________________________________________________________________Bill Not Genarated!____________________________________________________________")

    Sql6='INSERT INTO bills (customer_name, bill_date , total_bill) VALUES(%s , CURDATE(), %s);'
    R6=[C_name , Total]
    cur.execute(Sql6,R6)

    Bill_id = cur.lastrowid


    for P_Id , P_Quantity , P_Price in Products:
        R7=[Bill_id, P_Id, P_Quantity, P_Price]
        Sql7='INSERT INTO bill_items (bill_id, product_id, product_quantity, product_price) VALUES (%s, %s, %s, %s);'
        cur.execute(Sql7, R7)
        R8=[P_Quantity ,P_Id]
        Sql8='UPDATE products SET product_quantity= product_quantity - %s WHERE product_id = %s;'
        cur.execute(Sql8 , R8)


    mycon.commit()
    print("Bill generated successfully! Total amount: {} Rs.".format(Total))


    main()





def main():    
    print(''' _=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_ INVENTORY AND BILLING MANAGEMENT SYSTEM _=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_



   ---> 1. Add A Product                                            
   ---> 2. View Inventory
   ---> 3. Search A Product
   ---> 4. Update A Product                                         
   ---> 5. Delete A Product                                       
   ---> 6. Generate Bill                                         
   ---> 7. EXIT PROGRAM
 ''')

    Choose=int(input("Enter Your Choice : "))
    print("|==============================================================<><><><><><><><><><><><><><><><><>=======================================================|")

    if Choose==1:
        ADD_PRODUCT()
    if Choose==2:
        VIEW_INVENTORY()
    if Choose==3:
        SEARCH_PRODUCT()
    if Choose==4:
        UPDATE_PRODUCT()
    if Choose==5:
        DELETE_PRODUCT()
    if Choose==6:
        GENERATE_BILL()
    if Choose==7:
        print("|==============================================================<><><><><><><><><><><><><><><><><>=======================================================|")
        print(''' __________________________________________THANK YOU!_____________________________________________________SEE YOU AGAIN!______________________________''')
        
    else:
        print("SORRY ! , Choice Not Available..." )
        print(" Please Try Again" )
        main()
main()



    
        

    
                       
        
    

   
