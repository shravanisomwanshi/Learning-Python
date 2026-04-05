def main():
    try:
        a = int(input("hey, enter a number: "))
        print(a)
        return

    except Exception as e:
           print(e)
           return

    finally:
           print("I am inside of finally")   


main()                  