ALPHABET_B52 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encoding_base52(num: int) -> str:
    result = []

    if num < 0:
        raise ValueError("incorrect id for encoding base 52 - number is negative")

    if num == 0:
        return "a"

    while num > 0:
        num, reminder = divmod(num, 52)
        result.append(ALPHABET_B52[reminder])

    return "".join(reversed(result))


def decoding_base52(code: str) -> int:
    code_arr = list(code)

    result = 0
    for symbol in code_arr:
        index = ALPHABET_B52.find(symbol)

        if index == -1:
            raise ValueError("incorrect character in code for decoding")

        result = (52 * result) + index

    return result


# if __name__ == "__main__":
#     for num in range(999999):
#         encoded = encoding_base52(num)
#         decoded = decoding_base52(encoded)
#         if decoded != num:
#             print(f"ALARM")
#     print('done')
#     # result = decoding_base52('bc')
#     # print(result)
