import builtins

user_raised_exceptions = [
    exc for exc in dir(builtins)
    if isinstance(getattr(builtins, exc), type)
    and issubclass(getattr(builtins, exc), Exception)
    and not exc.startswith("_")
]

for exc in user_raised_exceptions:
    print(exc)