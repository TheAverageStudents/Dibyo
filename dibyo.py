class Dibyo:
    def __init__(self, params : dict):
        self.params = params
        self.params['coins'] = 0
        self.sleeping = False

        #Here, we check if some values were passed in by the user.
        #If not, we declare is ourself.
        if(not(self.params.get("name"))):self.params["name"] = "Dibo" #Ensure there is a name
        if(not(self.params.get("IQ"))):self.params["IQ"] = 0 #Ensure there is an IQ score

        #Make stuff easier here
        self.name = self.params.get("name")
        self.coins = self.params.get("coins")
        self.IQ = self.params.get("IQ")

    def fetchIQ(self):
        return self.IQ
    
    def speak(self, text):
        print(self.name, "says", text)
    
    def shout(self, text):
        print(self.name, ":", str(text).upper())

    def sleep(self):
        print(self.name, "going to sleep, gn.")
        self.sleeping = True
    
    def wakeup(self):
        print("Good morning.")
        self.sleeping = False

    def giveCash(self, coins : int):
        self.coins += coins
        return self.coins

    def flick(self, coins : int):
        self.coins -= coins
        if(self.coins < 0):
            print(self.name, "is bankrupt.")
        elif(self.coins == 0):
            print(self.name, "is broke.")
        return self.coins

    def test(self):
        print("Hello check check 123 123 Dibyo working")


"""
#Obviously

deebyo = Dibyo({
    "name" : "Dibo",
    "Description" : "Dibyo.",
    "Class" : "11I (maybe)"
})

#Testing area

deebyo.speak("Hi, my name is " + deebyo.name)
deebyo.shout("Hi guys my IQ is " + str(deebyo.IQ))

deebyo.giveCash(105)

print(deebyo.coins)

deebyo.flick(110)

print(deebyo.coins)
"""
