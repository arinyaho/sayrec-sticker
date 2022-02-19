import os
import argparse
import sys


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


parser = argparse.ArgumentParser(description='Numbering sayrec sticker.')
parser.add_argument('-s', '--side', type=str.lower, choices=['a','b','c'], required=True, metavar='SIDE', help='Side of sayrec sticker')
parser.add_argument('-i', '--index', type=int, required=True, metavar='NUM', help='Sticker number')
parser.add_argument('-d', '--dir', type=dir_path, required=True, metavar='PATH', help='Location of MP3 files')
parser.add_argument('-l', '--limit', type=int, required=False, metavar='NUM', help='Convert NUM MP3 file')
parser.add_argument('-p', '--prefix-include', type=str, required=False, metavar='STRING', help='Prefix for MP3 files')
parser.add_argument('-q', '--prefix-exclude', type=str, required=False, metavar='STRING', help='Prefix for MP3 files to exlucde')
args = parser.parse_args()

index = args.index

if args.side == 'a':
	prefix='SAY62'
	offset = 0
elif args.side == 'b':
	prefix='SAY59'
	offset = -476
elif args.side == 'c':
	prefix='SAY57'
else:
	print('Not supported side : ' + args.side)
	sys.exit(1)

fnames = os.listdir(args.dir)
fnames.sort()
count = 0
for fname in fnames:
	if not fname.lower().endswith('.mp3'):
		continue

	if args.prefix_include is not None:
		if not fname.startswith(args.prefix_include):
			continue
	if args.prefix_exclude is not None:
		if fname.startswith(args.prefix_exclude):
			continue

	if args.side == 'c':
		if index < 953 or index > 1428:
			printf('Index of side C must be between 953 and 1428.')
			sys.exit(1)
		elif index >= 1191:
			offset = -949
		elif index >= 1072:
			offset = -950
		elif index >= 953:
			offset = -951

	new_name = prefix + '{:0>3}'.format((index + offset) * 2)
	f = args.dir + os.path.sep + fname
	t = args.dir + os.path.sep + new_name + '.mp3'
	
	print(index, ':', fname, '->', new_name)

	os.rename(f, t)

	index += 1
	count += 1
	if args.limit == count:
		break

