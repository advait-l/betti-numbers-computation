# Visit 3.1.4 log file
ScriptVersion = "3.1.4"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
ShowAllWindows()
OpenDatabase("/home/advait/projects/bettinumbers/datasets/highrotminhel/velocity.800000.h5", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
DefineScalarExpression("operators/ConnectedComponents/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/Flux/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineVectorExpression("a", "{<PS/vx>,<PS/vy>,<PS/vz>}")
DefineScalarExpression("operators/ConnectedComponents/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/Flux/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineVectorExpression("a", "{<PS/vx>,<PS/vy>,<PS/vz>}")
DefineVectorExpression("b", "curl(a)")
DefineScalarExpression("operators/ConnectedComponents/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/Flux/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineCurveExpression("operators/Lineout/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh_128x128x128>, 0)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vx", "cell_constant(<PS/vx>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vy", "cell_constant(<PS/vy>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/PS/vz", "cell_constant(<PS/vz>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh_128x128x128", "cell_constant(<mesh_128x128x128>, 0.)")
DefineVectorExpression("a", "{<PS/vx>,<PS/vy>,<PS/vz>}")
DefineVectorExpression("b", "curl(a)")
DefineScalarExpression("c", "magnitude(b)")
AddPlot("Volume", "c", 1, 0)
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.axes3D.triadColor = (0, 0, 0)
AnnotationAtts.axes3D.triadLineWidth = 1
AnnotationAtts.axes3D.triadFont = 0
AnnotationAtts.axes3D.triadBold = 1
AnnotationAtts.axes3D.triadItalic = 1
AnnotationAtts.axes3D.triadSetManually = 0
AnnotationAtts.userInfoFlag = 1
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 1
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, 0, 1)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0, 1, 0)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.5
View3DAtts.nearPlane = -0.5
View3DAtts.farPlane = 0.5
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 0
SetView3D(View3DAtts)
# End spontaneous state

View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0, 0, 1)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0, 1, 0)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.5
View3DAtts.nearPlane = -0.5
View3DAtts.farPlane = 0.5
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 0
SetView3D(View3DAtts)
DrawPlots()
PickByNode(element=0)
PickByNode(element=0)
PickByNode(element=0)
PickByNode(element=1)
PickByNode(element=129)
PickByNode(element=16641)
PickByNode(element=2)
PickByNode(element=258)
PickByNode(element=33282)
PickByNode(element=3)
PickByNode(element=387)
PickByNode(element=49923)
PickByNode(element=4)
PickByNode(element=516)
PickByNode(element=66564)
PickByNode(element=5)
PickByNode(element=645)
PickByNode(element=83205)
PickByNode(element=6)
PickByNode(element=774)
PickByNode(element=99846)
PickByNode(element=7)
PickByNode(element=903)
PickByNode(element=116487)
PickByNode(element=8)
PickByNode(element=1032)
PickByNode(element=133128)
PickByNode(element=9)
PickByNode(element=1161)
PickByNode(element=149769)
PickByNode(element=10)
PickByNode(element=1290)
PickByNode(element=166410)
PickByNode(element=11)
PickByNode(element=1419)
PickByNode(element=183051)
PickByNode(element=12)
PickByNode(element=1548)
PickByNode(element=199692)
PickByNode(element=13)
PickByNode(element=1677)
PickByNode(element=216333)
PickByNode(element=14)
PickByNode(element=1806)
PickByNode(element=232974)
PickByNode(element=15)
PickByNode(element=1935)
PickByNode(element=249615)
PickByNode(element=16)
PickByNode(element=2064)
PickByNode(element=266256)
PickByNode(element=17)
PickByNode(element=2193)
PickByNode(element=282897)
PickByNode(element=18)
PickByNode(element=2322)
PickByNode(element=299538)
PickByNode(element=19)
PickByNode(element=2451)
PickByNode(element=316179)
PickByNode(element=20)
PickByNode(element=2580)
PickByNode(element=332820)
PickByNode(element=21)
PickByNode(element=2709)
PickByNode(element=349461)
PickByNode(element=22)
PickByNode(element=2838)
PickByNode(element=366102)
PickByNode(element=23)
PickByNode(element=2967)
PickByNode(element=382743)
PickByNode(element=24)
PickByNode(element=3096)
PickByNode(element=399384)
PickByNode(element=25)
PickByNode(element=3225)
PickByNode(element=416025)
PickByNode(element=26)
PickByNode(element=3354)
PickByNode(element=432666)
PickByNode(element=27)
PickByNode(element=3483)
PickByNode(element=449307)
PickByNode(element=28)
PickByNode(element=3612)
PickByNode(element=465948)
PickByNode(element=29)
PickByNode(element=3741)
PickByNode(element=482589)
PickByNode(element=30)
PickByNode(element=3870)
PickByNode(element=499230)
PickByNode(element=31)
PickByNode(element=3999)
PickByNode(element=515871)
PickByNode(element=32)
PickByNode(element=4128)
PickByNode(element=532512)
PickByNode(element=33)
PickByNode(element=4257)
PickByNode(element=549153)
PickByNode(element=34)
PickByNode(element=4386)
PickByNode(element=565794)
PickByNode(element=35)
PickByNode(element=4515)
PickByNode(element=582435)
PickByNode(element=36)
PickByNode(element=4644)
PickByNode(element=599076)
PickByNode(element=37)
PickByNode(element=4773)
PickByNode(element=615717)
PickByNode(element=38)
PickByNode(element=4902)
PickByNode(element=632358)
PickByNode(element=39)
PickByNode(element=5031)
PickByNode(element=648999)
PickByNode(element=40)
PickByNode(element=5160)
PickByNode(element=665640)
PickByNode(element=41)
PickByNode(element=5289)
PickByNode(element=682281)
PickByNode(element=42)
PickByNode(element=5418)
PickByNode(element=698922)
PickByNode(element=43)
PickByNode(element=5547)
PickByNode(element=715563)
PickByNode(element=44)
PickByNode(element=5676)
PickByNode(element=732204)
PickByNode(element=45)
PickByNode(element=5805)
PickByNode(element=748845)
PickByNode(element=46)
PickByNode(element=5934)
PickByNode(element=765486)
PickByNode(element=47)
PickByNode(element=6063)
PickByNode(element=782127)
PickByNode(element=48)
PickByNode(element=6192)
PickByNode(element=798768)
PickByNode(element=49)
PickByNode(element=6321)
PickByNode(element=815409)
PickByNode(element=50)
PickByNode(element=6450)
PickByNode(element=832050)
PickByNode(element=51)
PickByNode(element=6579)
PickByNode(element=848691)
PickByNode(element=52)
PickByNode(element=6708)
PickByNode(element=865332)
PickByNode(element=53)
PickByNode(element=6837)
PickByNode(element=881973)
PickByNode(element=54)
PickByNode(element=6966)
PickByNode(element=898614)
PickByNode(element=55)
PickByNode(element=7095)
PickByNode(element=915255)
PickByNode(element=56)
PickByNode(element=7224)
PickByNode(element=931896)
PickByNode(element=57)
PickByNode(element=7353)
PickByNode(element=948537)
PickByNode(element=58)
PickByNode(element=7482)
PickByNode(element=965178)
PickByNode(element=59)
PickByNode(element=7611)
PickByNode(element=981819)
PickByNode(element=60)
PickByNode(element=7740)
PickByNode(element=998460)
PickByNode(element=61)
PickByNode(element=7869)
PickByNode(element=1015101)
PickByNode(element=62)
PickByNode(element=7998)
PickByNode(element=1031742)
PickByNode(element=63)
PickByNode(element=8127)
PickByNode(element=1048383)
PickByNode(element=64)
PickByNode(element=8256)
PickByNode(element=1065024)
PickByNode(element=65)
PickByNode(element=8385)
PickByNode(element=1081665)
PickByNode(element=66)
PickByNode(element=8514)
PickByNode(element=1098306)
PickByNode(element=67)
PickByNode(element=8643)
PickByNode(element=1114947)
PickByNode(element=68)
PickByNode(element=8772)
PickByNode(element=1131588)
PickByNode(element=69)
PickByNode(element=8901)
PickByNode(element=1148229)
PickByNode(element=70)
PickByNode(element=9030)
PickByNode(element=1164870)
PickByNode(element=71)
PickByNode(element=9159)
PickByNode(element=1181511)
PickByNode(element=72)
PickByNode(element=9288)
PickByNode(element=1198152)
PickByNode(element=73)
PickByNode(element=9417)
PickByNode(element=1214793)
PickByNode(element=74)
PickByNode(element=9546)
PickByNode(element=1231434)
PickByNode(element=75)
PickByNode(element=9675)
PickByNode(element=1248075)
PickByNode(element=76)
PickByNode(element=9804)
PickByNode(element=1264716)
PickByNode(element=77)
PickByNode(element=9933)
PickByNode(element=1281357)
PickByNode(element=78)
PickByNode(element=10062)
PickByNode(element=1297998)
PickByNode(element=79)
PickByNode(element=10191)
PickByNode(element=1314639)
PickByNode(element=80)
PickByNode(element=10320)
PickByNode(element=1331280)
PickByNode(element=81)
PickByNode(element=10449)
PickByNode(element=1347921)
PickByNode(element=82)
PickByNode(element=10578)
PickByNode(element=1364562)
PickByNode(element=83)
PickByNode(element=10707)
PickByNode(element=1381203)
PickByNode(element=84)
PickByNode(element=10836)
PickByNode(element=1397844)
PickByNode(element=85)
PickByNode(element=10965)
PickByNode(element=1414485)
PickByNode(element=86)
PickByNode(element=11094)
PickByNode(element=1431126)
PickByNode(element=87)
PickByNode(element=11223)
PickByNode(element=1447767)
PickByNode(element=88)
PickByNode(element=11352)
PickByNode(element=1464408)
PickByNode(element=89)
PickByNode(element=11481)
PickByNode(element=1481049)
PickByNode(element=90)
PickByNode(element=11610)
PickByNode(element=1497690)
PickByNode(element=91)
PickByNode(element=11739)
PickByNode(element=1514331)
PickByNode(element=92)
PickByNode(element=11868)
PickByNode(element=1530972)
PickByNode(element=93)
PickByNode(element=11997)
PickByNode(element=1547613)
PickByNode(element=94)
PickByNode(element=12126)
PickByNode(element=1564254)
PickByNode(element=95)
PickByNode(element=12255)
PickByNode(element=1580895)
PickByNode(element=96)
PickByNode(element=12384)
PickByNode(element=1597536)
PickByNode(element=97)
PickByNode(element=12513)
PickByNode(element=1614177)
PickByNode(element=98)
PickByNode(element=12642)
PickByNode(element=1630818)
PickByNode(element=99)
PickByNode(element=12771)
PickByNode(element=1647459)
PickByNode(element=100)
PickByNode(element=12900)
PickByNode(element=1664100)
PickByNode(element=101)
PickByNode(element=13029)
PickByNode(element=1680741)
PickByNode(element=102)
PickByNode(element=13158)
PickByNode(element=1697382)
PickByNode(element=103)
PickByNode(element=13287)
PickByNode(element=1714023)
PickByNode(element=104)
PickByNode(element=13416)
PickByNode(element=1730664)
PickByNode(element=105)
PickByNode(element=13545)
PickByNode(element=1747305)
PickByNode(element=106)
PickByNode(element=13674)
PickByNode(element=1763946)
PickByNode(element=107)
PickByNode(element=13803)
PickByNode(element=1780587)
PickByNode(element=108)
PickByNode(element=13932)
PickByNode(element=1797228)
PickByNode(element=109)
PickByNode(element=14061)
PickByNode(element=1813869)
PickByNode(element=110)
PickByNode(element=14190)
PickByNode(element=1830510)
PickByNode(element=111)
PickByNode(element=14319)
PickByNode(element=1847151)
PickByNode(element=112)
PickByNode(element=14448)
PickByNode(element=1863792)
PickByNode(element=113)
PickByNode(element=14577)
PickByNode(element=1880433)
PickByNode(element=114)
PickByNode(element=14706)
PickByNode(element=1897074)
PickByNode(element=115)
PickByNode(element=14835)
PickByNode(element=1913715)
PickByNode(element=116)
PickByNode(element=14964)
PickByNode(element=1930356)
PickByNode(element=117)
PickByNode(element=15093)
PickByNode(element=1946997)
PickByNode(element=118)
PickByNode(element=15222)
PickByNode(element=1963638)
PickByNode(element=119)
PickByNode(element=15351)
PickByNode(element=1980279)
PickByNode(element=120)
PickByNode(element=15480)
PickByNode(element=1996920)
PickByNode(element=121)
PickByNode(element=15609)
PickByNode(element=2013561)
PickByNode(element=122)
PickByNode(element=15738)
PickByNode(element=2030202)
PickByNode(element=123)
PickByNode(element=15867)
PickByNode(element=2046843)
PickByNode(element=124)
PickByNode(element=15996)
PickByNode(element=2063484)
PickByNode(element=125)
PickByNode(element=16125)
PickByNode(element=2080125)
PickByNode(element=126)
PickByNode(element=16254)
PickByNode(element=2096766)
PickByNode(element=127)
PickByNode(element=16383)
PickByNode(element=2113407)
