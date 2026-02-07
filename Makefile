.PHONY: sync build dev clean

# Regenerate the examples.json from source files
sync:
	python3 scripts/sync_examples.py

# Verify all scripts with UV
verify:
	python3 scripts/verify_examples.py

# Build the SvelteKit app (includes sync)
build: sync
	cd webapp && npm install && npm run build
	touch webapp/build/.nojekyll

# Run the development server (includes sync)
dev:
	cd webapp && npm install && npm run dev

# Clean up build artifacts
clean:
	rm -rf webapp/build webapp/.svelte-kit webapp/node_modules
	rm -f webapp/src/data/examples.json
