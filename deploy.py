'''E4E Website Development PR Deploy
'''
import datetime as dt
from argparse import ArgumentParser
from os import environ
from pathlib import Path
from shlex import split
from subprocess import check_call


def main():
    parser = ArgumentParser()
    parser.add_argument('--host', default='e4e-dev@e4e-dev.ucsd.edu', type=str)
    parser.add_argument('--branch', required=True, type=str)
    parser.add_argument('--pr', required=True, type=int)

    args = parser.parse_args()

    CLONE_DIR = Path('/home/deploy/workspace/e4e_tools/website_prs/').joinpath(str(args.pr))
    CLONE_DIR.mkdir(parents=True, exist_ok=True)
    if not CLONE_DIR.joinpath('.git').exists():
        cmd = f'git clone --depth 1 --single-branch --branch={args.branch} https://github.com/UCSD-E4E/website2.0.git {CLONE_DIR.as_posix()}'
        check_call(split(cmd))
    else:
        cmd = f'git fetch --all'
        check_call(split(cmd), cwd=CLONE_DIR)
        cmd = f'git reset --hard origin/{args.branch}'
        check_call(split(cmd), cwd=CLONE_DIR)
    
    # At this point, the repo should be checked out to latest in the PR at CLONE_DIR
    CACHE_DIR = CLONE_DIR.joinpath('cache')
    RESIZE_DIR = CACHE_DIR.joinpath('resize')
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    RESIZE_DIR.mkdir(parents=True, exist_ok=True)
    check_call(split('npm ci'), cwd=CLONE_DIR)
    cmd = ['npx', 'gulp', 'build', '-j', f'--baseurl {args.pr} --config _config.yml,_e4e_dev_config.yml']
    check_call(cmd, cwd=CLONE_DIR, )
    assert CLONE_DIR.joinpath('_site').exists()
    with open(CLONE_DIR.joinpath('_site', 'last_deployed.txt'), 'w', encoding='utf-8') as handle:
        handle.write(dt.datetime.now().isoformat())

    # Deploy
    SITE_DIR = CLONE_DIR.joinpath('_site')
    cmd = f'rsync -r -e "ssh -i /home/deploy/.ssh/id_e4edev" --progress {SITE_DIR.as_posix()}/ e4e-dev@e4e-dev.ucsd.edu:htdocs/{args.pr}'

    check_call(split(cmd), cwd=CLONE_DIR)


if __name__ == '__main__':
    main()