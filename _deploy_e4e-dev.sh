set -e -x
PATH="$PATH:/home/deploy/.nvm/versions/node/v22.3.0/bin:/home/deploy/.rbenv/shims"
echo $PATH
HOME_DIR=`pwd`
CLONE_DIR="/home/deploy/workspace/e4e_tools/website2.0"
JEKYLL_ENV="production"
MOUNT_DIR="$HOME/e4e_web_deploy_mnt"
# git clone --depth 1 --single-branch --branch=$BRANCH https://github.com/UCSD-E4E/website2.0.git $CLONE_DIR
cd $CLONE_DIR
git fetch --all
git reset --hard origin/main
mkdir -p $CLONE_DIR/cache
mkdir -p $CLONE_DIR/cache/resize
npm ci
npx gulp build -j '--config _config.yml'
date >> _site/last_deployed.txt
mkdir -p $MOUNT_DIR
if ! findmnt e4e@mywebsite.eng.ucsd.edu:htdocs/; then
  sshfs e4e@mywebsite.eng.ucsd.edu:htdocs/ $MOUNT_DIR -o IdentityFile=/home/deploy/.ssh/id_e4edev
fi
rsync -r --progress -c $CLONE_DIR/_site/ $MOUNT_DIR
umount $MOUNT_DIR
cd $HOME_DIR
