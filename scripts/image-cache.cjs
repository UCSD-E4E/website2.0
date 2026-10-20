const fs = require('node:fs/promises');
const path = require('node:path');

// jekyll-resize moves referenced images from resize_temp into resize while
// rendering. Merge both generations before rotating so unused variants and
// images from interrupted builds survive, without publishing unused files.
async function prepareImageCache(root = '.') {
    const active = path.join(root, 'cache', 'resize');
    const retained = path.join(root, 'cache', 'resize_temp');
    await fs.mkdir(active, { recursive: true });
    await fs.mkdir(retained, { recursive: true });
    for (const name of await fs.readdir(retained)) {
        const destination = path.join(active, name);
        try {
            await fs.access(destination);
        } catch (error) {
            if (error.code !== 'ENOENT') throw error;
            await fs.rename(path.join(retained, name), destination);
        }
    }
    await fs.rm(retained, { recursive: true, force: true });
    await fs.rename(active, retained);
    await fs.mkdir(active);
}

module.exports = { prepareImageCache };
