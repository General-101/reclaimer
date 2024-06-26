#
# This file is part of Reclaimer.
#
# For authors and copyright check AUTHORS.TXT
#
# Reclaimer is free software under the GNU General Public License v3.0.
# See LICENSE for more information.
#

from reclaimer.meta.wrappers.halo_reach_map import HaloReachMap

class HaloReachBetaMap(HaloReachMap):
    tag_defs_module = ""
    tag_classes_to_load = ()
    # NOTE: setting defs to None so setup_defs doesn't think the
    #       defs are setup cause of class property inheritance.
    defs = None