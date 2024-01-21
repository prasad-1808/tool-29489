import argparse
from includes.filereader import file_reader
from includes.scan import scanner

def banner():
    print("""
████████╗░█████╗░░█████╗░██╗░░░░░░░░░░░██████╗░░█████╗░░░██╗██╗░█████╗░░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░░░░░░░╚════██╗██╔══██╗░██╔╝██║██╔══██╗██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░░░░█████╗░░███╔═╝╚██████║██╔╝░██║╚█████╔╝╚██████║
░░░██║░░░██║░░██║██║░░██║██║░░░░░╚════╝██╔══╝░░░╚═══██║███████║██╔══██╗░╚═══██║
░░░██║░░░╚█████╔╝╚█████╔╝███████╗░░░░░░███████╗░█████╔╝╚════██║╚█████╔╝░█████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝░░░░░░╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░░╚════╝░""")
    print("\n")

    print("""
        This Tool is used to check for CVE-2023-29489 Vulnerabilty in the provided URL with the set of payloads available
        To use tool-29489:
          tool-29489 [help] [URL] [inputfile] [outputfile]
          -h or --help   : To display help options.
          -u or --url    : To input URL to check.
          -i or --input  : To give the input file.
          -o or --output : To give the output file.
""")

def display_tool_name():
    print("""
████████╗░█████╗░░█████╗░██╗░░░░░░░░░░░██████╗░░█████╗░░░██╗██╗░█████╗░░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░░░░░░░╚════██╗██╔══██╗░██╔╝██║██╔══██╗██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░░░░█████╗░░███╔═╝╚██████║██╔╝░██║╚█████╔╝╚██████║
░░░██║░░░██║░░██║██║░░██║██║░░░░░╚════╝██╔══╝░░░╚═══██║███████║██╔══██╗░╚═══██║
░░░██║░░░╚█████╔╝╚█████╔╝███████╗░░░░░░███████╗░█████╔╝╚════██║╚█████╔╝░█████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝░░░░░░╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░░╚════╝░""")
    print("\n\n\n")

parser = argparse.ArgumentParser(add_help=False, usage=argparse.SUPPRESS)

parser.add_argument('-h','--help',nargs='?',const=True,help="Display help option.")
parser.add_argument('-u','--url',metavar='URL to scan')
parser.add_argument('-i','--input',metavar='input_file to scan',help="Pass input file name")
parser.add_argument('-o','--output',metavar='output_file to write result',help="Pass the output file name")

args = parser.parse_args()

help = args.help
url = args.url
input_file = args.input
output_file = args.output


def main():
    if help:
        banner()
    elif url:
        display_tool_name()
        scanner(url,output_file)
    elif input_file:
        display_tool_name()
        file_reader(input_file,output_file)
    else:
        banner()

if __name__=="__main__":
    main()
    