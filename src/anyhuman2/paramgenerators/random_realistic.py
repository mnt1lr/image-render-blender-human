# <LICENSE id="GPL-3.0">
#
#   Image-Render Blender Human add-on module
#   Copyright (C) 2022 Robert Bosch GmbH and its subsidiaries
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
# </LICENSE>
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# -----
# Copyright (c) 2022 Robert Bosch GmbH and its subsidiaries.
# All rights reserved.
# -----
###
from .GeneralRandomParameters import GeneralRandomParameters


############################################################################################
def RealisticRandomizeParams(params, generator_config, rnd):
    """
    Create a set of completely random realistic parameters for human generation.
    This randomizer is intended for the generation of visually
    plausible humans.

    The config dict can contain:
    - 'gender': either 'male' or 'female'

    If gender is not given, it will be selected randomly.


    Parameters
    ----------
    params : dict
        set of parameters controlling the randomization. E.g.
                {
                    "sId": "Armature.002",
                    "sMode": "RANDOM_REALISTIC",
                    "mParamConfig": {"sGender": "male"},
                }
    generator_config: dict
        set of all available parameters in HumGenV4

    Returns
    -------
    dict
        Dictionary of parameters for human generator
    """
    
    universal_params = GeneralRandomParameters(params, generator_config, rnd)
    dPreset = universal_params.GetPreset()
    sArmatureName = universal_params.ArmatureName()
    Male, dFaceHair, dBeardLength, sRegularHair, sEyebrows = universal_params.RandomizeHair()
    sGender = universal_params.GetGender()
    height_150, height_200, height = universal_params.RandomizeHeight()
    outfit = universal_params.RandomizeOutfit()
    sFootwear = universal_params.RandomFootwear()
    sSkinTexture = universal_params.RandomizeSkin()
    # HumGenV4 Config
    NewHumGenV4Config = dPreset
    # Skin
    NewHumGenV4Config["skin"]["tone"] =  rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["redness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["saturation"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["normal_strength"] = rnd.randint(1, 2)
    NewHumGenV4Config["skin"]["roughness_multiplier"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["freckles"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["splotches"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["texture.set"] = sSkinTexture
    NewHumGenV4Config["skin"]["cavity_strength"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["gender_specific"]["mustache_shadow"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["skin"]["gender_specific"]["beard_shadow"] =  rnd.uniform(0, 1.0)
    # Eyes
    NewHumGenV4Config["eyes"]["pupil_color"] = [rnd.uniform(0, 1.0), rnd.uniform(0, 1.0), rnd.uniform(0, 1.0), 1.00]
    NewHumGenV4Config["eyes"]["sclera"] = [rnd.uniform(0, 1.0), rnd.uniform(0, 1.0), rnd.uniform(0, 1.0), 1.00]
    # Height
    NewHumGenV4Config["height"]["set"] = height
    NewHumGenV4Config["keys"]["height_150"] = height_150
    NewHumGenV4Config["keys"]["height_200"] = height_200
    # Randomize Eye brows
    NewHumGenV4Config["hair"]["eyebrows"]["set"] = sEyebrows
    NewHumGenV4Config["hair"]["eyebrows"]["lightness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["redness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["roughness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["salt_and_pepper"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["roots"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["root_lightness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["root_redness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["roots_hue"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["eyebrows"]["fast_or_accurate"] = 1
    NewHumGenV4Config["hair"]["eyebrows"]["hue"] = rnd.uniform(0, 1.0)
    # Randomize Regular Hair
    NewHumGenV4Config["hair"]["regular_hair"]["set"] = sRegularHair
    NewHumGenV4Config["hair"]["regular_hair"]["lightness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["redness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["roughness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["salt_and_pepper"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["roots"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["root_lightness"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["root_redness"]= rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["roots_hue"] = rnd.uniform(0, 1.0)
    NewHumGenV4Config["hair"]["regular_hair"]["fast_or_accurate"] = 1.0
    NewHumGenV4Config["hair"]["regular_hair"]["hue"] = rnd.uniform(0, 1.0)
    # Face hair
    NewHumGenV4Config["hair"]["face_hair"] = dFaceHair
    # Clothing
    NewHumGenV4Config["clothing"]["outfit"]["set"] = outfit
    # Foot wear
    NewHumGenV4Config["clothing"]["footwear"]["set"] = sFootwear

    
    dictAnyHuman = {"dictCustom":
             {
                "sGender": sGender,
                "sArmatureName" : sArmatureName,
                "bOpenPoseHandLabels": False,
                "sOpenposeHandLabelFile": params['mParamConfig'].get('sOpenposeHandLabelFile', None),
                "bFacialRig": True,
                "sWFLWLableFile": params['mParamConfig'].get('sWFLWLableFile', None),
                "sIMSLabels": params['mParamConfig'].get('sIMSLabels', None),
                "sEyebrowLabelsPath": params['mParamConfig'].get('sEyebrowLabelsPath', None),
                "sPoseFilename": None,
                "dBeardLength" : dBeardLength,
            },
        "dictHumGen_V4": NewHumGenV4Config
    }
    return dictAnyHuman


# enddef
