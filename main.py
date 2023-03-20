import vtk

input_file = "/Users/wangpengan/Desktop/startup/dental/oral_scan/nazhao/Nazhaooralscan/nazhao-stl/nazhao-stl UpperJawScan.stl"
output_file = input_file.replace(".stl", ".vtk")

# create reader for the STL file
reader = vtk.vtkSTLReader()
reader.SetFileName(input_file)
reader.Update()

# create writer for the VTK file
writer = vtk.vtkDataSetWriter()
writer.SetFileName(output_file)
writer.SetInputConnection(reader.GetOutputPort())
writer.Write()

