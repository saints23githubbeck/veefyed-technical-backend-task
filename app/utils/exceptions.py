from fastapi import HTTPException, status


class InvalidFileTypeError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JPEG and PNG images are allowed"
        )


class FileTooLargeError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File size exceeds 5MB limit"
        )


class ImageNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found"
        )