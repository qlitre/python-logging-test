from logging import config
import os
import logging
import slackweb
from dotenv import load_dotenv

load_dotenv()


class SlackNotifyHandler(logging.Handler):
    """
    エラーが発生したらSlackに通知する自作ハンドラ
    """

    def __init__(self):
        super().__init__()
        webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
        self.slack = slackweb.Slack(webhook_url)

    def emit(self, record):

        if len(record.msg) > 0:
            msg = self.format(record)
        else:
            msg = ''
        try:
            text = 'エラーが発生！ログを確認!\n' + msg
            self.slack.notify(text=text)
        except Exception:
            self.handleError(record)


# ルートディレクトリにログ保存用のディレクトリを作成
if not os.path.exists('./log'):
    os.makedirs('./log')

# loggingの設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
        }
    },
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "./log/game.log",
            "encoding": "utf-8"
        },
        # 追加
        'slackHandler': {
            "class": 'utils.log.SlackNotifyHandler',
            "level": "ERROR",
            "formatter": "simple",
        }
    },
    "loggers": {
        "game": {
            "level": "DEBUG",
            # slackHandlerを追記
            "handlers": [
                "fileHandler", "slackHandler"
            ],
            "propagate": False
        }
    },
}


def configure_logging():
    """loggingに設定をする"""
    config.dictConfig(LOGGING)
