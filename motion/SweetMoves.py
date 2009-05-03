
#constants file to store all our sweet ass-moves for the Nao
#import MotionConstants


def getMoveTime(move):
    totalTime = 0.0
    for target in move:
        if len(target) == 6:
            totalTime += target[4]
        elif len(target) == 3:
            totalTime += target[1]
    return totalTime

OFF = None #OFF means the joint chain doesnt get enqueued during this motion


INITIAL_POS = (((80.,40.,-50.,-70.),(0.,0.,-50.,100.,-50.,0.),(0.,0.,-50.,100.,-50.,0.),(80.,-40.,50.,70.),4.0,1),)

#Angles measured pretty exactly from the robot w/gains off.
#might want to make them even different if we suspect the motors are weakening
SIT_POS = (((0.,90.,0.,0.),
            (0.,0.,-55.,125.7,-75.7,0.),
            (0.,0.,-55.,125.7,-75.7,0.),
            (0.,-90.,0.,0.),3.0,1),
           ((90.,0.,-65.,-57.),
            (0.,0.,-55.,125.7,-75.7,0.),
            (0.,0.,-55.,125.7,-75.7,0.),
            (90.,0.,65.,57.),1.5,1))

ZERO_POS = (((0.,0.,0.,0.),(0.,0.,0.,0.,0.,0.),(0.,0.,0.,0.,0.,0.),(0.,0.,0.,0.),4.0,1),)
PENALIZED_POS = INITIAL_POS

SET_POS = INITIAL_POS

READY_POS = INITIAL_POS

ZERO_HEADS = (((0.0,0.0),1.0,1),)

NEUT_HEADS = (((0.,20.),2.0,1),)

PENALIZED_HEADS = (((0.0,25.0),0.5,1),)

FIND_BALL_HEADS_LEFT = (((45.,-10.),0.8,1),
                        ((45.,20.),0.3,1))

FIND_BALL_HEADS_RIGHT =  (((-45.,-10.),0.8,1),
                          ((-45.,200.),0.3,1))
#KICKS

