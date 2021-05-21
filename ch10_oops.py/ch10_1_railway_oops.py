class RailwayForm:
    formType = "RailwayForm"#deifine variable into the class
    def printData(self): #define function into the class
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = RailwayForm() #object creation:(step 1: creating new application )
harrysApplication.name = "Harry"  #passing values by objects (or) information assciated by Application : (stpe 2: putting data into application)
harrysApplication.train = "Rajdhani Express" # informTION ASSOCIATED BY APPLICATION  (stpe 2: putting data into application)
harrysApplication.printData() #calling method "printData()" (step:3 : print that data of that application)

