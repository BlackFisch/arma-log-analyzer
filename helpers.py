def bytes_to_unit(b_count: int, use_binary: bool = False, target_unit: str = None, err_on_negative: bool = False) -> str:
    '''
    Convert amount of bytes into a unit.
    Largest supported unit: yottabyte/yobibyte

    @param b_count: Amount of bytes.
    @param use_binary: Use units based on binary instead of decimal (more accurate). Default: False
    @param target_unit: Specify target unit to convert to. Deducts use_binary from unit name. Default: None
    @param err_on_negative: Raise ValueError if b_count is negative. Default: False
    @raise ValueError if b_count is negative and err_on_negative is True, or if target_unit is set and not recognized


    @return: String with the amount of bytes and the unit.
    '''
    return bits_to_unit(b_count * 8, use_binary, target_unit, err_on_negative)


def bits_to_unit(b_count: int, use_binary: bool = False, target_unit: str = None, err_on_negative: bool = False) -> str:
    '''
    Convert amount of bits into a unit.
    Largest supported unit: yottabyte/yobibyte

    @param b_count: Amount of bytes.
    @param use_binary: Use units based on binary instead of decimal (more accurate). Default: False
    @param target_unit: Specify target unit to convert to. Deducts use_binary from unit name. Default: None
    @param err_on_negative: Raise exception if b_count is negative. Default: False
    @raise ValueError if b_count is negative and err_on_negative is True, or if target_unit is set and not recognized


    @return: String with the amount of bytes and the unit.
    '''
    UNIT_DEC = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    UNIT_BINARY = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
    BASE_MAGNITUDE = [1000, 1024][use_binary]
    UNITS = [UNIT_DEC, UNIT_BINARY][use_binary]

    if b_count == 0:
        return "0 b"

    # handle negative values in a secure way
    is_negative = b_count < 0
    if is_negative and err_on_negative:
        raise ValueError(
            "Negative value was supplied, but a positive value was expected.")

    if is_negative:
        b_count = abs(b_count)
        is_negative = '-'  # now use it for the output
    else:
        is_negative = ''

    # Force specified target unit
    if target_unit is not None:
        if target_unit == 'b':
            return f'{is_negative}{b_count} b'
        if target_unit in UNIT_DEC:
            return f"{is_negative}{b_count / pow(1000, UNIT_DEC.index(target_unit))} {target_unit}"
        elif target_unit in UNIT_BINARY:
            return f"{is_negative}{b_count / pow(1024, UNIT_BINARY.index(target_unit))} {target_unit}"
        else:
            raise ValueError('Invalid target unit: {}'.format(target_unit))

    if b_count <= 8:
        return f"{is_negative}{b_count} b"

    b_count = b_count / 8

    output = "ERROR"

    for index, unit in enumerate(UNITS):
        if b_count / pow(BASE_MAGNITUDE, index) < 1:
            break
        output = f"{is_negative}{b_count / pow(BASE_MAGNITUDE, index)} {unit}"

    return output
