from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def calculator() :
    a = float(input("첫번째 숫자: "))
    b = float(input("두번째 숫자: "))
    op = input("연산자 (+, -, *, /) : ")
    operation = {
        '+' : add,
        '-' : subtract,
        '*' : multiply,
        '/' : divide,
    }
    if op in operation :
        try :
            result = operation[op](a,b)
            print("result", result)
        except Exception as e :
            print("오류", e)
    else :
        print("Invalid operator")

if __name__ == "__main__" :
    calculator()