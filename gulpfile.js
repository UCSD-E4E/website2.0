const util = require('node:util');
const fs = require('fs');
const middleware = require('./middleware');

// const exec = util.promisify(require('node:child_process').exec);
var spawn = require('cross-spawn'); //= require('child_process').spawn= require('cross-spawn'); ;

const { watch, src, dest , series} = require('gulp');
var browserSync = require('browser-sync').create();

async function create_command(command) {
    command = command.split(" ")
    console.log(command[0], command.slice(1))
    const child = spawn(command[0], command.slice(1));

    //Handle stdout stream
    child.stdout.setEncoding('utf8');
    child.stdout.on('data', function(data) {
        console.log(data.toString());
    });

    //errors
    child.stderr.setEncoding('utf8');
    child.stderr.on('data', (data) => {
        console.error(`${data}`);
    });

    //wait until child closes to continue
    await new Promise( (resolve) => {
        child.on('close', resolve)
    })
}

function process_CLI(cb) {
    // fetch command line arguments
    //https://www.sitepoint.com/pass-parameters-gulp-tasks/
    const arg = (argList => {
        let arg = {}, a, opt, thisOpt, curOpt;
        for (a = 0; a < argList.length; a++) {
            thisOpt = argList[a].trim();
            opt = thisOpt.replace(/^\-+/, '');
            if (opt === thisOpt) {
                // argument value
                if (curOpt) arg[curOpt] = opt;
                curOpt = null;
            }
            else {
                // argument name
                curOpt = opt;
                arg[curOpt] = true;
            }
        }
    
        return arg;
    
    })(process.argv);

    //testing command line
    if (cb != null) {
        console.log(arg)
        cb()
    } else {
        return arg
    }
}

async function update_packages(cb) {
    await create_command("npm ci")
    await create_command("bundle install")
    cb()
}

function copy_foundation_files(cb) {
    //move foundation css to build
    //note you may need to exclude these files in config.yml 
    foundation = [
        "./node_modules/foundation-sites/dist/css/foundation.min.css",
        "./node_modules/foundation-sites/dist/js/foundation.min.js"
    ]
   
    return src(foundation).pipe(dest('cache')) 
}



async function build(cb) {
    var arg = process_CLI()
    if ("j" in arg) {
        await create_command("bundle exec jekyll build " + arg["j"])
    } else {
        await create_command("bundle exec jekyll build --config _config.yml")
    }
    cb();
}

async function dev_build(cb) {
    var arg = process_CLI()
    if ("j" in arg) {
        await create_command("bundle exec jekyll build " + arg["j"])
    } else {
        await create_command("bundle exec jekyll build --config _config.yml,_local_config.yml")
    }
    cb();
}


//ASSUMES THAT SERVER CANNOT GO DOWN AS LONG AS GULP IS WATCHING
let has_started = false;
function start_server(cb) {
    if (has_started) {
        return;
        cb();
    }

    has_started = true;
    browserSync.init({
        server: {
            baseDir: "./_site/"
        },
        port: 4000,
        online: false,
        host: "localhost",

        // WARNING: IF YOU FIND YOURSELF EDITING THIS FILE
        // then you may need to aslo check if the prod redict rules in .htaccess
        // work for the case your are trying to fix (use `jekyll serve`)
        middleware: [middleware.rewriteMiddleware, middleware.error404Middleware]
    });
    cb();
}

function reload(cb) {
    start_server(() => {})
    browserSync.reload()
    cb();
}

function livereload(cb) {
    // All events will be watched
    fileGlops = [
        "_bibliography/**", "_data/**", "_includes/**",
        "_layouts/**", "_posts/**", "_sass/**", "assets/**",
        "projects/**", "**.html", "**.md", "**.markdown",   
    ]
    watch(fileGlops, { events: 'all', ignoreInitial: false }, series(copy_foundation_files, dev_build, reload));
    
    cb();
    console.log("watcher created, stop watcher with ctrl+c")
}

async function defaultTask(cb) {
    console.log("Testing Gulp is Working!")
    await create_command("bundle exec jekyll build")
    cb();
}

exports.default = defaultTask
exports.build = series(build, copy_foundation_files)
exports.watch = series(update_packages, livereload)