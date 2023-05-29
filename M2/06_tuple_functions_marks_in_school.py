# Stwórz w IDE program, w którym zadeklarujesz tuplę odpowiadającą ocenom, jakie uzyskał uczeń.
# Wyświetl posortowane oceny od najniższej do najwyższej.
# Policz średnią jego ocen oraz odpowiedz czy dostanie świadectwo z paskiem (użyj if’a)
# Aby otrzymać pasek, uczeń musi uzyskać średnią ocen >= 4.75

marks_in_school = (5, 4, 3, 2, 1, 6, 2, 4)

print(sorted(marks_in_school))

average_of_marks = float(sum(marks_in_school) / len(marks_in_school))
print(average_of_marks)

if average_of_marks >= 4.75:
    print(f' Your average of marks i.e. {average_of_marks:.2f} shows that you will have certificate with distinction')
else:
    print(f' Your average of marks i.e. {average_of_marks:.2f} shows that you will not have certificate with distinction')