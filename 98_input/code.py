
import math
import os
import random
import re
import sys
from subprocess import Popen, PIPE, TimeoutExpired



if __name__ == '__main__':

    test_inputs = []

    p1 = Popen(["printf", "55\nmert"], stdout=PIPE)
    p1.wait()
    process = Popen(["python3", "-c", "print('first input: ' + input())\nprint('second input: ' + input())"], stdin=p1.stdout, stdout=PIPE)

    # process = Popen(["printf '55mert'", "|", "python3", "-c", f"import sys\n\rimport traceback\n\rtry:\n\r    print('printing input from user')\n\r    print(input())\n\rexcept Exception as e:\n\r    exception_type, exception_object, exception_traceback = sys.exc_info()\n\r    line_number = exception_traceback.tb_lineno\n\r    print(exception_type, line_number, str(e), end ='')"]
    #        + test_inputs, stdout=PIPE)

    try:
        (output, err) = process.communicate(timeout=10)
        exit_code = process.wait()
        print(f"output: {output}")
        print(f"exit code: {exit_code}")
    except TimeoutExpired as timeout_err:
        error_message = "Timeout"
        print(error_message)
    except Exception as e:
        # Main Exception
        # abort test runs
        print(str(e))