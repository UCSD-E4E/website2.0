const util = require('node:util');
const exec = util.promisify(require('node:child_process').exec);
const { watch, series } = require('gulp');

async function build(cb) {
    const { stdout, stderr } = await exec("bundle exec jekyll build");
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);

    cb();
}

function livereload(cb) {
    // All events will be watched

    fileGlops = ["**.html", "**.md", "_layouts/**", "_includes/**", "_posts/**", "_sass/**", "assets/**"]
    watch(fileGlops, { events: 'all', ignoreInitial: true }, async function(cb) {
        console.log("start new build!!!")
        await build(cb)
    });
    cb();
    console.log("watcher created, stop watcher with ctrl+c")
}

function defaultTask(cb) {
    console.log("test")
    cb();
}

exports.default = defaultTask
exports.build = build
exports.watch = livereload
