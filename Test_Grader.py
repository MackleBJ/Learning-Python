#Test Grader

grade=input("Enter your exam grade:")
f_grd=float(grade)
if f_grd >1.0:
    f_grd=f_grd/100
if f_grd >=.9:
    Letter="A"
elif f_grd>=.8:
    Letter="B"
elif f_grd>=.7:
    Letter="C"
elif f_grd >=.6:
    Letter="D"
else:
    Letter="F"

print("Letter Grade=",Letter)
