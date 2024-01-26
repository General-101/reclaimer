#
# This file is part of Reclaimer.
#
# For authors and copyright check AUTHORS.TXT
#
# Reclaimer is free software under the GNU General Public License v3.0.
# See LICENSE for more information.
#

from ...hek.defs.actr import *
from ..common_descs import *
from supyr_struct.util import desc_variant

panic = desc_variant(panic,
    ("leader_type", SEnum16("leader_type", *actor_types))
    )

actr_body = desc_variant(actr_body,
    ("type", SEnum16("type", *actor_types)),
    ("panic", panic)
    )


def get():
    return actr_def

actr_def = TagDef("actr",
    blam_header_stubbs('actr', 2),
    actr_body,

    ext=".actor", endian=">", tag_cls=ActrTag
    )
