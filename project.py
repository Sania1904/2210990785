print("WELCOME TO THE QUIZ GAME")
import random
ques=["Who is the prime minister of India?","What is the national animal of India?","What is the capital of America?","Who is the finance minister of India?","Which river runs through Egypt?","What is the derivative of log x?","Light year is a unit of","How many alphabets are there in English language?","Who is the richest person in the world?","What is actually electricity?","Which of the following disorders is the fear of being alone?","What is the speed of sound?","What do we call a newly hatched butterfly?","What is the main component of the sun?","Which two months are named after Emperors of the Roman Empire?","Which of the following animals can run the fastest?"," In the United States, football is called soccer. So what is American football called in the United Kingdom?","In which country is Transylvania?","The phrase: ”I think, therefore I am” was coined by which philosopher?","What does the term SOS commonly stand for?","Which company is known for publishing the Mario video game?","We often use sodium bicarbonate in the kitchen. What is its other name?"]
ans1=["Kejriwal","Tiger","Oslo","Ram Nath Kovind","Amazon","1/x","mass",25,"Jeff Bezos","Flow of electrons","Agoraphobia","120 km/h","A moth","Liquid lava"," January and February","Cheetah","Rugby","Bulgaria","Socrates"," Save Our Sheep","Xbox","Salt"]
ans2=["Rahul Gandhi","Peacock","Jakarta","Rajnath Singh","Nile","1/x**2","time",26,"Bill Gates","Flow of water","Aerophobia","1,200 km/h","A butter","Molten iron","March and April","Leopard","American football","Romania","Plato","Save Our Ship","Nintendo","Vinegar"]
ans3=["Manmohan Singh","Giraffe","Washington","Nirmala Sitharaman","Yangtze","log x","distance",28,"Elon musk","Flow of air","Acrophobia","400 km/h","A caterpillar","Gas","May and June","Tiger","Handball","Croatia","Aristotle","Save Our Seal","SEGA","Baking soda"]
ans4=["Narendra Modi","Panda","Ontario","Sambit Patra","Mississipi","x","gravity",30,"Gautam Adani","Flow of atoms","Arachnophobia","700 km/h","A chrysalis","Rock","July and August","Lion","Combball","Siberia","Descartes","Save Our Souls","Electronic arts","Sugar"]
q=int(input("HOW MANY QUESTIONS DO YOU WANT TO ANSWER?"))
rans=[4,1,3,3,2,1,3,2,3,1,1,2,3,3,4,1,2,2,4,4,2]
list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(list)
tempans=[]
for k in range(q):
    i=list[k]
    print("Question:",ques[i])
    print("1.",ans1[i])
    print("2.",ans2[i])
    print("3.",ans3[i])
    print("4.",ans4[i])
    ans=int(input("ENTER CHOICE 1-4:"))
    tempans.append(ans)
right=0
wrong=0
for i in range(q):
    if rans[list[i]]==tempans[i]:
        right=right+1
        print("NO.",i+1,"ANSWER IS CORRECT")
    else:
        print("NO.",i+1,"ANSWER IS INCORRECT")
        wrong=wrong+1
print("-----Result-----")
print("Right answers=",right)
print("Wrong answers=",wrong)
print("-----End-----")