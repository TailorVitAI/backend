def truncate(string: str | None, length=20, indicator="...", on_none="-"):
    return (
        string[:length] + (indicator if len(string) > length else "")
        if string
        else on_none
    )
