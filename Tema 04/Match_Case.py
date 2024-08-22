serie = "N-02"

if serie == "N-01":
    print("sansung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No esiste ese producto")





match serie:
    case "N-01":
        print("sansung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No esiste ese producto")