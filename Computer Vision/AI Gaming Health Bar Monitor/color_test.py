
class ConsoleColor:

    def print_format_table():
        """
        prints table of formatted text format options
        """
        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')

    def color(style, fg, bg):
        color = ';'.join([str(style), str(fg), str(bg)])
        return f'\x1b[{color}m'

    def norm():
        return '\x1b[0m'


# ConsoleColor.print_format_table()

print(f'{ConsoleColor.color(7,33,41)}Hello{ConsoleColor.norm()}, world!')