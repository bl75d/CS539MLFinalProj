import argparse

def add_args():
    parser = argparse.ArgumentParser(description='Task')
    parser.add_argument('-p', '--prepare', action='store_true')
    parser.add_argument('-a', '--analyze', action='store_true')
    parser.add_argument('-t', '--train', action='store_true')
    parser.add_argument('-e', '--eval', action='store_true')

    parser.add_argument('--predict', action='store_true')

    parser.add_argument('--period', default="1y", metavar='period', type=str)
    parser.add_argument('--interval', default="1d", metavar='interval', type=str)
    parser.add_argument('-s', '--stocks', action='append', default=[], metavar='stocks', type=str)
    
    parser.add_argument('--dir', default="model_checkpoints/", metavar='directory', type=str)
    parser.add_argument('--model', default="cp-0100.ckpt", metavar='model', type=str)
    parser.add_argument('--epochs', default=500, metavar='epochs', type=int)

    parser.add_argument('--layer_width',default=15, metavar='layer_width', type=int)
    parser.add_argument('--batch_size_divisor',default=1, metavar='batch_size_divisor', type=int)
    parser.add_argument('--save_period',default=100, metavar='save_period', type=int)
    return parser
