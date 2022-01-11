import sys
import os

sys.path.append("/home/advait/visit/visit3_1_4.linux-x86_64-ubuntu20/visit3_1_4.linux-x86_64/3.1.4/linux-x86_64/lib/site-packages")
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import visit

# Open the database
testfile_path = "/home/advait/projects/bettinumbers/datasets/highrotminhel/velocity.800000.h5"
visit.OpenDatabase(testfile_path)

# Create a vector expression
DefineVectorExpression("a","{<PS/vx>,<PS/vy>,<PS/vz>}")

# Compute the curl of the vector expression to get the vorticity vector
DefineVectorExpression("b","curl(a)")

# Compute the absolute of the vorticity vector
DefineScalarExpression("c","magnitude(b)")
AddPlot("Volume","c")

# Annotation Attributes
a=AnnotationAttributes()
a.axes3D.visible=1
a.axes3D.triadFlag=1
a.axes3D.bboxFlag=1
a.databaseInfoFlag=1
a.legendInfoFlag=1
SetAnnotationAttributes(a)

# View Attributes
viewatt=View3DAttributes()
viewatt.imageZoom=1.00
SetView3D(viewatt)
DrawPlots()
# SaveWindow()

# Wildcard usage
data_x = []
data_y = []
data_z = []
def processPickOutput(pickOutput):
    vorticity = pickOutput.get('c')
    coords = pickOutput.get('point')
    # print(vorticity, coords)
    return list(vorticity.values())

# Go through all the picks by nodes and extract the points
from collections import OrderedDict
x_index = 0
y_index = 0
z_index = 0
for i in range(128):
    PickByNode(element=x_index)
    pickOutput = GetPickOutputObject()
    pointCloud_x = processPickOutput(pickOutput)
    for values in pointCloud_x:
        data_x.append(values)
    data_x = list(OrderedDict.fromkeys(data_x))
    x_index = x_index + 1

    PickByNode(element=y_index)
    pickOutput = GetPickOutputObject()
    pointCloud_y = processPickOutput(pickOutput)
    for values in pointCloud_y:
        data_y.append(values)
    data_y = list(OrderedDict.fromkeys(data_y))
    y_index = y_index + 129

    PickByNode(element=z_index)
    pickOutput = GetPickOutputObject()
    pointCloud_z = processPickOutput(pickOutput)
    for values in pointCloud_z:
        data_z.append(values)
    data_z = list(OrderedDict.fromkeys(data_z))
    z_index = z_index + 129 * 129


grid_points = 128
# Method to pick all the points in the vorticity cube
# def pickAllpoints():
    # for i in range(grid_points):
        # for j in range(grid_points):
            # for k in range(grid_points):
                # PickByNode(element=i)
                # pickOutput = GetPickOutputObject()
                # pointCloud_x = processPickOutput(pickOutput)
                # for values in pointCloud_x:
                    # data_x.append(values)
                # # data_x = list(OrderedDict.fromkeys(data_x))

                # PickByNode(element=j)
                # pickOutput = GetPickOutputObject()
                # pointCloud_y = processPickOutput(pickOutput)
                # for values in pointCloud_y:
                    # data_y.append(values)
                # # data_y = list(OrderedDict.fromkeys(data_y))

                # PickByNode(element=k)
                # pickOutput = GetPickOutputObject()
                # pointCloud_z = processPickOutput(pickOutput)
                # for values in pointCloud_z:
                    # data_z.append(values)
                # # data_z = list(OrderedDict.fromkeys(data_z))

                # print(i, j, k)

pointCloud = []
for i in range(len(data_x)):
    pointCloud.append([data_x[i], data_y[i], data_z[i]])
print(pointCloud)
print(len(pointCloud))

import pickle
with open('pointCloud', 'wb') as fp:
    pickle.dump(pointCloud, fp)
    print("Successful pickle dump of point cloud")
