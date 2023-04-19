import maya.cmds as cmds


if cmds.window('recenter', exists = True):
    cmds.deleteUI('recenter')

#defs

def recenter(*args):
    for obj in cmds.ls(sl=True):
        cmds.move(rpr=True)
       

def delete_history(*args):
    for obj in cmds.ls(sl=True):
        cmds.delete(ch=True)

def freeze_trans(*args):
    cmds.makeIdentity(apply=True,t=True, r=True, s=True, n=0, pn=True)
        
def center_pivot(*args):
    for obj in cmds.ls(sl=True):
        cmds.xform(cp=True)

def move_pivotX(*args):
    for obj in cmds.ls(sl=True):
        cmds.xform(piv=(1,0,0),r=True)

def move_pivotmX(*args):
    for obj in cmds.ls(sl=True):
        cmds.xform(piv=(-1,0,0),r=True)        

def move_pivotY(*args):
    for obj in cmds.ls(sl=True):
        cmds.xform(piv=(0,1,0),r=True)

def move_pivotmY(*args):
    for obj in cmds.ls(sl=True):
        cmds.xform(piv=(0,-1,0),r=True)

def move_pivotZ(*args):
    for obj in cmds.ls(sl=True):
        cmds.xform(piv=(0,0,1),r=True)

def move_pivotmZ(*args):
    for obj in cmds.ls(sl=True):
        cmds.xform(piv=(0,0,-1),r=True)
                      
#window
cmds.window('recenter', t = 'Recenter Tool', w=300, h=220, sizeable=False, mnb=True,mxb=True)
cmds.columnLayout(adj=True)

cmds.separator(h=10)
cmds.rowColumnLayout(nc=1)
cmds.button('Recenter Object', w=150, h=30,bgc=[0.2,0.2,0.2],hlc=[1,0,0], command=recenter)
cmds.setParent()

cmds.separator(h=10)
cmds.rowColumnLayout(nc=2)
cmds.button(w=150, h=20, l = 'Freeze Transforms', bgc=[0,0,0.5], command=freeze_trans)
cmds.button(w=150, h=20, l = 'Delete History', bgc=[0.5,0,0],command=delete_history)
cmds.setParent('..')
cmds.separator(h=10)

cmds.separator(h=10, style='none')
cmds.rowColumnLayout(nc=1,adj=1)
cmds.button(w=300,h=20, l= 'Center Pivot', bgc=[0,1,0.5],command=center_pivot)
cmds.setParent('..')
cmds.rowColumnLayout(nc=3)
cmds.button(w=100, h=20, l='X +1',c=move_pivotX, bgc=[0,0.3,0.3])
cmds.button(w=100, h=20, l='Y +1',c=move_pivotY, bgc=[0,0.5,0.5])
cmds.button(w=100, h=20, l='Z +1',c=move_pivotZ, bgc=[0,0.7,0.7])
cmds.button(w=100, h=20, l='X -1',c=move_pivotmX, bgc=[0,0.3,0.3])
cmds.button(w=100, h=20, l='Y -1',c=move_pivotmY, bgc=[0,0.5,0.5])
cmds.button(w=100, h=20, l='Z -1',c=move_pivotmZ, bgc=[0,0.7,0.7])
cmds.setParent('..')

cmds.separator(h=20)
cmds.rowColumnLayout(nc=1)
cmds.button(w=300,h=30, l='Export Selection', bgc=[0.9,0.9,0.9], c=cmds.ExportSelection)
cmds.setParent('..')

cmds.showWindow()