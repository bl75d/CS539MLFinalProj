from arg_parser import *
from main import main

parser = add_args()
args = parser.parse_args(["--train", "--epochs", "1000", "--layer_width", "50"])

main(args)