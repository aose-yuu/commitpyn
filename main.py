import fire
import os
import git
from pick import pick

def clear_console():
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)

def select_func(title, options):
    title = title 
    options = options 
    option, index = pick(options, title)
    return index

def select_prefix():
    title = 'Select a prefix: '
    options = ['feat', 'fix', 'docs', 'style', 'refactor', 'perf', 'test']
    options_text = [
        'feat:     A new feature',
        'fix:      A bug fix',
        'docs:     Documentation only changes',
        'style:    Changes that do not affect the meaning of the code (while-space, formatting, missing semi-colons, etc)',
        'refactor: A code change that neither fixes a bug nor adds a feature',
        'perf:     Acode change that improves performance',
        'test:     Adding missing tests or correcting existing tests',
    ]
    index = select_func(title, options_text)
    return options[index]

def commit():
    repo = git.Repo()
    prefix = select_prefix()
    clear_console()
    message = input('Enter commit message: ')
    commit_message = f'{prefix}: {message}'
    repo.index.commit(commit_message)
    print('Commited.')

def main():
    fire.Fire(commit)

if __name__ == '__main__':
    main()
