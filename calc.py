import argparse 
parser = argparse.ArgumentParser() 
parser.add_argument('blog', default="JournalDev", help="Best blog name here.") 
args = parser.parse_args() 
if args.blog == 'JournalDev':
     print('You made it!') 
else: 
    print("Didn't make it!")
