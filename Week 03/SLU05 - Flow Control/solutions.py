def solution1 (answer="E"):
    assert answer.strip() == "D", "Wrong answer, you fall through the floor tile into an abyss!"
    print("Congratulations, you passed the tile")

def solution2 (a=0, b=0, expression1=0, expression2=0, expression3=0, expression4=0):
    print("Your answers:")
    print(f"""a={a}""")
    assert a == 1, "Wrong answer, you hear a small noise and everything around you becomes black!"
    print(f"""b={b}""")
    assert b == 99, "Wrong answer, you hear a small noise and everything around you becomes black!"
    print(f"""expression1={expression1}""")
    assert expression1==False, "Wrong answer, you hear a small noise and everything around you becomes black!"
    print(f"""expression2={expression2}""")
    assert expression2==True, "Wrong answer, you hear a small noise and everything around you becomes black!"
    print(f"""expression3={expression3}""")
    assert expression3==True, "Wrong answer, you hear a small noise and everything around you becomes black!"
    print(f"""expression4={expression4}""")
    assert expression4==False, "Wrong answer, you hear a small noise and everything around you becomes black!"
    print("The screen vanishes, you may pass!")

def solution3(answer):
    assert answer.strip() == "B", "The robot starts screaming 'Exterminate! Exterminate!',it seems it does not like your answer."
    print("The robot deactivates and you pass.")

def solution4(answer):
    assert answer == [1,2,3,4,5,6,7,8,9,10], "The lady looks at you, disapproval in her eyes. You realize you cannot move nor talk anymore."
    print("The lady nods and says 'lets take this up a notch, shall we?'")

def solution5(answer):
    assert answer == ["R","E","W","A","R","D"," ","T","I","M","E"], "The lady snips her fingers and you are being attacked by a gigantic alien kitten!"
    print("Well done, not much more and you shall be free. While you walk down the corridor you feel the ladys eyes in your back.")

def solution6(answer):
    assert answer == ['a', 'w', 'e', 's', 'o', 'm', 'e'], "A net falls on top of you and you are being pulled in a windowless chamber above the corridor"
    print("The wall vanishes and you blink as your eyes adjust to the sunshine of Planet X")

def solution7(answer):
    assert answer == [42], "No solution no special seat - they say and vanish into the crowd - fair enough"
    print("You proudly look to the person to present your correct solution - to find they vanished into thin air.")