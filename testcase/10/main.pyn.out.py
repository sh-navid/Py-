# pyn:compile


def test():
    return "Test"


def view():
    return (
            """
                <body>
                    <center>
                        """ + test() + """
                    <center>
                </body>
            """
    )


print(view())
