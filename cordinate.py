img_height = 450
img_width = 800

x_min, y_min, x_max, y_max = 0, 0, 0, 0

x_min = int(input("Enter x_min:"))
y_min = int(input("Enter y_min:"))
x_max = int(input("Enter x_max:"))
y_max = int(input("Enter y_max:"))


x_centre, y_centre = (x_min + x_max) / 2, (y_min + y_max) / 2
print(x_centre, y_centre)
if (x_centre < (img_width / 2) - 50):
    print("Object is on left side")
elif(x_centre > (img_width / 2) + 50):
    print("Object is on right side")
else:
    print("Object is in centre")
