import argparse

def add_args():
    parser = argparse.ArgumentParser(description='Task')
    parser.add_argument('-p', '--prepare', action='store_true')
    parser.add_argument('-t', '--train', action='store_true')
    parser.add_argument('-e', '--eval', action='store_true')

    parser.add_argument('--predict', action='store_true')

    parser.add_argument('--period', default="1y", metavar='period', type=str)
    parser.add_argument('--interval', default="1d", metavar='interval', type=str)
    parser.add_argument('-s', '--stocks', action='append', default=[], metavar='stocks', type=str)
    
    parser.add_argument('--model', default="model_checkpoints/cp-0100.ckpt", metavar='model', type=str)
    return parser
