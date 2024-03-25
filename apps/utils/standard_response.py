from fastapi.responses import JSONResponse


class StandardResponse:
    """This class is universal to return standard API responses

    Attributes:
        status (int): The http status response from API
        data (dict/list): The Data from API
        message (str): The message from the API
    """

    def __init__(self, status: int, data: dict, message: str) -> None:
        """This function defines arguments that are used in the class

        Arguments:
            status (int): The http status response from API
            data (dict/list): The Data from API
            message (str): The message from the API

        Returns:
            Returns the API standard response
        """
        self.status = status
        self.status_code = status
        self.data = data
        self.message = message

    @property
    def make(self) -> dict:
        self.status = "success" if self.status in [201, 200] else False
        response = {'status': self.status, 'data': self.data, 'message': self.message}
        return JSONResponse(content=response,status_code=self.status_code)
