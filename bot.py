# making a bot which can tell u about your mood
print("👋 Hello! I'm PythonBot. Let's get to know you!")
name=input("what is your name:")
print("Hi",name)
user=input("How can i help you?: ")
print("of course! i can help u with : ",user)
mood=input("what are u feeling today?:")
mood=int(input("rate it on the scale of 1 to 10 i will let u know about your mood: "))
if mood ==10:
 print("🥳OVERJOYED Woah! you're full of joy today!")
elif mood ==9:
 print("🥰EXCITED Woah! you're full of joy today!")
elif mood ==8:
 print("😁HAPPY Awsome! you're doing great")
elif mood ==7:
  print("😀CONTENT Awsome! you're doing great")
elif mood ==6:
 print("😄CALM Awsome! you're doing great")
elif mood ==5:
 print("😊NEUTRAL HUH? let's make it better!")
elif mood ==4:
  print("🥱TIRED I hope your day gets better. Try some rest or music")
elif mood ==3:
 print("😖ANXIOUS")
elif mood ==2:
 print("😓VERY SAD")
elif mood ==1:
  print("😔DEPRESSED")
else:
  print("please enter between the range of 1 to 10")
