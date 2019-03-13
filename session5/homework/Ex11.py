def is_inside(x,y):
    if x[0] >= y[0] and x[1] >= y[1] and x[0] <= (y[0]+y[2]) and x[1] <= (y[1]+y[3]):
        print("True")
    else:
        print("False")

is_inside([100,200],[40,60,200,300])