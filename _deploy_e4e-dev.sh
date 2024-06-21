PATH="$PATH:/home/deploy/.nvm/versions/node/v22.3.0/bin:/home/deploy/.rbenv/shims"
echo $PATH
BRANCH="main"
HOME_DIR=`pwd`
CLONE_DIR=`mktemp -d`
JEKYLL_ENV="production"
git clone --depth 1 --single-branch --branch=$BRANCH https://github.com/UCSD-E4E/website2.0.git $CLONE_DIR
cd $CLONE_DIR
mkdir -p $CLONE_DIR/cache
mkdir -p $CLONE_DIR/cache/resize
npm ci
npx gulp build -j '--config _config.yml,_e4e_dev_config.yml'
date >> _site/last_deployed.txt
rsync -r -e "ssh -i $HOME/.ssh/id_e4edev" --progress $CLONE_DIR/_site/ e4e-dev@e4e-dev.ucsd.edu:htdocs/
cd $HOME_DIR
rm -rf $CLONE_DIR
