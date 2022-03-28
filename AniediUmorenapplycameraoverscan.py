import maya.cmds as cmds
def applycameraoverscan(camera):
    cmds.camera(name = "cameraShape2")
    camera = "cameraShape2"
    percentage = 150
    
    RRW = cmds.getAttr ("defaultResolution.width")
    print("resolution width was " + str(RRW))
#stored render resolution width as variable: RRW

    RRH = cmds.getAttr ("defaultResolution.height")
    print("resolution height was " + str(RRH))
    
#stored render resolution height as variable: RRH

    RRW = cmds.getAttr ("defaultResolution.width") * (percentage / 100.0)
    print(" NEW resolution height is " + str(RRW))
    cmds.setAttr ("defaultResolution.width", RRW)

    RRH = cmds.getAttr ("defaultResolution.height") * (percentage / 100.0)
    print(" NEW resolution height is " + str(RRH))
    cmds.setAttr ("defaultResolution.height", RRH)

#store horizaontal film aperature as variable: HCA

    HCA = cmds.getAttr (camera + ".horizontalFilmAperture")
    print(" horizontal film aperture was " + str(HCA))  

#stored vertical film aperture as variable: VCA

    VCA = cmds.getAttr (camera + ".verticalFilmAperture")
    print(" vertical film aperture was " + str(VCA))

    HCA = (HCA * 1.5)
    cmds.setAttr (camera + ".horizontalFilmAperture", HCA)
    print(" NEW horizontal film aperture is " + str(HCA))
#changed camera aperature 
   
    VCA = (VCA * 1.5)
    cmds.setAttr (camera + ".verticalFilmAperture", VCA)
    print(" NEW vertical film aperture is " + str(VCA))

applycameraoverscan("cameraShape2")



