# game/coin_toss.py
import random
from logging import getLogger


class InvalidInputError(Exception):
    """無効な値が入力されたことを知らせるエラー"""
    pass


def game_start():
    # loggerをインスタンス化
    logger = getLogger(__name__)
    # ゲーム開始ログの出力
    logger.debug('game start')

    guess = ''
    while guess not in ('表', '裏'):
        print('コインの表裏を当ててください。表か裏を入力してください:')
        guess = input()

    toss = random.randint(0, 1)
    # 追加 tossの値を表か裏に変換
    toss = '表' if toss == 0 else '裏'
    # tossとguessの値を調べてみる
    logger.debug(f'toss="{toss}"')
    logger.debug(f'guess="{guess}"')

    if toss == guess:
        print('当たり')
    else:
        print('はずれ、もう１回当てて')
        guess = input()
        # ユーザーにエラーを知らせつつ、ログにもエラーとして書きこむ
        if guess not in ('表', '裏'):
            logger.error(f'2回目のguessで無効な値が入力された！guess={guess}')
            raise InvalidInputError('入力は表か裏にしてください')

        if toss == guess:
            print('当たり')
        else:
            print('はずれ。このゲームは苦手ですね')

    # ゲーム終了ログの出力
    logger.debug('game end')


"""
元のゲームのコード
Al Sweigart 著 相川 愛三 訳 (2017) . 退屈なことはPythonにやらせよう  
　株式会社オライリー・ジャパン P258

import random

guess = ''
while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力してください:')
    guess = input()

toss = random.randint(0, 1)
if toss == guess:
    print('当たり')
else:
    print('はずれ、もう１回当てて')
    guess = input()
    if toss == guess:
        print('当たり')
    else:
        print('はずれ。このゲームは苦手ですね')
"""
