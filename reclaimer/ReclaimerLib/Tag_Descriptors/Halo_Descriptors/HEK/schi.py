from .Common_Block_Structures import *
from supyr_struct.Defs.Tag_Def import Tag_Def
from .Objs.schi import SCHI_Tag

def Construct():
    return SCHI_Definition

class SCHI_Definition(Tag_Def):

    Ext = ".shader_transparent_chicago"

    Cls_ID = "schi"

    Tag_Obj = SCHI_Tag

    Endianness = ">"

    Tag_Structure = {TYPE:Container, GUI_NAME:"shader_transparent_chicago",
                     0:Combine( {1:{ DEFAULT:"schi" } }, Tag_Header),
                     
                     1:{TYPE:Struct, SIZE:108, GUI_NAME:"Data",
                        #Radiosity Properties
                        0:Radiosity_Block,
                        
                        #Shader TYPE
                        1:Material_Type,
                        2:Numeric_Shader_ID,
                        3:{ TYPE:SInt32, OFFSET:37, GUI_NAME:"Numeric Counter Limit"},#[0,255]
                        
                        # Shader Properties
                        4:{ TYPE:UInt8, OFFSET:41, GUI_NAME:"Chicago Shader Flags" ,
                             FLAGS:Transparent_Shader_Properties
                             },
                        5:{ TYPE:UInt16, OFFSET:42, GUI_NAME:"First Map Type" ,
                             ELEMENTS:Transparent_Shader_First_Map_Type
                             },
                        6:{ TYPE:UInt16, OFFSET:44, GUI_NAME:"Framebuffer Blend Function" ,
                             ELEMENTS:Framebuffer_Blend_Modes
                             },
                        7:{ TYPE:UInt16, OFFSET:46, GUI_NAME:"Framebuffer Fade Mode" ,
                             ELEMENTS:Transparent_Shader_Fade_Mode
                             },
                        8:{ TYPE:UInt16, OFFSET:48, GUI_NAME:"Framebuffer Fade Source" ,
                             ELEMENTS:Function_Outputs
                             },
                        
                        #Lens Flare
                        9:{ TYPE:Float, OFFSET:52, GUI_NAME:"Lens Flare Spacing"},#world units
                        10:{ TYPE:Struct, OFFSET:56, GUI_NAME:"Lens Flare" ,
                             ATTRIBUTES:Tag_Reference_Structure
                             },
                        
                        11:{ TYPE:Struct, OFFSET:72, GUI_NAME:"Extra Layers",
                             ATTRIBUTES:Block_Reference_Structure,
                             CHILD:{TYPE:Array, NAME:"Extra_Layers_Array",
                                    MAX:4, SIZE:".Block_Count",
                                    ARRAY_ELEMENT:Extra_Layers_Block
                                    }
                             },
                        12:{ TYPE:Struct, OFFSET:84, GUI_NAME:"Maps",
                             ATTRIBUTES:Block_Reference_Structure,
                             CHILD:{TYPE:Array, NAME:"Maps_Array",
                                    MAX:4, SIZE:".Block_Count",
                                    ARRAY_ELEMENT:Chicago_4_Stage_Maps
                                    }
                             },
                        13:{ TYPE:UInt16, OFFSET:98, GUI_NAME:"Extra Flags" ,
                             FLAGS:Chicago_Extra_Flags
                             }
                        }
                     }
