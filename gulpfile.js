


var spawn = require('cross-spawn'); 
const { src, dest , series} = require('gulp');
const fs   = require('fs');
const fsPromises = require('fs').promises; 

async function create_command(command_str) {
    var command = command_str.split(" ")
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
    var value = await new Promise( (resolve) => {
        child.on('close', resolve)
        return "test"
    })
    if (value != 0) {
        throw new Error(`FAILED TO RUN ${command_str} \n see above for stacktrace`);
    }
    console.log(value)
}

function process_CLI(cb) {
    // fetch command line arguments
    //https://www.sitepoint.com/pass-parameters-gulp-tasks/
    const arg = (argList => {
        let arg = {}, a, opt, thisOpt, curOpt;
        for (a = 0; a < argList.length; a++) {
            thisOpt = argList[a].trim();
            //was opt === thisOpt
            //updated code will always store following opt
            if (curOpt !== null) {
                // argument value
                if (curOpt) arg[curOpt] = thisOpt;
                curOpt = null;
            }
            else {
                // argument name
                opt = thisOpt.replace(/^\-+/, '');
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
    await create_command("bundle update")
    cb()
}

function copy_foundation_files(cb) {
    //move foundation css to build
    //note you may need to exclude these files in config.yml 
    foundation = [
        "./node_modules/foundation-sites/dist/css/foundation.min.css",
        "./node_modules/foundation-sites/dist/css/foundation.min.css.map",
        "./node_modules/foundation-sites/dist/js/foundation.min.js",
        "./node_modules/foundation-sites/dist/js/foundation.min.js.map"
    ]
   
    return src(foundation).pipe(dest('cache')) 
}

async function handle_cache_updates(cb) {
    // delete temp cache if it exists, otherwise add a new temp cache
    // The idea is we delete the temp cache each build, temp cache contains unused images
    const temp_dir = "./cache/resize_temp"
    const dir = "./cache/resize"

    // Remove the temp directory, files here before build should have been taken
    // out by the user 
    if(fs.existsSync(temp_dir)) {
        await fsPromises.rmdir(temp_dir, {"recursive": true})
        //rimraf.sync(temp_dir)
    }

    // Make sure resize exists if it doesn't already
    if(!fs.existsSync(dir)) {
        fs.mkdirSync(dir)
    }
    
    // Move all files in resize (the stuff we ideally want to keep)
    // into resize_temp to actually check during jekyll build if files should be kept
    fs.renameSync(dir, temp_dir);
    fs.mkdirSync(dir)
    return cb
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
    console.log(arg)
    if ("j" in arg) {
        await create_command("bundle exec jekyll serve " + arg["j"])
    } else {
        await create_command("bundle exec jekyll serve --livereload")
    }
    cb();
}

async function defaultTask(cb) {
    console.log("Testing Gulp is Working!")
    await create_command("bundle exec jekyll build")
    cb();
}

exports.default = handle_cache_updates
exports.build = series(update_packages, handle_cache_updates, copy_foundation_files, build)
exports.watch = series(update_packages, handle_cache_updates, copy_foundation_files, dev_build)
