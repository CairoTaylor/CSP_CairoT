#Cairo Taylor, Name Decorator

name = input("What is your name?\n").strip().capitalize()
decoration1 = "$o$"
decoration2_1 = "o-[----"
decoration2_2 = "----]-o"
decoration3_1 = "<)-"
decoration3_2 = "-(>"
decoration4_1 = ",o`"
decoration4_2 = "`o,"
decoration5_1 = "(╯°□°)╯︵ ┻━┻"
decoration5_2 = "┻━┻ ︵╰(°□°╰)"
decoration6 = "⛧  \(*□*)/ ⛧"

# ~:)-|--[
decor1 = decoration1+name+decoration1
decor2 = decoration2_1+name+decoration2_2
decor3 = decoration3_1+name+decoration3_2
decor4 = decoration4_1+name+decoration4_2
decor5 = decoration5_1+name+decoration5_2
decor6 = decoration6+name+decoration6

print(decor1)
print(decor2)
print(decor3)
print(decor4)
print(decor5)
print(decor6)