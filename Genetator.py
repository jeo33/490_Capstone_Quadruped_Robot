import numpy as np
import matplotlib.pyplot as plt
import sys

# Get arguments from the terminal
# sys.argv[0] is the script name
# arg1 = sys.argv[1]  # First argument
# arg2 = sys.argv[2]  # Second argument
arg1 = "[(-0.1 -0.20),(0.1 -0.20),(0.0 -0.19),(0.0 -0.20)]"  # First argument
arg2 = 20  # Second argument

# Continue for additional arguments if needed
# Given points
points_str = arg1.strip("[]").split(",")

# Extract x and y coordinates for each point
points = []
for point_str in points_str:
    # Remove parentheses and split by comma
    coordinates = point_str.strip("()").split(" ")
    # Convert coordinates to float and append to points list
    points.append([float(coordinates[0]), float(coordinates[1])])

# Convert points list to numpy array
points_array = np.array(points)

# Separate x and y coordinates
x = points_array[:, 0]
y = points_array[:, 1]

# Separate points for curve and line arrays
curve_points = points[:3]
line_points = [points[0], points[1], points[3]]

# Convert curve and line points list to numpy arrays
curve_points_array = np.array(curve_points)
line_points_array = np.array(line_points)

# Separate x and y coordinates for curve and line arrays
curve_x = curve_points_array[:, 0]
curve_y = curve_points_array[:, 1]
line_x = line_points_array[:, 0]
line_y = line_points_array[:, 1]

# Fit a polynomial curve to the curve points with degree 5
degree_1 = 5
coefficients_1 = np.polyfit(curve_x, curve_y, degree_1)
polynomial_1 = np.poly1d(coefficients_1)

# Fit a polynomial curve to the line points with degree 1
degree_2 = 1
coefficients_2 = np.polyfit(line_x, line_y, degree_2)
polynomial_2 = np.poly1d(coefficients_2)

# Generate points on the polynomial curve for plotting
x_curve = np.linspace(min(curve_x), max(curve_x), 100)

# Generate 20 points on the polynomial curve for both fitted curves
num_points = arg2
x_samples_1 = np.linspace(min(x_curve), max(x_curve), num_points)
y_samples_1 = polynomial_1(x_samples_1)

x_samples_2 = np.linspace(min(curve_x), max(curve_x), num_points*3)
y_samples_2 = polynomial_2(x_samples_2)

# Initialize arrays for curve and line points
curve_array = []
line_array = []
top=[points[2][0], 0.0,points[2][1]]
mid_point=[points[3][0], 0.0,points[3][1]]

# Generate points for the curve array
for i in range(len(x_samples_1)):
    curve_array.append([x_samples_1[i], 0.0, y_samples_1[i]])

# Generate points for the line array
for i in reversed(range(len(x_samples_2))):
    line_array.append([x_samples_2[i], 0.0, y_samples_2[i]])
temp=[]
temp.append(mid_point)
final_list=temp+line_array[30:]+curve_array+line_array[0:30]
counter=0
temp_list=[]
np_list=[]
for it in final_list:
    print(f'        temp{counter}=np.array([{it[0]},{it[1]},{it[2]}])')
    temp_list.append(f"temp{counter}")
    np_list.append(f"np.array([{it[0]},{it[1]},{it[2]}])")
    counter+=1
for it in range(0,4):
    if it==0:
        for its in range(1+it*int(arg2),counter+1+it*int(arg2)):
            if f"temp{its%counter}" in temp_list:
                print(f'        BR.append(temp{its%counter})#{np_list[its%counter]}')
    if it==1:
        for its in range(1+it*int(arg2),counter+1+it*int(arg2)):
            if f"temp{its%counter}" in temp_list:
                print(f'        BL.append(temp{it%counter})#{np_list[its%counter]}')
    if it==2:
        for its in range(1+it*int(arg2),counter+1+it*int(arg2)):
            if f"temp{its%counter}" in temp_list:
                print(f'        FR.append(temp{its%counter})#{np_list[its%counter]}')
    if it==3:
        for its in range(1+it*int(arg2),counter+1+it*int(arg2)):
            if f"temp{its%counter}" in temp_list:
                print(f'        FL.append(temp{its%counter})#{np_list[its%counter]}')

# Plot the original points, the fitted curves, and the sampled points
plt.figure(figsize=(10, 8))

# Plot the first fitted curve
plt.plot(x_curve, polynomial_1(x_curve), color='red', label=f'Fitted Curve (Degree {degree_1})')
plt.scatter(x_samples_1, y_samples_1, color='green', label=f'Sampled Points (Degree {degree_1})')

# Plot the second fitted curve
plt.plot(x_curve, polynomial_2(x_curve), color='blue', label=f'Fitted Curve (Degree {degree_2})')
plt.scatter(x_samples_2, y_samples_2, color='orange', label=f'Sampled Points (Degree {degree_2})')

# Plot the original points
plt.scatter(x, y, color='black', label='Given Points')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation of Given Points')
plt.legend()
plt.grid(True)
plt.show()

