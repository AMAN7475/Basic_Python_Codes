L = int(input("Enter Length (in Feet) : "))
B = int(input("Enter Breadth (in Feet) : "))
H = int(input("Enter Height (in Feet) : "))
Paint_Coverage = int(input("Enter Paint_Coverage (in Sq. Ft/Litre) : "))

Surface_area = 2*(L*B) + 2*(B*H) + 2*(H*L)

Area_of_floor = L*B

Paintable_area = (Surface_area - Area_of_floor)

Required_Paint = Paintable_area / Paint_Coverage
print("Required_Paint = ", Required_Paint,"Litre")