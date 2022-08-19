import json
import getpass
import hashlib
class loginsys():
    
    def encrypt_password(self, password):
        hash_string = password
        hash_string = hash_string.encode()
        return hashlib.sha256(hash_string).hexdigest()
    
    
    def menu(self):
        x=int(input("Please enter:\n0 to exit\n1 to register\n2 to login"))
        if x==0:
            return None
        elif x==1:
            y=self.register()
            return y
        elif x==2:
            y=self.login()
            return y
        else:
            print("Invalid input. Enter again")
            self.menu()
           
    def register(self):
        self.username=input("enter username\n")
        self.password=getpass.getpass('enter password\n')
        self.password = self.encrypt_password(self.password)
        self.confirm_password = getpass.getpass('confirm password\n')
        self.confirm_password = self.encrypt_password(self.confirm_password)
        if(self.confirm_password==self.password):
            print("Registered successfully.\n")

            with open('LoginSystemData.json', 'a') as f:      
                    f.write( self.username + "," + self.password+"\n")
            

        else:
            print("Registration failed! Please confirm your Password correctly.\n")
            self.menu()
        return self.username         
                
    def login(self):
        self.username=input("enter username\n")
        self.password=getpass.getpass('enter password\n')
        self.password = self.encrypt_password(self.password)
        success = False
        with open('LoginSystemData.json', 'r') as f: 
            x=f.read()
            l=x.split("\n")
            for i in range(len(l)-1):
                
                a,b = l[i].split(",")
                correct=0
                b = b.strip()
                a = a.strip()
                if(a==self.username and b==self.password):
                    print("Login successful")
                    correct=1
                   
            if correct==0:
                print("Login failed. Wrong Username or Password.\n")
                self.menu()
                
            return self.username   
                               
