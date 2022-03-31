
def VS(Name, Inc, Value):
    '''
    These will be the inputs for VS
    
    Spatial Frequency 
    Temperoal Frequency 
    Time before Stimulation
    Duration of Stimulation
    Time After Stimulation
    Pixel length of Window
    Pixel Hight of Window
    Synch status
    
    VS will increase ir decrease the value of the chosen parameter
    '''
    if Inc == 1: #if inc == 1 then increase the following
        if Name == "Spatial Frequency":
            Value = Value + 0.01
            return Value
        elif Name == "Temporal Frequency":
            Value = Value + 0.1
            return Value
        elif Name == "Time before Stimulation":
            Value = Value + 0.5
            return Value
        elif Name == "Duration of Stimulation":
            Value = Value + 0.1
            return Value
        elif Name == "Time After Stimulation":
            Value = Value + 0.5
            return Value
        elif Name == "Pixel Length of Window":
            Value = Value + 10
            return Value
        elif Name == "Pixel Height of Window":
            Value = Value + 10
            return Value
        elif Name == "syncStat":
            Value = True
            return Value
        elif Name == "Motionmode":
            return 0
    
    elif Inc == 0: #if inc == 0 then decrease the following
        if Name == "Spatial Frequency":
            Value = Value - 0.01
            return Value
        elif Name == "Temporal Frequency":
            Value = Value - 0.1
            return Value
        elif Name == "Time before Stimulation":
            Value = Value - 0.5
            return Value
        elif Name == "Duration of Stimulation":
            Value = Value - 0.1
            return Value
        elif Name == "Time After Stimulation":
            Value = Value - 0.5
            return Value
        elif Name == "Pixel Length of Window":
            Value = Value - 10
            return Value
        elif Name == "Pixel Height of Window":
            Value = Value - 10
            return Value
        elif Name == "syncStat":
            Value = False
            return Value
        elif Name == "Motionmode":
            return 1
