import aiogram
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token="6086360512:AAHhw6cOLcovpNei6sFGs3UBBwW9AjCPTQM")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_message(message: types.Message):
    await message.reply('/1 431.43')


@dp.message_handler(commands="1")
async def sixth_solve(message: types.Message):
    if message.text == '/1':
        await message.reply('Введите в формате:\n\n/1 431.67')
    else:
        mess_split = float(message.text.replace('/1 ', ''))
        n = int(str(mess_split).split('.')[0])
        b = ''
        spp = []
        while n > 0:
            spp.append(f'{n} / 2 = {n // 2}, остаток: {n - (n // 2 * 2) if n - (n // 2 * 2) != 0 else 0}')
            b = str(n % 2) + b
            n = n // 2
        await message.reply("\n".join(spp))
        await message.reply(b)
        await message.reply(f'ИТОГ: \n\n{float_to_binary(mess_split)}')


def full_num(n):
    n = int(str(n).split('.')[0])
    b = ''
    while n > 0:
        print(f'{n} / 2 = {n // 2}, остаток: {n - (n // 2 * 2) if n - (n // 2 * 2) != 0 else 0}')
        b = str(n % 2) + b
        n = n // 2

    return b


def float_to_binary(num):
    exponent=0
    shifted_num=num
    while shifted_num != int(shifted_num):
        shifted_num*=2
        exponent+=1
    if exponent==0:
        return '{0:0b}'.format(int(shifted_num))
    binary='{0:0{1}b}'.format(int(shifted_num),exponent+1)
    integer_part=binary[:-exponent]
    fractional_part=binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part,fractional_part[:10])


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
