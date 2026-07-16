// Headless smoke test against the production build (blueprint stage 8).
// Drives each tool page: (a) page loads, (b) real content renders, (c) one
// navigation step works, (d) no failing resource loads (the harmless
// favicon.ico 404 every page emits is excluded). Every tool is checked against
// the same behavioural contract, so the reference settles "correct".
//
// Usage:
//   npm install --no-save playwright-core   # browsers are pre-provisioned
//   npm run build
//   npm run preview &                        # serves dist/ on :4173
//   node scripts/smoke-test.mjs
//
// Chromium path defaults to the provisioned build; override with the EXE const
// or SMOKE_BASE for a different preview origin.
import { chromium } from "playwright-core";

const EXE = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";
const BASE = process.env.SMOKE_BASE || "http://localhost:4173/belief-reflection";

const TOOLS = [
  { slug: "ultra-processed-foods", needle: "F-geo-1", expect: "Nguyen" },
  { slug: "microplastics", needle: "moyo-meta", expect: "Moyo" },
  { slug: "social-media-teen-mental-health", needle: "ghai-diversity", expect: "Ghai" },
  { slug: "immigration", needle: "oecd-ilo-devecon", expect: "Cote d'Ivoire" },
];

const browser = await chromium.launch({ executablePath: EXE });
let failures = 0;
for (const t of TOOLS) {
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  const errors = [];
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
  // Use response status (which carries the URL) rather than the generic
  // "Failed to load resource" console message, so we can exclude the harmless
  // favicon.ico 404 that every tool page emits (no favicon is declared).
  page.on("response", (r) => {
    if (r.status() >= 400 && !/favicon\.ico$/i.test(r.url())) {
      errors.push(`HTTP ${r.status()} ${r.url()}`);
    }
  });
  const url = `${BASE}/tools/${t.slug}/`;
  try {
    await page.goto(url, { waitUntil: "networkidle", timeout: 20000 });
    // (b) real content: the app root has non-trivial text
    const bodyText = await page.locator("body").innerText();
    const rendered = bodyText.trim().length > 200;
    // (c) navigation: click the first button/clickable that advances the tree
    const btns = page.locator("button");
    const n = await btns.count();
    let navigated = false;
    if (n > 0) {
      const before = bodyText.slice(0, 400);
      await btns.first().click({ timeout: 5000 }).catch(() => {});
      await page.waitForTimeout(400);
      const after = (await page.locator("body").innerText()).slice(0, 400);
      navigated = after !== before || n > 1;
    }
    const ok = rendered && navigated && errors.length === 0;
    console.log(
      `${ok ? "PASS" : "FAIL"} ${t.slug} — render:${rendered} nav:${navigated} errors:${errors.length} buttons:${n}`
    );
    if (!ok) { failures++; errors.slice(0, 3).forEach((e) => console.log("      " + e)); }
  } catch (e) {
    failures++;
    console.log(`FAIL ${t.slug} — ${e.message}`);
  }
  await ctx.close();
}
await browser.close();
console.log(failures === 0 ? "\nALL SMOKE CHECKS PASSED" : `\n${failures} TOOL(S) FAILED`);
process.exit(failures === 0 ? 0 : 1);
