const util = require('node:util');
const fs = require('fs');
const middleware = require('./middleware');

const exec = util.promisify(require('node:child_process').exec);
const { watch, src, dest , series} = require('gulp');
var browserSync = require('browser-sync').create();


function copy_foundation_files(cb) {
    //move foundation css to build 
    foundation = [
        "./node_modules/foundation-sites/dist/css/foundation.min.css",
        "./node_modules/foundation-sites/dist/js/foundation.min.js"
    ]
   
    return src(foundation).pipe(dest('_site/assets/')) 
}

async function create_command(command) {
    const { stdout, stderr } = await exec(command);
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
}

async function build(cb) {
    await create_command("bundle exec jekyll build --config _config.yml")
    cb();
}

async function prod_build(cb) {
    await create_command("bundle exec jekyll build --config '_config.yml,_e4e_dev_config.yml'")
    cb();
}

async function dev_build(cb) {
    await create_command("bundle exec jekyll build --config _local_config.yml")
    cb();
}

//ASSUMES THAT SERVER CANNOT GO DOWN AS LONG AS GULP IS WATCHING
let has_started = false;
function start_server(cb) {
    if (has_started) {
        cb();
        return;
    }

    has_started = true;
    browserSync.init({
        server: {
            baseDir: "./_site/"
        },
        port: 4000,
        // WARNING: IF YOU FIND YOURSELF EDITING THIS FILE
        // then you may need to aslo check if the prod redict rules in .htaccess
        // work for the case your are trying to fix (use `jekyll serve`)
        middleware: [middleware.rewriteMiddleware, middleware.error404Middleware]
    });
}

function reload(cb) {
    start_server(() => {})
    browserSync.reload()
    cb();
}

function livereload(cb) {
    // All events will be watched

    fileGlops = ["**.html", "**.md", "_layouts/**", "_includes/**", "_posts/**", "_sass/**", "assets/**"]
    watch(fileGlops, { events: 'all', ignoreInitial: false }, series(copy_foundation_files, dev_build, reload));
    
    cb();
    console.log("watcher created, stop watcher with ctrl+c")
}

function defaultTask(cb) {
    console.log("test")
    cb();
}

exports.default = defaultTask
exports.build = series(copy_foundation_files, prod_build)
exports.Local_build = series(copy_foundation_files, build)
exports.watch = series(copy_foundation_files, livereload)
