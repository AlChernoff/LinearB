class TooMuchCoinsException(Exception):
    """Exception raised for errors if the Amount of coins is more  than 50 or euqal

    Attributes:
        reschedule_time -- amount of time to add to current time for rescheduling
        message -- explanation of the error
    """

    def __init__(self,message):
        self.message = message

    def __str__(self):
        return  self.message