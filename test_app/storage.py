
from typing import NoReturn

from django.core.files.storage.filesystem import FileSystemStorage


class NoReadException(Exception):
    pass


class NoReadStorageMixin:
    def open(self, *args, **kwargs) -> NoReturn:
        raise NoReadException("This storage class does not support reading.")


class NoReadFileSystemStorage(NoReadStorageMixin, FileSystemStorage):
    pass