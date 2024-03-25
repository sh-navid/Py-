class PyHtml:
    """
    <>
        <body>
            <center>
                {test()}
            <center>
        </body>
    <>
    """
    def __init__(self) -> None:
        self._pattern=r"\<\>[\S\s]*?\<\>" # regex pattern to identify

    def exec(self, content):
        """
            to simplify the procedure we can replace <> with just a simple '''
        """

        # OK; this is working but cannot support {test()}
        content=content.replace("<>","'''")

        return content