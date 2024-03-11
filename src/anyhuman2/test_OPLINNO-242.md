### About [OPLINNO-242](https://github.com/mnt1lr/image-render-blender-human/tree/feature/OPLINNO-242---Convert-Eyebrow-particles-to-mesh):


### What changed?

Added 
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_001.json`<\br>
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_002.json`<\br>
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_003.json`<\br> 
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_004.json`<\br>
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_005.json`<\br>
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_006.json`<\br>
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_007.json`<\br>
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_008.json`<\br>
    - `anyhuman2/labelling/mapping/eyebrows/Eyebrows_009.json`

Each json file contains WFLW labels [33-50] for each eyebrow style, `HG_Eyebrows_001 `through `HG_Eyebrows_009`

Added new entry `sEyebrowLabelsPath` to `anyhuman2\personas\FILE_male.json`, as follows

```json
{
    "dictCustom": {
        "sGender": "male",
        "sArmatureName": "Armature.001",
        "bOpenPoseHandLabels": true,
        "sOpenposeHandLabelFile": "labelling//mapping//openpose_hand_humgen.json",
        "bFacialRig": true,
        "sWFLWLableFile": "labelling//mapping//WFLW_bones.json",
        "sEyebrowLabelsPath":"labelling//mapping//eyebrows//",
        "sPoseFilename": {
            "set": null
        },
        "dBeardLength": {...}
    },
    "dictHumGen_V4": {...}
}
```

> Case FILE mode:
When a new human is created from `FILE_male.json` file, depending on eyebrow style set in `dictHumGen_V4['hair']['eyebrows']['set']`, appropriate JSON file will be read from the path taken from `dictCustom['sEyebrowLabelsPath']`

Suppose `dictHumGen_V4['hair']['eyebrows']['set']` = `Eyebrows_007` and `dictCustom['sEyebrowLabelsPath']` = `labelling//mapping//eyebrows//`then JSON file will be taken as `labelling//mapping//eyebrows//Eyebrows_007.json`

> Case RANDOM mode:
When a new human is generated, appropriate JSON file will be read from the path mentioned in `dictCustom['sEyebrowLabelsPath']` by getting eyebrow style from HumGen3D API `human.hair.eyebrows.as_dict()['set']`


### How to test [OPLINNO-240](https://github.com/mnt1lr/image-render-blender-human/tree/feature/OPLINNO-240---add-missing-v4-WFLW-eyebrow-labels)
- 1. In dev.py, enable `FILE` mode, pass `src\\anyhuman2\\personas\\FILE_male.json` as `sFilename` under `mParamConfig` (line ~69). Make sure bOpenPoseHandLabels & bFacialRig are `True` in json file
- 2. change file input for sHandLabelFile & sWFLWLableFile (line. 291 & 297)
- 3. Hit play by opening `dev.py` in blender debug mode, Face labels should show up


### Next work
- 1. Improve left eyebrow labels position (should mirror right arrow labels), updates reflect in `WFLW_bones.json`
