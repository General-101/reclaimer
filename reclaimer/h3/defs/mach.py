from reclaimer.common_descs import *
from supyr_struct.defs.tag_def import TagDef

mach_ai_propertie_leap_jump_speed = (
    "none",
    "down",
    "step",
    "crouch",
    "stand",
    "storey",
    "tower",
    "infinite",
    )

mach_ai_propertie_size = (
    "default",
    "tiny",
    "small",
    "medium",
    "large",
    "huge",
    "immobile",
    )

mach_attachment_change_color = (
    "none",
    "primary",
    "secondary",
    "tertiary",
    "quaternary",
    )

mach_collision_response = (
    "pause_until_crushed",
    "reverse_directions",
    "discs",
    )

mach_lightmap_shadow_mode_size = (
    "default",
    "never",
    "always",
    "unknown",
    )

mach_multiplayer_object_propertie_object_type = (
    "ordinary",
    "weapon",
    "grenade",
    "projectile",
    "powerup",
    "equipment",
    "light_land_vehicle",
    "heavy_land_vehicle",
    "flying_vehicle",
    "teleporter_2way",
    "teleporter_sender",
    "teleporter_receiver",
    "player_spawn_location",
    "player_respawn_zone",
    "hold_spawn_objective",
    "capture_spawn_objective",
    "hold_destination_objective",
    "capture_destination_objective",
    "hill_objective",
    "infection_haven_objective",
    "territory_objective",
    "vip_boundary_objective",
    "vip_destination_objective",
    "juggernaut_destination_objective",
    )

mach_multiplayer_object_propertie_shape = (
    "none",
    "sphere",
    "cylinder",
    "box",
    )

mach_multiplayer_object_propertie_spawn_timer_mode = (
    "on_death",
    "on_disturbance",
    )

mach_object_type = (
    "biped",
    "vehicle",
    "weapon",
    "equipment",
    "terminal",
    "projectile",
    "scenery",
    "machine",
    "control",
    "sound_scenery",
    "crate",
    "creature",
    "giant",
    "effect_scenery",
    )

mach_pathfinding_policy = (
    "discs",
    "sectors",
    "cut_out",
    "none",
    )

mach_sweetener_size = (
    "small",
    "medium",
    "large",
    )

mach_type = (
    "door",
    "platform",
    "gear",
    )

mach_water_density = (
    "default",
    "least",
    "some",
    "equal",
    "more",
    "more_still",
    "lots_more",
    )


mach_early_mover_propertie = Struct("early_mover_properties",
    string_id_meta("name"),
    Pad(36),
    ENDIAN=">", SIZE=40
    )


mach_ai_propertie = Struct("ai_properties",
    Bool32("flags",
        "destroyable_cover",
        "pathfinding_ignore_when_dead",
        "dynamic_cover",
        ),
    string_id_meta("ai_type_name"),
    Pad(4),
    SEnum16("size", *mach_ai_propertie_size),
    SEnum16("leap_jump_speed", *mach_ai_propertie_leap_jump_speed),
    ENDIAN=">", SIZE=16
    )


mach_function = Struct("functions",
    Bool32("flags",
        "invert",
        "mapping_does_not_controls_active",
        "always_active",
        "random_time_offset",
        ),
    string_id_meta("import_name"),
    string_id_meta("export_name"),
    string_id_meta("turn_off_with"),
    Float("minimum_value"),
    rawdata_ref("default_function"),
    string_id_meta("scale_by"),
    ENDIAN=">", SIZE=44
    )


mach_attachment = Struct("attachments",
    dependency("attachment"),
    string_id_meta("marker"),
    SEnum16("change_color", *mach_attachment_change_color),
    SInt16("unknown"),
    string_id_meta("primary_scale"),
    string_id_meta("secondary_scale"),
    ENDIAN=">", SIZE=32
    )


mach_widget = Struct("widgets",
    dependency("type"),
    ENDIAN=">", SIZE=16
    )


mach_change_color_initial_permutation = Struct("initial_permutations",
    Pad(4),
    color_rgb_float("color_lower_bound"),
    color_rgb_float("color_upper_bound"),
    string_id_meta("variant_name"),
    ENDIAN=">", SIZE=32
    )


mach_change_color_function = Struct("functions",
    Bool32("scale_flags",
        "blend_in_hsv",
        "more_colors",
        ),
    color_rgb_float("color_lower_bound"),
    color_rgb_float("color_upper_bound"),
    string_id_meta("darken_by"),
    string_id_meta("scale_by"),
    ENDIAN=">", SIZE=32
    )


mach_change_color = Struct("change_colors",
    reflexive("initial_permutations", mach_change_color_initial_permutation),
    reflexive("functions", mach_change_color_function),
    ENDIAN=">", SIZE=24
    )


mach_predicted_resource = Struct("predicted_resources",
    SInt16("type"),
    SInt16("resource_index"),
    UInt32("tag_index"),
    ENDIAN=">", SIZE=8
    )