KICK_STRAIGHT_LEFT = (
    #Stand up more fully
    ((80.,40.,-50.,-70.),
     (0.,0.,-10.,20.,-10.,0.),
     (0.,0.,-10.,20.,-10.,0.),
     (80.,-40.,50.,70.),2.0,1),
    #swing to the right
    ((80.,40.,-50.,-70.),
     (0.,20.,-10.,20.,-10.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1),
    #lift the left leg
    ((80.,40.,-50.,-70.),
     (0.,20.,-30.,60.,-30.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1),
    #kick the left leg
    ((80.,40.,-50.,-70.),
     (0.,20.,-55.,60.,-5.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),.08,1),
    #unkick the left leg
    ((80.,40.,-50.,-70.),
     (0.,20.,-30.,60.,-30.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),.08,1),
    #put the left leg back down the middle
    ((80.,40.,-50.,-70.),
     (0.,20.,-10.,20.,-10.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1))

STAND_FOR_KICK_LEFT = (
    ((80.,40.,-50.,-70.),
     (0.,0.,-10.,20.,-10.,0.),
     (0.,0.,-10.,20.,-10.,0.),
     (80.,-40.,50.,70.),2.0,1),
    #swing to the right
    ((80.,40.,-50.,-70.),
     (0.,20.,-10.,20.,-10.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1) )

# NEEDS 0.4 value for right leg
LEFT_FAR_KICK = (
    #swing to the right
    ((80.,40.,-50.,-70.),
     (0.,0.,-15.,20.,-10.,0.),
     (0.,0.,-15.,20.,-10.,0.),
     (80.,-40.,50.,70.),1.0,1),
    ((80.,40.,-50.,-70.),
     (0.,15.,-10.,20.,-10.,-20.),
     (0.,15.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),0.5,1),
    # Lift leg leg
    ((80.,40.,-50.,-70.),
     (0.,15.,-45.,85.,-40.,-20.),
     (0.,15.,-12.,16.,-10.,-20.),
     (80.,-40.,50.,70.),0.5,1),
    # kick left leg
    ((80.,40.,-50.,-70.),
     (0.,15.,-60.,41.,-8.,-20.),
     (0.,15.,-10.,30.,-10.,-20.),
     (80.,-40.,50.,70.),0.11,1),
    # unkick foot
    ((80.,40.,-50.,-70.),
     (0.,15.,-45.,85.,-40.,-10.),
     (0.,15.,-12.,16.,-10.,-20.),
     (80.,-40.,50.,70.),0.2,1),
    # put foot down
    ((80.,40.,-50.,-70.),
     (0.,15.,-10.,20.,-10.,-10.),
     (0.,15.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1),
    #swing to normal
    ((80.,40.,-50.,-70.),
     (0.,15.,-10.,20.,-10.,-20.),
     (0.,15.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1),
    ((80.,40.,-50.,-70.),
     (0.,0.,-15.,20.,-10.,0.),
     (0.,0.,-15.,20.,-10.,0.),
     (80.,-40.,50.,70.),1.0,1)
    )



KICK_STRAIGHT_LEFT_FAR = (
    #Stand up more fully
    ((80.,40.,-50.,-70.),
     (0.,0.,-10.,20.,-10.,0.),
     (0.,0.,-10.,20.,-10.,0.),
     (80.,-40.,50.,70.),1.0,1),
    #swing to the right
    ((80.,40.,-50.,-70.),
     (0.,20.,-10.,20.,-10.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),1.0,1),
    #lift the left leg
    ((80.,40.,-50.,-70.),
     (0.,20.,-30.,60.,-30.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),1.0,1),
    #cock the left leg back
    ((30.,40.,-50.,-70.),
     (0.,25.,-10.,70.,-50.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (30.,-40.,50.,70.),0.8,1),
#     #kick the left leg
#     ((90.,40.,-50.,-70.),
#      (0.,25.,-0.,20.,45.,-10.),
#      (0.,20.,-10.,20.,-10.,-20.),
#      (90.,-40.,50.,70.),0.7,1),
    #follow through with the left leg
    ((95.,40.,-50.,-70.),
     (0.,25.,-75.,20.,45.,-10.),
     (0.,20.,-10.,20.,-10.0,-20.),
     (95.,-40.,50.,70.),.4,1),
    #unkick the left leg
    ((95.,40.,-50.,-70.),
     (0.,20.,-30.,60.,-30.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (95.,-40.,50.,70.),2.0,1),
    #put the left leg back down the middle
    ((95.,40.,-50.,-70.),
     (0.,20.,-10.,20.,-10.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (95.,-40.,50.,70.),2.0,1),
    # go back to stood straight up
    ((80.,40.,-50.,-70.),
     (0.,0.,-10.,20.,-10.,0.),
     (0.,0.,-10.,20.,-10.,0.),
     (80.,-40.,50.,70.),1.0,1) )


NEW_KICK = (
    ((80.,40.,-50.,-70.),
     (0.,0.,-10.,20.,-10.,0.),
     (0.,0.,-10.,20.,-10.,0.),
     (80.,-40.,50.,70.),2.0,1),
    #swing to the right
    ((80.,40.,-50.,-70.),
     (0.,20.,-10.,20.,-10.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1),

    (( 79.4 , 38.31 , -50.7 , -71.1 ),
     ( -5.09 , 20.04 , 17.58 , 29.84 , -42.35 , -18.19 ),
     ( -5.09 , 20.21 , -9.4 , 20.30 , -10.28 , -20.12 ),
     ( 77.96 , -39.02 , 50.44 , 69.70 ),0.4,1 ),

    (( 79.45 , 38.40 , -50.71 , -71.18 ),
     ( -2.72 , 19.42 , -19.24 , 58.3 , -39.34 , -19.15 ),
     ( -2.72 , 20.74 , -10.02 , 20.39 , -10.3688192368 , -19.9490184784 ),
     ( 77.9 , -39.02 , 50.44 , 69.70 ),0.2,1),

    (( 79.45 , 38.40 , -50.71 , -71.18 ),
     ( 3.51 , 20.39 , -50.71 , 40 , 0.12 , -20.2 ),
     ( 3.51 , 20.56 , -9.40 , 19.86 , -11.2 , -20.03 ),
     ( 77.96 , -39.02 , 50.44 , 69.6 ),0.15,1),

    (( 79.45 , 38.40 , -50.71 , -71.18 ),
     ( 3.51 , 20.39 , -50.71 , 40 , 0.12 , -20.2 ),
     ( 3.51 , 20.56 , -9.40 , 19.86 , -11.2 , -20.03 ),
     ( 77.96 , -39.02 , 50.44 , 69.6 ),0.15,1),
    #swing to the right
    ((80.,40.,-50.,-70.),
     (0.,20.,-10.,20.,-10.,-20.),
     (0.,20.,-10.,20.,-10.,-20.),
     (80.,-40.,50.,70.),2.0,1),
    ((80.,40.,-50.,-70.),
     (0.,0.,-10.,20.,-10.,0.),
     (0.,0.,-10.,20.,-10.,0.),
     (80.,-40.,50.,70.),2.0,1)
    )




#HEAD SCANS

LOC_PANS = (
    (( 65.0, 10.0),1.5, 1),
    ((65.,-25.),1.0,  1),
    ((-65.,-25.),2.5, 1),
    ((-65.0, 10.0) ,1., 1),
    (( 0.0, 10.0),1.5,  1),)

QUICK_PANS = (
    ((  0.0,-40.0),.3,  1),
    (( 30.0,-25.0),.3,  1),
    (( 65.0,-25.0),.4,  1),
    (( 30.0,-25.0),.4,  1),
    ((  0.0,-40.0),.3,  1),
    ((-30.0,-25.0),.3,  1),
    ((-65.0,-25.0),.4,  1),
    ((-30.0,-25.0),.4,  1))

SCAN_BALL= (
    (( 65.0, 20.0),0.7, 1),
    ((65.,-5.),0.3,  1),
    ((-65.,-5.),1.4, 1),
    ((-65.,-30.),0.3,  1),
    ((65.,-30.),1.4, 1),
    ((65.0, -5.0) ,0.3, 1),
    (( -65.0, -5.0),1.3,  1),
    (( -65.0, 20.0),0.3,  1),
    (( 0.0, 20.0),0.7,  1),)

POST_SCAN = (
    ((65.,-25.),2.0,  1),
    ((-65.,-25.),2.0, 1))

PAN_LEFT = (
    (( 65.0, -25.0),1.0, 1),
    ((0.0,-25.),1.0,1))
PAN_RIGHT = (
    (( -65.0, -25.0),1.0, 1),
    ((0.0,-25.),1.0,1))

KICK_SCAN = (
    ((0.0,-25),0.25, 1),
    ((65.,-25.),1.0,  1),
    ((-65.,-25.),1.0, 1))


# STAND UPS
STAND_UP_FRONT = ( ((90,50,0,0),
                    (0,8,0,120,-65,0),
                    (0,0,8,120,-65,4),
                    (90,-50,0,0 ),1.0,1 ),

                   ((90,90,0,0),
                    (0,8,0,120,-65,0),
                    (0,0,8,120,-65,4),
                    (90,-90,0,0 ),1.0,1 ),

                   ((-90,90,0,0),
                    (0,8,0,120,-65,0),
                    (0,0,8,120,-65,4),
                    (-90,-90,0,0 ),0.5,1 ),

                   ((-90,0,0,0),
                    (0,8,0,120,-65,0),
                    (0,0,8,120,-65,4),
                    (-90,0,0,0 ),0.75,1 ),

                   ((-90,0,-90,0),
                    (0,8,0,120,-65,0),
                    (0,0,8,120,-65,4),
                    (-90,0,90,0 ),0.3,1 ),

                   ((-50,0,-90,-35),
                    (5,8,-90,120,-65,0),
                    (5,0,-90,120,-65,4),
                    (-50,0,90,35),2.0,1),

                   ((-10,0,-90,-95),
                    (-50,8,-90,60,-44,-39),
                    (-50,0,-90,60,-44,39),
                    (-10,0,90,95),1.3,1),

                   ((0,0,-90,-8),
                    (-50,8,-90,58,5,-31),
                    (-50,0,-90,58,5,31),
                    (0,0,90,8),1.7,1),

                   ((35,2,-14,-41),
                    (-55,5,-90,123,-17,-17),
                    (-55,-5,-90,123,-17,17),
                    (35,2,14,41),0.8, 1),

                   ((64,7,-53,-74),
                    (-45,6,-61,124,-41,-6),
                    (-45,-6,-61,124,-41,6),
                    (64,-7,53,74),1.2, 1),

                   ((93,10,-90,-80),
                    (0,0,-60,120,-60,0),
                    (0,0,-60,120,-60,0),
                    (93,-10,90,80),1.0,1),

                   ( INITIAL_POS[0][0],
                     INITIAL_POS[0][1],
                     INITIAL_POS[0][2],
                     INITIAL_POS[0][3],0.5,1))

STAND_UP_BACK = ( ((0,90,0,0),
                   (0,0,0,0,0,0),
                   (0,0,0,0,0,0),
                   (0,-90,0,0),1.0,1),

                  ((120,46,9,0),
                   (0,8,10,96,14,0),
                   (0,0,10,96,14,4),
                   (120,-46,-9,0), 1.0, 1),

                  ((120,25,10,-95),
                   (-2,8,0,70,18,0),
                   (-2,0,0,70,18,4),
                   (120,-25,-10,95),0.7,1),

                  ((120,22,15,-30),
                   (-38,8,-90,96,14,0),
                   (-38, 0,-90, 96, 14, 4),
                   ( 120,-22,-15, 30), 0.7, 1),


                  ((120,0,5,0),
                   (-38,31,-90,96,45,0),
                   (-38,-31,-90,96,45,4),
                   (120,0,-5,0), 1.0,1),

                  ((40,60,4,-28),
                   (-28,8,-49,126,-32,-22),
                   (-28,-31,-87,70,45,0),
                   (120,-33,-4,4),1.0,1 ),

                  ((42,28,5,-47),
                   (-49,-16,22,101,-70,-5),
                   (-49,-32,-89,61,39,-7),
                   (101,-15,-4,3),0.9,1 ),

                  ((42,28,4,-46),
                   (-23,11,-49,126,-70,6),
                   (-23,-17,-51,50,23,38),
                   (51,-50,0,26), 1.0,1),

                  ((42,28,4,-46),
                   (-23,21,-47,126,-70,5),
                   (-23,-1,-51,101,-33,15),
                   (51,-39,0,32), 0.5,1),

                  ((98,2,-72,-65),
                   (0,0,-50,120,-70,0),
                   (0,0,-50,120,-70,0),
                   (98,-2,72,65), 1.1,1),

                  ( INITIAL_POS[0][0],
                    INITIAL_POS[0][1],
                    INITIAL_POS[0][2],
                    INITIAL_POS[0][3],0.5,1))
