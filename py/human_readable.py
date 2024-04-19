def make_readable(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}"


print(make_readable(0))  # "00:00:00"
print(make_readable(59))  # "00:00:59"
print(make_readable(60))  # "00:01:00"
print(make_readable(3599))  # "00:59:59"
print(make_readable(3600))  # "01:00:00"
print(make_readable(86399))  # "23:59:59"
print(make_readable(86400))  # "24:00:00"
print(make_readable(359999))  # "99:59:59"
