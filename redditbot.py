import praw
import click
from googletrans import Translator

@click.command()
@click.argument('post_url')
def main(post_url):

    reddit = praw.Reddit(
        client_id="FAKRVSGPPz7yx-qjjw09FQ",
        client_secret="O_Ev6V3UBSsLVcC4L5igKikgmq1yRw",
        user_agent="comment translator bot (by /u/MrAySian)",
    )

    translator = Translator()

    submission = reddit.submission(url=post_url)
    for i in range(len(submission.comments)):
        comment = submission.comments[i]

        print(f'Comment {i + 1}:')
        print(translator.translate(comment.body, dest='es').text)
        #print(comment.body)

if __name__ == '__main__':
    main()