from numpy import put_along_axis
from gl import Raytracer, V3
from obj import *
from figures import *

# Dimensiones
width = 1980
height = 1080



# Materiales sin texturas
refle = Material(diffuse=(0.93, 0.27, 0.27) ,spec = 64, ior = 1.33, matType = REFLECTIVE)
vidrio = Material(diffuse= (0.98, 0.96, 0.96), spec= 64, ior = 1.33, matType= TRANSPARENT)


# Materiales con texturas
snow = Material(texture = Texture('Sources/ah.bmp'))
wood = Material(texture = Texture('Sources/wooded.bmp'))
stri = Material(texture = Texture('Sources/sni.bmp'))
roquis = Material(texture = Texture('Sources/roca.bmp'))
redix = Material(texture = Texture('Sources/red.bmp'))
pandix = Material(texture = Texture('Sources/panda.bmp'))
kik = Material(texture= Texture("Sources/kik.bmp"))
redwo = Material(texture= Texture("Sources/redwo.bmp"))
px = Material(texture= Texture("Sources/px.bmp"))
mx = Material(texture= Texture("Sources/plip.bmp"))
galaxy = Material(texture= Texture("Sources/Galaxys/galaxy3.bmp"))
galaxy2 = Material(texture= Texture("Sources/Galaxys/pia2.bmp"))
galaxy3 = Material(texture= Texture("Sources/Galaxys/pia3.bmp"))
planeta = Material(texture= Texture("Sources/sol.bmp"))
sol = Material(texture= Texture("Sources/planeta.bmp"))


# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('Sources/fondo.bmp')
#rtx.envmap = EnvMap('3k.bmp')

# Luces
rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.5))



# Esfera principal 
rtx.scene.append( Sphere(V3(0,0,-8), 1, vidrio ))


#Esferas texturizadas
rtx.scene.append( Sphere(V3(1.5,1.5,-8), 0.5, roquis ))
rtx.scene.append( Sphere(V3(1.8,0,-8), 0.5, redix ))
rtx.scene.append( Sphere(V3(1.5,-1.5,-8), 0.5, wood ))
rtx.scene.append( Sphere(V3(-1.5,-1.3,-8), 0.5, stri ))
rtx.scene.append( Sphere(V3(-1.8,0,-8), 0.5, kik ))
rtx.scene.append( Sphere(V3(-1.5,1.6,-8), 0.5, redwo ))
rtx.scene.append( Sphere(V3(0, 2,-8), 0.5, px ))
rtx.scene.append( Sphere(V3(-0.1,-1.8,-8), 0.5, mx ))

# las de la esquina
rtx.dirLight = DirectionalLight(direction = V3(5.4, -1.8, -3), intensity = 0.8)
rtx.scene.append( Sphere(V3(5.8,-1.8,-10), 1.5, sol ))
rtx.scene.append( Sphere(V3(3.4, -1.2,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(3.8, -1.3,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(4.2, -1.4,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(4.2, -1.5,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(4.6, -1.5,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(5, -1.6,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(5.4, -1.7,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(5.8, -1.8,-8), 0.3, refle ))
rtx.scene.append( Sphere(V3(6.2, -1.9,-8), 0.3, refle ))



# La mas grande
rtx.scene.append( Sphere(V3(-5.4,2.3,-8), 1.3, planeta) )



# Terminar
rtx.glRender()
rtx.glFinish('Proyecto#2.bmp')



