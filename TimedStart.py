import datetime


def timeleftmin(minutes):
    '''
    Takes array with times in array. Based off those paramaters,
    Returns the ammount of seconds before system time is equal to specified time
    Returns false for invalid input

    REMINDER:
    This uses system time
    Should not be trusted, users can change system time

    If you need just minutes:
    timeleftmin([arr])

    If you need just hours:
    timelefthour([arr])

    If you need mins and seconds:
    timeleftminsec([arr])

    If you need hours and minutes:
    timelefthourmin([arr])

    If you need hours, minutes and seconds:
    timelefthourminsec([arr])
    '''
    returnArr 
    now = datetime.datetime.now()
    returnArr = []
    for minute in minutes:
        timeSecond = ((minute - now.minute) * 60) - now.second
        if timeSecond < -1:
            continue
        else:
            returnArr.append(timeSecond)
    if len(returnArr) >= 1:
        return(returnArr)
    else:
        return(False)


def timeleftminsec(times):
    '''
    Takes array with times in array. Based off those paramaters,
    Returns the ammount of seconds before system time is equal to specified time
    Returns false for invalid input

    REMINDER:
    This uses system time
    Should not be trusted, users can change system time

    If you need just minutes:
    timeleftmin([arr])

    If you need just hours:
    timelefthour([arr])

    If you need mins and seconds:
    timeleftminsec([arr])

    If you need hours and minutes:
    timelefthourmin([arr])

    If you need hours, minutes and seconds:
    timelefthourminsec([arr])
    '''
    returnArr 
    returnArr = []

    now = datetime.datetime.now()
    for time in times:
        minute, second = time.replace(':', ' ').split()
        timeSecondLeft = ((int(minute) - now.minute) * 60) - (now.second - int(second))
        if timeSecondLeft < -1:
            continue
        else:
            returnArr.append(timeSecondLeft)
    if len(returnArr) >= 1:
        return(returnArr)
    else:
        return(False)


def timelefthourmin(times):
        '''
    Takes array with times in array. Based off those paramaters,
    Returns the ammount of seconds before system time is equal to specified time
    Returns false for invalid input

    REMINDER:
    This uses system time
    Should not be trusted, users can change system time

    If you need just minutes:
    timeleftmin([arr])

    If you need just hours:
    timelefthour([arr])

    If you need mins and seconds:
    timeleftminsec([arr])

    If you need hours and minutes:
    timelefthourmin([arr])

    If you need hours, minutes and seconds:
    timelefthourminsec([arr])
    '''
    returnArr 
    returnArr = []

    now = datetime.datetime.now()
    for time in times:
        hour, minute = time.replace(':', ' ').split()
        timeSecond = ((int(hour) - now.hour) * 3600) + ((int(minute) - now.minute) * 60) - now.second
        if timeSecond < -1:
            continue
        else:
            returnArr.append(timeSecond)
    if len(returnArr) >= 1:
        return(returnArr)
    else:
        return(False)


def timelefthour(hours):
    '''
    Takes array with times in array. Based off those paramaters,
    Returns the ammount of seconds before system time is equal to specified time
    Returns false for invalid input

    REMINDER:
    This uses system time
    Should not be trusted, users can change system time

    If you need just minutes:
    timeleftmin([arr])

    If you need just hours:
    timelefthour([arr])

    If you need mins and seconds:
    timeleftminsec([arr])

    If you need hours and minutes:
    timelefthourmin([arr])

    If you need hours, minutes and seconds:
    timelefthourminsec([arr])
    '''
    returnArr 
    now = datetime.datetime.now()

    returnArr = []
    for hour in hours:
        timeSecond = ((hour - now.hour) * 3600) - (now.minute * 60) - now.second
        if timeSecond < -1:
            continue
        else:
            returnArr.append(timeSecond)
    if len(returnArr) >= 1:
        return(returnArr)
    else:
        return(False)


def timelefthourminsec(times):
    '''
    Takes array with times in array. Based off those paramaters,
    Returns the ammount of seconds before system time is equal to specified time
    Returns false for invalid input

    REMINDER:
    This uses system time
    Should not be trusted, users can change system time

    If you need just minutes:
    timeleftmin([arr])

    If you need just hours:
    timelefthour([arr])

    If you need mins and seconds:
    timeleftminsec([arr])

    If you need hours and minutes:
    timelefthourmin([arr])

    If you need hours, minutes and seconds:
    timelefthourminsec([arr])
    '''
    returnArr = []

    now = datetime.datetime.now()
    for time in times:
        hour, minute, second = time.replace(':', ' ').split()
        timeSecondLeft = ((hour - now.hour) * 3600) + ((int(minute) - now.minute) * 60) + (now.second - int(second))
        if timeSecondLeft < -1:
            continue
        else:
            returnArr.append(timeSecondLeft)
    if len(returnArr) >= 1:
        return(returnArr)
    else:
        return(False)
