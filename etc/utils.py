def get_first_error_message(items):
    label = list(items)[0][0]
    first_err_msg = list(items)[0][1][0]
    msg = '{}: {}'.format(label, first_err_msg)
    return msg
