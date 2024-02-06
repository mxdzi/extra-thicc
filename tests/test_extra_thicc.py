from string import ascii_lowercase

from extra_thicc import make_extra_thicc


def test_make_extra_thicc_letters_lower():
    result = make_extra_thicc(ascii_lowercase)

    assert "卂乃匚刀乇千厶卄工勹片乚爪𠘨口尸甲尺己丅凵リ山乂丫乙" == result

