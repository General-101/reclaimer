from ...common_descs import *
from supyr_struct.defs.tag_def import TagDef

shader_pass = Struct("pass",
    ascii_str32("name"),
    BBool16("flags",
        "clear target",
        "copy scene to target",
        "clear buffer texture",
        ),
    BSEnum16("render chain",
        "main chain",
        "buffer chain"
        ),
    SIZE=48,
    )

technique = Struct("entry",
    ascii_str32("name"),
    BBool16("shader model",
        "sm 1.0",
        "sm 2.0",
        "sm 3.0",
        ),

    Pad(18),
    reflexive("shader pass", shader_pass),
    SIZE=64
    )

shpp_attrs = Struct("shpp",
    Pad(24),
    rawdata_ref("shader code binary", Rawdata, max_size=32768),

    Pad(64),
    reflexive("techniques", technique),
    reflexive("predicted resources", predicted_resource, 1024),
    SIZE=164
    )

shpp_body = Struct("tagdata", shpp_attrs)

def get():
    return shpp_def

shpp_def = TagDef("shpp",
    blam_header_os('shpp'),
    shpp_body,

    ext=".shader_postprocess", endian=">"
    )