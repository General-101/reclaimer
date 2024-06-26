#
# This file is part of Reclaimer.
#
# For authors and copyright check AUTHORS.TXT
#
# Reclaimer is free software under the GNU General Public License v3.0.
# See LICENSE for more information.
#

from ...hek.defs.shdr import *
from ..common_descs import *

shdr_attrs  = desc_variant(shdr_attrs, SEnum16("material_type", *materials_list))
shader_body = Struct("tagdata",
    shdr_attrs,
    SIZE=40
    )

def get():
    return shdr_def

shdr_def = TagDef("shdr",
    blam_header_stubbs('shdr'),
    shader_body,

    ext=".shader", endian=">", tag_cls=ShdrTag
    )
