x_inicial = float(input("posición en metros:"))
v_inicial = float(input("velocidad en m/s:"))
a = float(input("aceleración en m/s**2:"))
t = float(input("tiempo en s:"))
x = x_inicial + v_inicial*t + 0.5*a*t**2
v = v_inicial + a*t
print(f"la posición final son {x} m")
print(f"{v}m/s")