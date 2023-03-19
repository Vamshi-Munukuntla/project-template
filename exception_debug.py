import math
import sys

a, b, c = 2, 2, 1

try:
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    print(x1, x2)
except:
    e, p, t = sys.exc_info()
    print('E:', e)
    print('P:', p)
    print('T', t)
    print('ERROR FILE PATH:', t.tb_frame)
    print('ERROR LINE NUMBER:', t.tb_frame.f_lineno)
    print('TRY BLOCK STARTING LINE NUMBER:', t.tb_lineno)
    print('FILE_NAME:', t.tb_frame.f_code.co_filename)

    exception_block_line_number = t.tb_frame.f_lineno
    try_block_line_number = t.tb_lineno
    file_name = t.tb_frame.f_code.co_filename

    error_message = f"""
    Error occurred in script: 
    [ {file_name} ] at 
    try block line number: [{try_block_line_number}] 
    and exception block line number: [{exception_block_line_number}] 
    """
    print(error_message)
