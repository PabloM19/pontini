import { cpSync, mkdirSync, readdirSync, rmSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const output = join(root, 'dist');
const pages = readdirSync(root).filter(file => file.endsWith('.html'));
if (!pages.includes('index.html')) throw new Error('Missing index.html');

rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });
for (const file of [...pages, 'styles.css', 'app.js', 'assets']) {
  cpSync(join(root, file), join(output, file), { recursive: true });
}
console.log(`Built ${pages.length} static pages and their assets in dist/`);