mach_multiplayer_object_propertie = Struct("multiplayer_object_properties",
    Bool16("engine_flags",
        "capture_the_flag",
        "slayer",
        "oddball",
        "king_of_the_hill",
        "juggernaut",
        "territories",
        "assault",
        "vip",
        "infection",
        ),
    SEnum8("object_type", *mach_multiplayer_object_propertie_object_type),
    Bool8("teleporter_flags",
        "disallows_players",
        "allows_land_vehicles",
        "allows_heavy_vehicles",
        "allows_flying_vehicles",
        "allows_projectiles",
        ),
    Bool16("flags",
        "editor_only",
        ),
    SEnum8("shape", *mach_multiplayer_object_propertie_shape),
    SEnum8("spawn_timer_mode", *mach_multiplayer_object_propertie_spawn_timer_mode),
    SInt16("spawn_time"),
    SInt16("abandon_time"),
    Float("radius_width"),
    Float("length"),
    Float("top"),
    Float("bottom"),
    Float("unknown"),
    Float("unknown_1"),
    Float("unknown_2"),
    SInt32("unknown_3"),
    SInt32("unknown_4"),
    dependency("child_object"),
    SInt32("unknown_5"),
    dependency("shape_shader"),
    dependency("unknown_shader"),
    dependency("unknown_6"),
    dependency("unknown_7"),
    dependency("unknown_8"),
    dependency("unknown_9"),
    dependency("unknown_10"),
    dependency("unknown_11"),
    ENDIAN=">", SIZE=196
    )


mach_meta_def = BlockDef("mach",
    SEnum16("object_type", *mach_object_type),
    Bool16("flags",
        "does_not_cast_shadow",
        "search_cardinal_direction_lightmaps",
        ("not_a_pathfinding_obstacle", 1 << 3),
        "extension_of_parent",
        "does_not_cause_collision_damage",
        "early_mover",
        "early_mover_localized_physics",
        "use_static_massive_lightmap_sample",
        "object_scales_attachments",
        "inherits_player_s_appearance",
        "dead_bipeds_can_t_localize",
        "attach_to_clusters_by_dynamic_sphere",
        "effects_created_by_this_object_do_not_spawn_objects_in_multiplayer",
        ),
    Float("bounding_radius"),
    Float("bounding_offset_x"),
    Float("bounding_offset_y"),
    Float("bounding_offset_z"),
    Float("acceleration_scale"),
    SEnum16("lightmap_shadow_mode_size", *mach_lightmap_shadow_mode_size),
    SEnum8("sweetener_size", *mach_sweetener_size),
    SEnum8("water_density", *mach_water_density),
    SInt32("unknown"),
    Float("dynamic_light_sphere_radius"),
    Float("dynamic_light_sphere_offset_x"),
    Float("dynamic_light_sphere_offset_y"),
    Float("dynamic_light_sphere_offset_z"),
    string_id_meta("default_model_variant"),
    dependency("model"),
    dependency("crate_object"),
    dependency("collision_damage"),
    reflexive("early_mover_properties", mach_early_mover_propertie),
    dependency("creation_effect"),
    dependency("material_effects"),
    dependency("melee_impact"),
    reflexive("ai_properties", mach_ai_propertie),
    reflexive("functions", mach_function),
    SInt16("hud_text_message_index"),
    SInt16("unknown_1"),
    reflexive("attachments", mach_attachment),
    reflexive("widgets", mach_widget),
    reflexive("change_colors", mach_change_color),
    reflexive("predicted_resources", mach_predicted_resource),
    reflexive("multiplayer_object_properties", mach_multiplayer_object_propertie),
    Bool32("flags_1",
        "position_loops",
        ("position_interpolation", 1 << 2),
        ),
    Float("power_transition_time"),
    Float("power_acceleration_time"),
    Float("position_transition_time"),
    Float("position_acceleration_time"),
    Float("depowered_position_transition_time"),
    Float("depowered_position_acceleration_time"),
    Bool32("lightmap_flags",
        "don_t_use_in_lightmap",
        "don_t_use_in_lightprobe",
        ),
    dependency("open_up"),
    dependency("close_down"),
    dependency("opened"),
    dependency("closed"),
    dependency("depowered"),
    dependency("repowered"),
    Float("delay_time"),
    dependency("delay_effect"),
    Float("automatic_activation_radius"),
    SEnum16("type", *mach_type),
    Bool16("flags_2",
        "pathfinding_obstacle",
        "but_not_when_open",
        "elevator",
        ),
    Float("door_open_time"),
    Float("occlusion_bounds_min"),
    Float("occlusion_bounds_max"),
    SEnum16("collision_response", *mach_collision_response),
    SInt16("elevator_node"),
    SEnum16("pathfinding_policy", *mach_pathfinding_policy),
    SInt16("unknown_2"),
    TYPE=Struct, ENDIAN=">", SIZE=424
    )