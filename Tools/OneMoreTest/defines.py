import os
from enum import Enum

TM_PATH = os.path.join(os.getcwd(), 'TM')
MM_PATH = os.path.join(os.getcwd(), 'MM')
MODEL_PATH = os.path.join(os.getcwd(), 'model')
DATA_PATH = os.path.join(os.getcwd(), 'data')
FIG_PATH = os.path.join(os.getcwd(), 'fig')
TEMP_PATH = os.path.join(os.getcwd(), 'temp')
DATA1_PATH = os.path.join(os.getcwd(), 'data1')
TEST_PATH = os.path.join(os.getcwd(), 'test')


class TM(Enum):
    TM1_name = 'jacksoncore_6'
    TM2_name = 'compress_30'
    TM3_name = 'csv_14'
    TM4_name = 'time_3_addYears'
    TM5_name = 'time_3_addMonths'
    TM6_name = 'time_3_addWeeks'
    TM7_name = 'time_3_addDays'
    TM8_name = 'time_3_add'
    TM9_name = 'time_14_minusMonths'
    TM10_name = 'time_14_plusMonths'
    TM11_name = 'csv_3'
    TM12_name = 'lang_21'
    TM13_name = 'io_18'
    TM14_name = 'shiro_web_3'
    TM15_name = 'johnzon_core_2'
    TM16_name = 'compress_39'
    TM17_name = 'mockito_6'
    TM18_name = 'geometry_core_3'
    TM19_name = 'math_15'
    TM20_name = 'codec_15'
    TM21_name = 'codec_3'
    TM22_name = 'compress_40'
    TM23_name = 'io_25'
    TM24_name = 'compress_50'
    TM25_name = 'math_24'
    # TM26_name = 'io_13'
    TM27_name = 'codec_12'
    TM28_name = 'codec_14'
    TM29_name = 'suncalc_1'
    TM30_name = 'suncalc_1'
    # TM31_name = 'compress_6'
    TM32_name = 'math_26'
    TM33_name = 'math_5'
    TM34_name = 'drools_model_compiler_1'
    TM35_name = 'gson_9'
    TM36_name = 'hivemall_core_1'
    TM37_name = 'io_8'
    TM38_name = 'io_2'
    TM39_name = 'vault_core_1'
    TM40_name = 'jacksoncore_12'
    TM41_name = 'jacksoncore_28'
    # TM42_name = 'jacksondatabind_101'
    TM43_name = 'jacksondatabind_12'
    TM44_name = 'jacksondatabind_56'
    TM45_name ='jacksondatabind_87'
    TM46_name ='jacksondatabind_30'
    TM47_name ='jacksondatabind_31'
    TM48_name ='jacksonxml_1'
    TM49_name = 'jacksonxml_2'
    TM50_name = 'james_mime4j_core_6'
    TM51_name = 'james_mime4j_core_7'
    TM52_name = 'james_mime4j_core_8'
    TM53_name = 'math_8'
    TM54_name = 'math_9'