# Waterloo Bike Shop redesign

Version 9 of the shop redesign: responsive storefront, category and selected product pages, workshop and booking pages, customer support, and a scroll-driven photographic-style bicycle assembly.

## Build and preview

Requires Node.js 18+; there are no npm dependencies.

```sh
npm run build
npm run preview
```

Open http://localhost:8765. Preview uses Python 3's static HTTP server. Any static server can serve `build/` instead.

`dist/` contains the editable, ready-to-host website source. `npm run build` checks all HTML file references and JavaScript syntax, then produces a clean `build/` folder. Deploy the contents of `build/` at the domain root. Nested pages require normal directory-index support; this is not a single-page application.

## Editing

- `dist/index.html`, `dist/style.css`, `dist/pages.css`: homepage and shared page design.
- `dist/app.js`, `dist/site.js`: homepage and storefront interactions.
- `dist/bicycle-assembly.js`: scroll assembly, arrows, captions and manual controls.
- `dist/realistic-bicycle.js`: complete photographic-style component image placement.
- `dist/assets/bicycle-photo-parts-v8.png`: alpha-transparent component atlas.
- `tools/place-photo-parts.py`: regenerates component placements from measured mounts.
- `tools/build-pages.py`: regenerates category, product and informational pages from `dist/catalog.json`.

Commit the regenerated `dist/` files after changing generators. The dated catalog snapshot contains 438 selected products; it is not a live inventory feed.

## Integrations and artwork

Purchases, stock availability and secure customer accounts continue on the original Waterloo Bike Shop store. Booking uses its existing HubTiger service. This repository does not include a commerce backend or payment credentials.

The bicycle anatomy uses AI-reconstructed photographic-style components consistently throughout assembly. It is educational artwork, not an exact manufacturer specification image. Product and lifestyle images retained from the original shop remain subject to their owners' rights. Bundled GSAP and Anatomy files retain their upstream license terms.

Netlify is configured through `netlify.toml` to run the build command and publish `build/`.

See `UPDATE-V9.md` for the latest motion changes and `UPDATE-V8.md` for the photographic anatomy changes and earlier update notes for the page coverage.
