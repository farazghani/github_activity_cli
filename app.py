import argparse
from main import get_github_activity

def main():
    # 1. Initialize the parser
    parser = argparse.ArgumentParser(description="enter your github username")

    parser.add_argument("my_arg" , type=str , help="The single required input")
    arg = parser.parse_args()

    url = f"https://api.github.com/users/{arg.my_arg}/events"

    out = get_github_activity(url)

    for o in out:
        if o.event == "WatchEvent":
            print(f"starred {o.repo}")
            

        elif o.event == "PushEvent":
            print(f"pushed commits to {o.repo}")

        else:
            print(f"open new issue at {o.repo}")














if __name__ == "__main__":
    main()