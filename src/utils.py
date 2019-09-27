from ctypes import CFUNCTYPE, cdll, c_char_p, c_int


def py_error_handler(filename, line, function, err, fmt):
    pass


def error_messages():

    ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int,
                                   c_char_p)
    c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    # Set error handler
    asound.snd_lib_error_set_handler(c_error_handler)