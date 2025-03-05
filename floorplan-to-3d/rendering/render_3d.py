from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

floor_plan_data = []

def render_floor_plan(data):
    global floor_plan_data
    floor_plan_data = data

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Floor Plan")
    glEnable(GL_DEPTH_TEST)
    
    glutDisplayFunc(draw_floor_plan)
    glutMainLoop()

def draw_floor_plan():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, 1.33, 0.1, 50.0)
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

    for obj in floor_plan_data:
        if obj["type"] == "wall":
            draw_wall(*obj["coords"])

    glFlush()

def draw_wall(x1, y1, x2, y2):
    glBegin(GL_QUADS)
    glVertex3f(x1 / 100, 0, y1 / 100)
    glVertex3f(x2 / 100, 0, y2 / 100)
    glVertex3f(x2 / 100, 3, y2 / 100)  # Wall height: 3
    glVertex3f(x1 / 100, 3, y1 / 100)
    glEnd()
