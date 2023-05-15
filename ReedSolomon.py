import os


def qr_check_qformat(Format):
    QrGenerator = 0b10100110111
    for I in range(4, -1, -1):
        if Format & (1 << (I + 10)):
            Format = Format ^ (QrGenerator << I)
    return Format
