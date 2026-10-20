const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const os = require('node:os');
const path = require('node:path');
const { prepareImageCache } = require('./image-cache.cjs');

test('cache survives cold, repeated, interrupted and variant-changing builds', async (t) => {
    const root = await fs.mkdtemp(path.join(os.tmpdir(), 'e4e-image-cache-'));
    t.after(() => fs.rm(root, { recursive: true, force: true }));
    const active = path.join(root, 'cache/resize');
    const retained = path.join(root, 'cache/resize_temp');
    await prepareImageCache(root);
    await fs.writeFile(path.join(active, 'original.jpg'), 'original');
    await prepareImageCache(root);
    assert.deepEqual(await fs.readdir(active), []);
    assert.equal(await fs.readFile(path.join(retained, 'original.jpg'), 'utf8'), 'original');

    // Simulate plugin reuse plus a new template-requested size, then a failed build.
    await fs.rename(path.join(retained, 'original.jpg'), path.join(active, 'original.jpg'));
    await fs.writeFile(path.join(active, 'new-size.jpg'), 'new size');
    await fs.writeFile(path.join(retained, 'unused.jpg'), 'unused');
    await prepareImageCache(root);
    assert.deepEqual((await fs.readdir(retained)).sort(), ['new-size.jpg', 'original.jpg', 'unused.jpg']);
    assert.deepEqual(await fs.readdir(active), []);

    // An interruption before rendering must not discard the entire previous cache.
    await prepareImageCache(root);
    assert.equal(await fs.readFile(path.join(retained, 'new-size.jpg'), 'utf8'), 'new size');
    assert.equal(await fs.readFile(path.join(retained, 'unused.jpg'), 'utf8'), 'unused');

    // A duplicate from recovery keeps the active generation rather than failing
    // on Windows or overwriting a newer completed output.
    await fs.writeFile(path.join(active, 'original.jpg'), 'active output');
    await prepareImageCache(root);
    assert.equal(await fs.readFile(path.join(retained, 'original.jpg'), 'utf8'), 'active output');
});
