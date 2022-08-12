from dibyo import Dibyo

dibs = Dibyo({
    "name" : "deebyo",
    "IQ" : 50
})

dibs.test()

dibs.shout(f"My IQ is {dibs.IQ}")

dibs.sleep()
print(dibs.sleeping)
dibs.wakeup()
print(dibs.sleeping)

print(dibs.coins)
dibs.giveCash(25)
print(dibs.coins)
dibs.flick(30)
print(dibs.coins)