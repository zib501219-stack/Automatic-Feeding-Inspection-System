"""Detailed stepped-shaft automatic feeding and AI inspection cell.

Design target: 60 x 20 mm, 0.12 kg steel workpiece, 12 parts/minute.
"""
from math import cos, radians, sin
from build123d import Compound, Location
from engineering_primitives import *


def pneumatic_cylinder(parts, p, stroke, prefix, axis="x"):
    x,y,z=p
    if axis == "x":
        parts.extend([cx(24,90,p,prefix+"_barrel",LIGHT),cx(8,stroke,(x+45+stroke/2,y,z),prefix+"_rod",STEEL),bx(12,62,62,(x-45,y,z),prefix+"_rear_mount",DARK)])
    else:
        parts.extend([cy(24,90,p,prefix+"_barrel",LIGHT),cy(8,stroke,(x,y+45+stroke/2,z),prefix+"_rod",STEEL),bx(62,12,62,(x,y-45,z),prefix+"_rear_mount",DARK)])


def gen_step():
    p=[]
    # welded/aluminium frame and machine feet
    frame_rect(p,-700,700,-360,360,110,40,"machine_lower")
    frame_rect(p,-700,700,-360,360,760,40,"machine_upper")
    for i,(x,y) in enumerate(((-700,-360),(-700,360),(700,-360),(700,360)),1):
        p.extend([bx(40,40,650,(x,y,435),f"frame_leg_{i}",MID),cz(34,20,(x,y,78),f"leveling_foot_{i}",DARK)])
    p.extend([bx(1480,800,16,(0,0,785),"machine_table",LIGHT),bx(360,300,460,(500,220,330),"electrical_cabinet",LIGHT),bx(300,12,260,(500,65,380),"cabinet_door",MID)])
    # vibratory bowl with stepped shell and helical track blocks
    bowl=(-500,40,980)
    p.extend([cz(220,18,(bowl[0],bowl[1],800),"bowl_base_plate",DARK),cz(155,90,(bowl[0],bowl[1],880),"bowl_drive_base",MID),cz(205,20,(bowl[0],bowl[1],940),"bowl_lower_flange",ORANGE),cz(190,150,bowl,"bowl_body",ORANGE),cz(155,160,(bowl[0],bowl[1],1000),"bowl_inner_void_envelope",DARK)])
    for i in range(32):
        a=radians(i*26)
        r=168
        z=970+i*4.2
        p.append(bx(52,30,10,(bowl[0]+r*cos(a),bowl[1]+r*sin(a),z),f"spiral_track_segment_{i+1:02d}",STEEL))
    for i in range(8):
        a=radians(i*45)
        p.append(bx(10,38,80,(bowl[0]+185*cos(a),bowl[1]+185*sin(a),1010),f"bowl_wall_rib_{i+1}",ORANGE))
    # linear feeder rails and isolation station
    p.extend([
        bx(620,145,18,(-40,40,985),"linear_feeder_base",DARK),
        bx(620,12,42,(-40,-10,1015),"left_guide_rail",STEEL),
        bx(620,12,42,(-40,90,1015),"right_guide_rail",STEEL),
        bx(620,55,8,(-40,40,1000),"feeder_track",LIGHT),
        bx(180,180,18,(310,40,970),"separation_station_base",DARK),
        bx(22,110,100,(260,40,1040),"front_separator_gate",ORANGE),
        bx(22,110,100,(330,40,1040),"rear_separator_gate",ORANGE),
    ])
    pneumatic_cylinder(p,(270,-85,1040),65,"separator_cylinder_1","y")
    pneumatic_cylinder(p,(340,165,1040),65,"separator_cylinder_2","y")
    # workpiece train
    for i in range(10):
        p.extend([cx(10,60,(-270+i*55,40,1030),f"stepped_shaft_{i+1}_main",STEEL),cx(14,18,(-270+i*55,40,1030),f"stepped_shaft_{i+1}_shoulder",STEEL)])
    # transfer slide, V fixture, push cylinder
    p.extend([
        bx(480,240,20,(420,-160,880),"transfer_slide_base",DARK),
        bx(420,18,26,(420,-215,915),"linear_guide_left",STEEL),
        bx(420,18,26,(420,-105,915),"linear_guide_right",STEEL),
        bx(160,160,22,(390,-160,950),"inspection_carriage",LIGHT),
        bx(90,24,34,(390,-185,990),"v_block_left",ORANGE),
        bx(90,24,34,(390,-135,990),"v_block_right",ORANGE),
        bx(34,110,90,(310,-160,1005),"hard_stop_bracket",DARK),
    ])
    pneumatic_cylinder(p,(105,-160,950),170,"transfer_cylinder","x")
    pneumatic_cylinder(p,(540,-300,990),85,"eject_cylinder","y")
    # laser micrometer fork, cameras and lighting enclosure
    p.extend([
        bx(30,90,260,(420,-255,1110),"laser_micrometer_emitter_post",BLUE),
        bx(30,90,260,(420,-65,1110),"laser_micrometer_receiver_post",BLUE),
        bx(120,42,55,(420,-255,1245),"laser_emitter_head",DARK),
        bx(120,42,55,(420,-65,1245),"laser_receiver_head",DARK),
        bx(55,55,380,(225,-160,1190),"vision_left_post",MID),
        bx(55,55,380,(615,-160,1190),"vision_right_post",MID),
        bx(450,55,55,(420,-160,1360),"vision_crossbeam",MID),
        bx(72,66,62,(420,-160,1305),"ai_industrial_camera",DARK),
        cz(30,86,(420,-160,1240),"telecentric_lens",DARK),
        bx(320,180,15,(420,-160,1185),"backlight_panel",LIGHT),
        bx(430,10,360,(420,-270,1160),"inspection_guard_front",YELLOW),
        bx(430,10,360,(420,-50,1160),"inspection_guard_rear",YELLOW),
    ])
    # sensors, manifolds and cable chain
    for i,x in enumerate((-260,-120,20,160,300),1):
        p.extend([bx(24,36,24,(x,-15,1070),f"photo_sensor_{i}",DARK),bx(18,18,45,(x,-15,1038),f"sensor_bracket_{i}",STEEL)])
    p.extend([bx(260,80,140,(0,250,930),"pneumatic_manifold_box",BLUE),bx(240,12,110,(0,205,930),"manifold_cover",DARK)])
    for i in range(8):
        p.append(cx(7,60,(-90+i*25,215,940),f"solenoid_valve_{i+1}",LIGHT))
    cable_chain(p,(120,-245,900),(550,-245,900),20,"transfer_drag_chain",(18,26,10))
    # OK/NG chutes and bins
    p.extend([
        bx(340,150,20,(555,170,900),"ok_chute",GREEN),bx(340,150,20,(555,335,900),"ng_chute",RED),
        bx(280,210,140,(560,170,780),"ok_bin",GREEN),bx(280,210,140,(560,335,780),"ng_bin",RED),
    ])
    # front polycarbonate guarding, doors, interlocks and beacon
    for i,x in enumerate((-720,-240,240,720),1): p.append(bx(35,35,720,(x,-395,750),f"front_guard_post_{i}",YELLOW))
    p.extend([
        bx(450,10,640,(-480,-395,780),"left_polycarbonate_guard",BLUE),
        bx(450,10,640,(480,-395,780),"right_polycarbonate_guard",BLUE),
        bx(40,25,90,(-250,-410,950),"safety_door_interlock",RED),
        bx(170,60,120,(650,-390,1210),"operator_hmi",DARK),
        cz(18,22,(700,-390,1300),"emergency_stop",RED),
        bx(30,30,170,(670,310,1250),"beacon_post",DARK),
        cz(22,45,(670,310,1370),"beacon_red",RED),cz(22,45,(670,310,1325),"beacon_yellow",YELLOW),cz(22,45,(670,310,1280),"beacon_green",GREEN),
    ])
    return assembly(p,"stepped_shaft_feeding_ai_inspection_cell")

if __name__ == "__main__": pass
