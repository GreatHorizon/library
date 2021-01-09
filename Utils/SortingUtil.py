import datetime

def SortStringColumn(tv, col, reverse=True):
    l = [(tv.set(k, col), int(k)) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda:SortStringColumn(tv, col, not reverse))



def SortNumericColumn(tv, col, reverse=True):
    l = [(int(tv.set(k, col)), int(k)) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda:SortNumericColumn(tv, col, not reverse))


def SortDateColumn(tv, col, reverse=True):
    l = [(str(tv.set(k, col)), int(k)) for k in tv.get_children('')]
    l = sorted(l, key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'), reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda:SortDateColumn(tv, col, not reverse))
