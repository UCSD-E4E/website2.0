// thank you chatgpt for this template for me to edit.
// I spent so much time trying to find documentation

// WARNING: IF YOU FIND YOURSELF EDITING THIS FILE
// then you may need to also check if the prod redict rules in .htaccess
// work for the case your are trying to fix (use `jekyll serve`)
const http = require('http');
const path = require('path');
const fs = require('fs');
const exp = require('constants');

// Define location of pages
const dirname = "./_site"

// Custom middleware to handle 404 errors
function error404Middleware(req, res, next) {
    const url = req.url
    fs.stat(path.join(dirname, url), (err, stats) => {
        if (!err) {
            next();
        } else {
            //console.log(url, " is missing")
            res.writeHead(301, { 'Location': "/404.html" });
            res.end();
        }
    })
}

// Utility function to get content type based on file extension
function getContentType(filePath) {
    const extname = path.extname(filePath);
    switch (extname) {
        case '.html':
            return 'text/html';
        case '.css':
            return 'text/css';
        case '.js':
            return 'text/javascript';
        default:
            return 'text/plain';
    }
}

function serveContent(filePath, res) {
    fs.readFile(filePath, (err, data) => {
        if (!err) {
            // Set appropriate Content-Type based on file extension
            const contentType = getContentType(filePath);
            res.writeHead(200, { 'Content-Type': contentType });
            res.write(data);
            res.end();
        } else {
            next();
        }
    });
}

// Custom middleware to handle trailing slashes and append .html extension
function rewriteMiddleware(req, res, next) {
    let  url = req.url
    if (url[-1] == "/") {
        url = url.splice(0, -1)
    }
    if (url == "/.html") {
        serveContent(path.join(dirname, "/index.html"), res)
        // res.writeHead(301, { 'Location': '/index.html' });
        // res.end();
        
    }
    
    const extension = path.extname(url);
    if (!extension) {
        // If the request does not have an extension add .html on it
        fs.stat(path.join(dirname, url + '.html'), (err, stats) => {
            if (!err) {
                serveContent(path.join(dirname, url + '.html'), res)
                // res.writeHead(301, { 'Location': url + '.html' });
                // res.end();
            } else {
                next();
            }
        });
    }  else {
        next();
    }
}

module.exports = {
    error404Middleware,
    rewriteMiddleware
};