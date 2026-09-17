degree=(int(input("enter the degree: "))
        print("the degree is:",degree)
        if degree <=20:
        
            print("cold wheather.")
        elif degree >=20 and degree <=38:
            print("normal weather.")
        else:
            print("HOT! weather.")
            fahrenheit=(degree*1.8)+32
            print("the fahrenheit value is:",fahrenheit,"F")