# Secret Handling

Purpose: prevent API keys and credentials from leaking into VCOS memory, graphs, task systems, or public history.

## Rule

Never store real secrets in:

- Chat history.
- Obsidian notes.
- GBrain imports.
- Graphify outputs.
- ClickUp comments or task descriptions.
- Git-tracked files.

Use local `.env` files, OS keychain, provider secret stores, or deployment platform secrets.

## NVIDIA / NVCR

If an NVIDIA or NGC key is pasted into chat, treat it as compromised and rotate it before use.

Local environment shape:

```bash
NGC_API_KEY=...
NVIDIA_API_KEY=${NGC_API_KEY}
NVCR_USERNAME=$oauthtoken
NVCR_REGISTRY=nvcr.io
```

Docker login:

```bash
printf "%s" "$NGC_API_KEY" | docker login nvcr.io --username '$oauthtoken' --password-stdin
```

