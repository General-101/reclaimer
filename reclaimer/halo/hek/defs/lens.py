from ...common_descs import *
from supyr_struct.defs.tag_def import TagDef

reflection = Struct("reflection",
    BBool16("flags",
        "align rotation with screen center",
        "radius not scaled by distance",
        "radius scaled by occlusion factor",
        "occluded by solid objects",
        ),
    Pad(2),
    BSInt16("bitmap index"),
    Pad(22),
    BFloat("position"), # along flare axis
    BFloat("rotation offset"), # degrees
    Pad(4),
    QStruct("radius", INCLUDE=from_to),  # world units
    BSEnum16("radius scaled by",
        "none",
        "rotation",
        "rotation and strafing",
        "distance from center",
        ),
    Pad(2),
    QStruct("brightness", INCLUDE=from_to),  # world units
    BSEnum16("brightness scaled by",
        "none",
        "rotation",
        "rotation and strafing",
        "distance from center",
        ),
    Pad(2),

    #Tint color
    QStruct("tint color", INCLUDE=argb_float),

    #Animation
    Struct("animation",
        QStruct("color lower bound", INCLUDE=argb_float),
        QStruct("color upper bound", INCLUDE=argb_float),
        BBool16("flags", *blend_flags),
        BSEnum16("function", *animation_functions),
        BFloat("period"),  # seconds
        BFloat("phase"),  # seconds
        ),

    SIZE=128
    )


lens_body = Struct("tagdata",
    BFloat("falloff angle"),  # radians
    BFloat("cutoff angle"),  # radians
    FlFloat("unknown1", DEFAULT=1.0),
    FlFloat("unknown2", DEFAULT=1.0),
    BFloat("occlusion radius"),
    BSEnum16("occlusion offset direction",
        "toward viewer",
        "marker forward",
        "none",
        ),
    Pad(2),
    BFloat("near fade distance"),
    BFloat("far fade distance"),
    dependency("bitmap", valid_bitmaps),
    BBool16("flags",
        "sun",
        ),
    Pad(78),

    BSEnum16("rotation function",
        "none",
        "rotation a",
        "rotation b",
        "rotation translation",
        "translation",
        ),
    Pad(2),
    BFloat("rotation function scale"),  # radians
    Pad(24),
    BFloat("horizontal scale"),
    BFloat("vertical scale"),
    Pad(28),

    reflexive("reflections", reflection, 32),

    SIZE=240,
    )

    
def get():
    return lens_def

lens_def = TagDef("lens",
    blam_header("lens", 2),
    lens_body,

    ext=".lens_flare", endian=">",
    )
