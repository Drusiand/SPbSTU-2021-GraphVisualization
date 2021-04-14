_invalid_source_errmsg = "ERROR: source file not found"


class file_reader:
    """

    Context manager with handling FileNotFound error and closing valid file

    """
    def __init__(self, file_name: str, flag="r"):
        self.file = file_name
        self.flag = flag

    def __enter__(self):
        try:
            self.file_stream = open(self.file, self.flag)
        except FileNotFoundError:
            self.file_stream = None
        return self.file_stream

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_stream is None:
            print(_invalid_source_errmsg)
            return True
        self.file_stream.close()
