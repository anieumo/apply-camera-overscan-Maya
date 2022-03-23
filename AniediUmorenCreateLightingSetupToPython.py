import maya.cmds as cmds

cmds.polyPlane(name="Plane_GEO")
cmds.scale(24, 24, 24, relative=True)

cmds.polySphere(name="sphere_GEO")
cmds.move(0, 1, 0, relative=True)

cmds.camera(name="shot_CAM1")
cmds.move(0, 0, 18, relative=True)

cmds.pointLight(name="key_LGT")
cmds.move(24.5, 5, 17, relative=True)
cmds.rotate(-7, 55, 0, relative=True)

cmds.spotLight(name="fill_LGT")
cmds.move(-21, 2, 19.5, relative=True)
cmds.rotate(-1.4, -43, 0, relative=True)

cmds.directionalLight(name="back_LGT")
cmds.move(-16.8,6, -19, relative=True)
cmds.rotate(168, -40, 180, relative=True)

print("FINISHED!")





