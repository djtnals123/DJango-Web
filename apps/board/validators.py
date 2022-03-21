from django.core.exceptions import ValidationError


def max_file_size(file):
    file_size = file.file.size
    limit_mb = 10
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)
