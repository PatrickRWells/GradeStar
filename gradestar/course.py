class Course:
    
    def __init__(self, data={}):
        self.__dict__.update(data)

    
    def _validate(self, *args, **kwargs):
        """
        Checks to make sure a minimum set of arguments
        have been past to the constructor
        """

        assert hasattr(self, "name"), "Unable to find course name"
        assert hasattr(self, "id"), "Unable to find course ID"
