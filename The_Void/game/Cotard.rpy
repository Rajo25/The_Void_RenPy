transform scale_cotard:
    zoom 0.4

#image wyciete_swiatlo = AlphaMask("moje_swiatlo.png", "cotard_pose_normal.png")

layeredimage Cotard:
    at scale_cotard
    

    #body
    group body:
        attribute crossed_arms default:
            "Cotard/Body_Crossed_Arms.png"
        attribute Arm_Pocket:
            "Cotard/Body_Arm_Pocket.png"
        attribute Arm_On_Body:
            "Cotard/Body_Arm_On_Body.png"
        attribute Stress:
            "Cotard/Body_Stress.png"
  
    #face
    group face:
        attribute speak default:
            "Cotard/Head_N_Speak.png"
        attribute notspeak:
            "Cotard/Head_Speak.png"
        
   
    #eyes
    group eyes:
        attribute Lost:
            "Cotard/Eyes_Lost.png"
        attribute Angry:
            "Cotard/Eyes_Angry.png"
        attribute Bitch:
            "Cotard/Eyes_Bitch.png"
        attribute Crying:
            "Cotard/Eyes_Crying.png"
        attribute Happy:
            "Cotard/Eyes_Happy.png"
        attribute Pain:
            "Cotard/Eyes_Pain.png"
        attribute Pain_2:
            "Cotard/Eyes_Pain_2.png"
        attribute Small_Cry:
            "Cotard/Eyes_Small_Cry.png"
        attribute Very_Angry:
            "Cotard/Eyes_Very_Angry.png"

    group emotion:
        #emotion not sepak
        attribute Digust:
            "Cotard/Disgust.png"
        attribute Sad:
            "Cotard/Sad.png"
        attribute Smile:
            "Cotard/Smile.png"
        attribute Not_Happy:
            "Cotard/Not_Happy.png"

        #emotion sepak
        attribute Speak_Smile:
            "Cotard/Speak_Happy.png"
        attribute Speak_Not_Happy:
            "Cotard/Speak_Not_Happy.png"
        attribute Speak_Angry:
            "Cotard/Speak_Angry.png"



    #shader
    group shader:
        attribute night:
            night_sh
        attribute sunset:
            sunset_sh
        attribute day:
            day_sh
        attribute crystal:
            crystal_sh
  