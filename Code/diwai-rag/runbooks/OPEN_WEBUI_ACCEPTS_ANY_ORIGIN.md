default_repair: owui-cors-any-origin
decisions: 13
objectives: 3.1.3[e]
user_sees: Usually nothing. The AI chat page works normally for the owner.
means: A web site the owner visits in another tab could read answers from the AI chat page, including text from the owner's documents.
evidence: The AI chat page tells web browsers that any web site may read its answers, not only its own address.
repair: Add one setting so that only the chat page's own address may read its answers, then restart the chat page. A backup is kept first.
if_wrong: The chat page may stop answering for about 20 seconds, or longer if the restart fails. Anyone mid-conversation loses that reply.
rollback: The repair's undo puts the original start-up file back from the backup and restarts the chat page.
say_no_if: Someone is in the middle of a conversation on the AI chat page, because the restart interrupts it.
---
Status as of 2026-10-04 (DIWAI-CR-2026-10-03 §7 item 1; checked live 2026-10-03). `CORS_ALLOW_ORIGIN` is not set in `/usr/local/sbin/open-webui-start`, so Open WebUI defaults to `*`: a request with `Origin: http://evil.example` gets `access-control-allow-origin: http://evil.example` and `access-control-allow-credentials: true`. Repair `owui-cors-any-origin` adds `export CORS_ALLOW_ORIGIN=https://ai.[DOMAIN.ORG]` after the last `export` line, restarts LaunchAgent `org.diwai.open-webui`, and verifies: health 200 within 60 s, foreign origin no longer allowed, `https://ai.[DOMAIN.ORG]` still allowed, the "CORS_ALLOW_ORIGIN IS SET TO '*'" startup warning gone, and the `diwai-library` model listed. The launcher also holds `WEBUI_SECRET_KEY`, so the backup lives in the root-only run folder. Browser cookie defaults (SameSite) limit the practical exposure, which is why this is a hardening fix, not an emergency.
