import datetime

timestamps = [
    1690747208.206005,
    1702855701.965646,
]

for timestamp in timestamps:
    datetime_obj = datetime.datetime.utcfromtimestamp(timestamp)
    formatted_date_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date_time)

# 这个程序允许用户输入一个 Unix 时间戳（例如 1690747208.206005 或 1690747208.20600）
# 然后将其转换为可读的日期时间格式。用户可以不断输入时间戳进行转换，
# 或输入 'q' 来退出程序。

def convert_timestamp_to_datetime(timestamp):
    """
    Converts a Unix timestamp to a formatted date-time string.
    Args:
        timestamp (float): Unix timestamp.

    Returns:
        str: Formatted date-time string.
    """
    datetime_obj = datetime.datetime.utcfromtimestamp(timestamp)
    return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

while True:
    input_str = input("请输入一个Unix时间戳（例如 1690747208.206005），输入'q'退出: ")

    if input_str.lower() == 'q':
        break

    try:
        timestamp = float(input_str)
        formatted_date_time = convert_timestamp_to_datetime(timestamp)
        print(f"转换后的日期时间: {formatted_date_time}")
    except ValueError:
        print("输入无效，请输入有效的Unix时间戳。")


