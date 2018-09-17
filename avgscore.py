import math

def avg_scores():
    print("This is a program to help you calculate the average test score across 10 tests. Please answer the questions accurately to provide an accurate score.")
    test1=float(input("Score for Test 1? "))
    test2=float(input("Score for Test 2? "))
    test3=float(input("Score for Test 3? "))
    test4=float(input("Score for Test 4? "))
    test5=float(input("Score for Test 5? "))
    test6=float(input("Score for Test 6? "))
    test7=float(input("Score for Test 7? "))
    test8=float(input("Score for Test 8? "))
    test9=float(input("Score for Test 9? "))
    test10=float(input("Score for Test 10? "))
    avg=test1+test2+test3+test4+test5+test6+test7+test8+test9+test10/10
    print(avg)
avg_scores()
