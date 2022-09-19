#**************************hotel management*********************************
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="string1234",
    database="hotel_management"
)
mycursor=mydb.cursor()
#*****************************************************************************************
class hotel:
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',cindate='',coutdate='',rno=1):
        print("****************WELCOME TO GANGA HOTEL************************")
        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno

#********customer details******************************
    def details (self):
        self.name=input(f"Enter your name:{self.name}")
        self.address=input(f"Enter your address:{self.address}")
        self.cindate=input(f"Enter your check in date:{self.cindate}")
        self.coutdate=input(f"Enter your check out date:{self.coutdate}")
        print(f"your room no:{self.rno}")
        sql="insert into customer_details(name,address,cindate,coutdate,room_no)values(%s,%s,%s,%s,%s)"
        val=(self.name,self.address,self.cindate,self.coutdate,self.rno)
        mycursor.execute(sql,val)
        mydb.commit()
#************room type*******************

    def roomrent(self):
        print("choose your room based on your budget")
        print("1.Standard Non AC")
        print("2.Standard AC")
        print("3.3 Bed Non AC")
        print("4.3 Bed AC")
        x=int(input("Enter your roomtype:"))
        n=int(input("For How Many Nights Did You Stay:"))
        if(x==1):
            print ("Room Type- Standard Non-AC")
            self.s=4000*n
        elif (x==2):
            print ("Room Type- Standard AC")
            self.s=3000*n
        elif (x==3):
            print ("Romm Type- 3-Bed Non-AC")
            self.s=2000*n
        elif (x==4):
            print ("Room Type- 3-Bed AC")
            self.s=1000*n
        else:
            print ("please choose a room")
        print (f"your choosen room rent is :{self.s}")

        sql="insert into customer_room_details(name,address,cindate,coutdate,room_no,room_type_no,stayed_days,room_rent)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self.name,self.address,self.cindate,self.coutdate,self.rno,x,n,self.s)
        mycursor.execute(sql,val)
        mydb.commit()
#***********menu card********************

    def food(self):
        print("*****RESTAURANT MENU*****")
        print("1.Dessert----->100","2.Drinks----->50","3.Breakfast------>90","4.Lunch---->110","5.Dinner--->150","6.Exit")
        while (1):
            c=int(input("Enter the number of your choice:"))
            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d
            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d
            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d
            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d
            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d
            elif (c==6):
                break;
            else:
                print("You've Enter an Invalid Key")
        print (f"Total food Cost=Rs:{self.r}")
#********************hotel bill******************************        
    def bill(self):    
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print (f"Customer name:{self.name}")
        print (f"Customer address:{self.address}")
        print (f"Check in date:{self.cindate}")
        print (f"Check out date:{self.coutdate}")
        print (f"Room no:{self.rno}")
        print (f"Your Room rent is:{self.s}")
        print (f"Your Food bill is:{self.r}")
        self.rt=self.s+self.t+self.p+self.r
        print (f"Your sub total Purchased is:{self.rt}")
        print (f"Additional Service Charges is:{self.a}")
        total=self.rt+self.a
        print (f"Your grandtotal Purchased is:{total}")
        sql="insert into customer_history(name,address,cindate,coutdate,room_no,room_rent,food_bill,tot_purchased,service_charge,grand_total)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self.name,self.address,self.cindate,self.coutdate,self.rno,self.s,self.r,self.rt,self.a,total)
        mycursor.execute(sql,val)
        mydb.commit()    
#**********************main *****************************

def main():
      a=hotel()
      while(1):       
        print("1.Enter the customer data")
        print("2.Calculate Room Rent")
        print("3.Calculate Food Purchased")
        print("4.Show total cost")
        print("5.EXIT")

        b=int(input("Enter the number:")) 
        if b==1:
         a.details()
        if b==2:
         a.roomrent()    
        if b==3:
         a.food()
        if b==4:
         a.bill()  
        if b==5:
            quit() 
        
main()
