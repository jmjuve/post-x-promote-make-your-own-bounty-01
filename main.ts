// A working post-x-promote-make-your-own-bounty-01 entry (Node 22, standard
// library only): it copies POST.json from the repository root to
// /output/POST.json, where the gate reads it. That is all the program has to
// do. The entry is the post itself: one post of your own on X that quotes
// make.fun's make-your-own-bounty post
// (https://x.com/makefunai/status/2124915864336236646) or links to it, with
// a photo of its own attached, make.fun or the @makefunai tag and your play
// code in its text; POST.json names the post, and the house reads its
// replies, reposts and quotes from X. Nothing this program writes about the
// post is scored.
//
// The POST.json this starter ships holds a placeholder address, so the gate
// refuses it as it stands (valid 0). Replace it with your post's address
// before you submit.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

// Entry note (post-x-promote-make-your-own-bounty-01): this program's only
// job is to hand POST.json to the gate. The photo lives in the X post
// POST.json points at; nothing here renders, fetches, or judges it. The
// post quotes make.fun's make-your-own-bounty post and carries the
// entrant's play code in its text.
import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
// Refuse to hand the gate an empty address: a copied POST.json must name a post.
const postJson = readFileSync(join(OUTPUT_DIR, 'POST.json'), 'utf8').trim();
if (!postJson) {
  console.error('POST.json copied but empty');
  process.exit(1);
}
// Refuse a placeholder or malformed address: the url must be an X post's
// address (x.com or twitter.com, /status/<digits> or /i/web/status/<digits>,
// an optional query or fragment is read past). A placeholder that slipped
// through would be refused by the gate as invalid, so fail here instead.
let postUrl = '';
try {
  postUrl = (JSON.parse(postJson) as { url?: unknown }).url as string;
} catch {
  console.error('POST.json is not valid JSON');
  process.exit(1);
}
if (
  typeof postUrl !== 'string' ||
  !/^https?:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/(?:i\/web\/status\/\d+|[^/]+\/status\/\d+)\/?([?#].*)?$/.test(postUrl)
) {
  console.error(`POST.json does not name an X post: ${postUrl}`);
  process.exit(1);
}
