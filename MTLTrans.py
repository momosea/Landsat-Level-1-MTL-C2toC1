# coding = utf-8
# author: Yaping Mo
import re
from pathlib import Path

reconstruct_texts = [
    "IMAGE_ATTRIBUTES", "PROJECTION_ATTRIBUTES", "LEVEL1_PROCESSING_RECORD", "LEVEL1_MIN_MAX_RADIANCE",
    "LEVEL1_MIN_MAX_REFLECTANCE", "LEVEL1_MIN_MAX_PIXEL_VALUE", "LEVEL1_RADIOMETRIC_RESCALING",
    "LEVEL1_THERMAL_CONSTANTS", "LEVEL1_PROJECTION_PARAMETERS", "PRODUCT_PARAMETERS"
]
remove_texts = [
    "SENSOR_MODE_SLC", "SENSOR_ANOMALIES", "DIGITAL_OBJECT_IDENTIFIER",
    "FILE_NAME_QUALITY_L1_RADIOMETRIC_SATURATION", "FILE_NAME_ANGLE_SENSOR_AZIMUTH_BAND",
    "FILE_NAME_ANGLE_SOLAR_AZIMUTH_BAND", "FILE_NAME_ANGLE_SOLAR_ZENITH_BAND",
    "FILE_NAME_METADATA_XML"
]
rename_texts = {
    "PROJECTION_ATTRIBUTES": "PROJECTION_PARAMETERS", "LEVEL1_PROCESSING_RECORD": "PRODUCT_METADATA",
    "PROCESSING_LEVEL": "DATA_TYPE", "DATE_PRODUCT_GENERATED": "FILE_DATE",
    "FILE_NAME_QUALITY_L1_PIXEL": "FILE_NAME_BAND_QUALITY",
    "FILE_NAME_GROUND_CONTROL_POINT": "GROUND_CONTROL_POINT_FILE_NAME",
    "FILE_NAME_ANGLE_COEFFICIENT": "ANGLE_COEFFICIENT_FILE_NAME",
    "FILE_NAME_METADATA_ODL": "METADATA_FILE_NAME",
    "FILE_NAME_CPF": "CPF_NAME", "DATA_SOURCE_ELEVATION": "ELEVATION_SOURCE",
    "LEVEL1_THERMAL_CONSTANTS": "TIRS_THERMAL_CONSTANTS", "LEVEL1_": ""
}


def ReconstructText(list):
    '''Reconstruct group structure'''
    for ele in list:
        result = re.findall("  GROUP = " + ele + "[\s\S]*\n  END_GROUP = " + ele, inputs)
        if result:
            output.extend(result)
        else:
            print("Can't find " + ele)
    return


def RemoveText(list):
    '''Remove added parameter'''
    data = ""
    for ele in list:
        results = re.findall("    " + ele + ' = "\S*"\n', inputs)
        for result in results:
            data = inputs.replace(str(result), "")
    return data


def RenameText(text, dic):
    '''Rename group/parameter'''
    data = ""
    for key, value in dic.items():
        if text.find(key):
            data = text.replace(key, value)
    return data


# ==================================================================================== #
current_path = Path.cwd()
files = Path("/").joinpath(current_path, "inputs").rglob("*.txt")

for file in files:
    if file.exists():
        inputs = open(str(file), "r").read()
        file_name = file.name
        inputs = RemoveText(remove_texts)
        output = ["GROUP = L1_METADATA_FILE"]
        ReconstructText(reconstruct_texts)
        output.append("END_GROUP =  L1_METADATA_FILE\nEND")
        str_output = RenameText("\n".join(output), rename_texts)

        Path("/").joinpath(current_path, "outputs").mkdir(parents=True, exist_ok=True)
        savefile = str(file).replace("inputs", "outputs")
        try:
            fsave = open(str(savefile), "w").write(str_output)
        except IOError:
            print(file_name + " save failed\n")
        else:
            print(file_name + " saved successfully\n")
temp = input("Press the enter key to exit...")
