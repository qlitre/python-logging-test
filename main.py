# main.py
from utils import log
from game import coin_toss


def start():
    # loggingの設定を読み込む
    log.configure_logging()
    # gameを開始する
    coin_toss.game_start()


if __name__ == '__main__':
    start()
