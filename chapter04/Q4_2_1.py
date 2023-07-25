def number_to_day(num=0)
    if num == 0:
        day = '水曜日'
    elif num == 1:
        day = '木曜日'
    elif num == -1:
        day = '火曜日'
    else:
        day = '今日より1日を超えて離れた日'
    return day
