import config
from twitter import Twitter, OAuth

LF = '\n'
CHECK_MARK = '✅'

def main():
    t = Twitter(
        auth = OAuth(
            config.TW_TOKEN,
            config.TW_TOKEN_SECRET,
            config.TW_CONSUMER_KEY,
            config.TW_CONSUMER_SECRET,
        )
    )

    msg = '#今日の積み上げ'\
            + LF + CHECK_MARK + 'Twitter API使って自動ツイート機能作成'\
            + LF + CHECK_MARK + '温泉いく'\
            + LF\
            + LF + '#駆け出しエンジニアと繋がりたい'

    t.statuses.update(status = msg)

if __name__ == '__main__':
    main()
