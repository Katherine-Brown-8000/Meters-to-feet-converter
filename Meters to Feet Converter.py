metric = str(input("Enter M for Meters or F for feet: "))
distant = float(input("distance: "))


if metric == 'M':
    mf = distant * 3.2808399
    print(f"distance in feet is {mf:.2f}")
elif metric == 'F':
    fm = distant*0.3048
    print(f"The distance in meters is {fm:.2f}")
