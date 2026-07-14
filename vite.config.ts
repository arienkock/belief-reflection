import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { readdirSync, existsSync } from "node:fs";
import { resolve } from "node:path";

// Every tools/<slug>/index.html becomes its own build entry at /tools/<slug>/.
// Adding a new tool directory with an index.html is enough — no config edits needed.
const toolsDir = resolve(__dirname, "tools");
const toolEntries = Object.fromEntries(
  readdirSync(toolsDir, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .filter((slug) => existsSync(resolve(toolsDir, slug, "index.html")))
    .map((slug) => [slug, resolve(toolsDir, slug, "index.html")])
);

export default defineConfig({
  // Served at https://<user>.github.io/belief-reflection/ — update if the repo is renamed.
  base: "/belief-reflection/",
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"),
        ...toolEntries,
      },
    },
  },
});
