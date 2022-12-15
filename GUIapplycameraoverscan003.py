import maya.cmds as cmds
    
def onButtonClicked1():
    
    global camera
    x=0
    cmds.camera(name= "camera_1")
    
def onButtonClicked2():
    
    global camera
    x=0
    x+=1
    RRW = cmds.getAttr ("defaultResolution.width")
    RRH = cmds.getAttr ("defaultResolution.height")
   
    RRW = cmds.getAttr ("defaultResolution.width") * 1.5
    RRW = cmds.setAttr ("defaultResolution.width", RRW)
    print("resolution width is" + str(RRW))
    
    RRH = cmds.getAttr ("defaultResolution.height") * 1.5
    RRH = cmds.setAttr ("defaultResolution.height", RRH)
    print("resolution height is" + str(RRH))
    
    HCA = cmds.getAttr ("camera_1Shape" + str(x) + ".horizontalFilmAperture")
    print(" horizontal film aperture was " + str(HCA)) 
    HCA = HCA + (HCA * 1.5)
    cmds.setAttr ("camera_1Shape" + str(x) + ".horizontalFilmAperture", HCA)
    print(" horizontal film aperture IS " + str(HCA))
    
    VCA = cmds.getAttr ("camera_1Shape" + str(x) + ".verticalFilmAperture")
    print(" vertical film aperture was " + str(VCA))
    VCA = VCA + (VCA * 1.5)
    cmds.setAttr ("camera_1Shape" + str(x) + ".verticalFilmAperture", VCA)
    
def onButtonClicked3():
    
    global camera
    x=0
    x+=1
    RRW = cmds.getAttr ("defaultResolution.width")
    print("resolution width is " + str(RRW))
    RRH = cmds.getAttr ("defaultResolution.height")
    print("resolution height is " + str(RRH))
    HCA = cmds.getAttr ("camera_1Shape" + str(x) +".horizontalFilmAperture")
    print(" horizontal film aperture IS " + str(HCA))
    VCA = cmds.getAttr ("camera_1Shape" + str(x) + ".verticalFilmAperture")
    print(" horizontal film aperture IS " + str(VCA))

    
def launchchangeRRUI():
   
    window = cmds.window(title="Render Resolution")
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="create camera", command="onButtonClicked1()")
    cmds.button(label="change render resolution", command="onButtonClicked2()")
    cmds.button(label="check render resolution", command="onButtonClicked3()")


  
    cmds.showWindow(window)
    
launchchangeRRUI()
