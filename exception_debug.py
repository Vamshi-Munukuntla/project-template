import math
import sys
from collections import namedtuple


a, b, c = 2, 2, 1

try:
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    print(x1, x2)
except:
    e, p, exec_tb = sys.exc_info()
    print('TYPE OF EXCEPTION:', e)
    print('EXCEPTION ITSELF:', p)
    print('TRACEBACK OBJECT', exec_tb)
    print('ERROR FILE PATH:', exec_tb.tb_frame)
    print('ERROR LINE NUMBER:', exec_tb.tb_frame.f_lineno)
    print('TRY BLOCK STARTING LINE NUMBER:', exec_tb.tb_lineno)
    print('FILE_NAME:', exec_tb.tb_frame.f_code.co_filename)

    exception_block_line_number = exec_tb.tb_frame.f_lineno
    try_block_line_number = exec_tb.tb_lineno
    file_name = exec_tb.tb_frame.f_code.co_filename

    error_message = f"""
    Error occurred in script: 
    [ {file_name} ] at 
    try block line number: [{try_block_line_number}] 
    and exception block line number: [{exception_block_line_number}] 
    """
    print(error_message)


Color = namedtuple('Color', ['red', 'blue', 'green'])

color = Color(1, 1, 1)
print(color)
print(color.red)
