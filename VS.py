
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
    Motion mode
    
    VS will increase ir decrease the value of the chosen parameter
    '''
    
    if Inc == 1: #if inc == 1 then increase the following
        if Name == "Spatial Frequency" or Name =="Spatial FrequencyORI" or Name =="Spatial FrequencyB":
            Value = Value + 0.01
            return Value
        elif Name == "Temporal Frequency" or Name =="Temporal FrequencyORI" or Name =="Temporal FrequencyB" :
            Value = Value + 0.1
            return Value
        elif Name == "Time before Stimulation" or Name =="Time before StimulationORI" or Name =="Time before StimulationB":
            Value = Value + 500
            return Value
        elif Name == "Duration of Stimulation" or Name =="Duration of StimulationORI" or Name =="Duration of StimulationB":
            Value = Value + 500
            return Value
        elif Name == "Time After Stimulation" or Name =="Time After StimulationORI" or Name =="Time After StimulationB" :
            Value = Value + 500
            return Value
        elif Name == "Pixel Length of Window" or Name =="Pixel Length of WindowORI" or Name =="Pixel Length of WindowB" :
            Value = Value + 10
            return Value
        elif Name == "Pixel Height of Window" or Name =="Pixel Height of WindowORI" or Name =="Pixel Height of WindowB":
            Value = Value + 10
            return Value
        elif Name == "syncStat" or Name =="syncStatORI" or Name =="syncStatB":  
            Value = True
            return Value
        elif Name == "Motionmode" or Name =="MotionmodeB" or Name =="MotionmodeORI":
            return 0
        elif Name == "Ledstate":
            Value = Value + 1
            return Value
        elif Name == "Rep":
            Value = Value + 5
            return Value
        elif Name == "Tuning feature: ":
            if Value < 4:
                Value += 1
            else: 
                Value = 0
            return Value

    
    elif Inc == 0: #if inc == 0 then decrease the following
        if Name == "Spatial Frequency" or Name =="Spatial FrequencyB" or Name =="Spatial FrequencyORI":
            Value = Value - 0.01
            return Value
        elif Name == "Temporal Frequency" or Name =="Temporal FrequencyB" or Name =="Temporal FrequencyORI":
            Value = Value - 0.1
            return Value
        elif Name == "Time before Stimulation" or Name =="Time before StimulationB" or Name =="Time before StimulationORI":
            Value = Value - 500
            return Value
        elif Name == "Duration of Stimulation" or Name =="Duration of StimulationB" or Name =="Duration of StimulationORI":
            Value = Value - 500
            return Value
        elif Name == "Time After Stimulation" or Name =="Time After StimulationB" or Name =="Time After StimulationORI":
            Value = Value - 500
            return Value
        elif Name == "Pixel Length of Window" or Name =="Pixel Length of WindowB" or Name =="Pixel Length of WindowORI":
            Value = Value - 10
            return Value
        elif Name == "Pixel Height of Window" or Name =="Pixel Height of WindowB" or Name =="Pixel Height of WindowORI":
            Value = Value - 10
            return Value
        elif Name == "syncStat" or Name =="syncStatB" or Name =="syncStatORI":
            Value = False
            return Value
        elif Name == "Motionmode" or Name =="MotionmodeB" or Name =="MotionmodeORI" or Name =="randomseq":
            return 1
        elif Name == "Ledstate" :
            Value = Value - 1
            return Value
        elif Name == "Rep":
            Value = Value - 5
            return Value
        elif Name == "Tuning feature: ":
            if Value > 0:
                Value -= 1
            else: 
                Value = 4
            return Value