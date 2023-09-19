ingreso_mensual = 18300
gasto_mensual =16500

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual >3000:
        print("estas bien pa")
    else :
        print ("estas gastando una banda nose si te alcanza")    
elif ingreso_mensual > 1000 :
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500 :
    print("estas bien en Argentina")
elif ingreso_mensual > 200 :
    print("estas bien en Venezuela")
else:
    print("sos pobre")        