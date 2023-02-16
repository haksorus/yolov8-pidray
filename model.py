from ultralytics import YOLO

def get_yolov8(path):
    
    model = YOLO(path, type="v8")
    
    # Correct class-name setting (if dataset was wrong converted)
    
    model.names[0] = "baton"
    model.names[1] = "pliers"
    model.names[2] = "hammer"
    model.names[3] = "powerbank"
    model.names[4] = "scissors"
    model.names[5] = "wrench"
    model.names[6] = "gun"
    model.names[7] = "bullet"
    model.names[8] = "sprayer"
    model.names[9] = "handcuffs"
    model.names[10] = "knife"
    model.names[11] = "lighter"
    
    
    return model

