def title_maker(string):
    """Generates comments with blocks"""
    import pyperclip
    dashes = "#"+"-".center(69,"-")
    main_title = "#"+string.center(69,"-")
    title = f"\n{dashes}\n{main_title}\n{dashes}\n"
    pyperclip.copy(title)

def single_title_maker(string):
    """Generates comments with blocks"""
    import pyperclip
    main_title = "#" + string.center(69, "-")
    pyperclip.copy(main_title)


