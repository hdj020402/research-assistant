"""Translation: GLM-4.7-Flash → translators lib (Bing/Alibaba/Sogou) → Haiku fallback."""
import logging
import os
import requests

log = logging.getLogger(__name__)

# Track which methods have failed this session (skip on subsequent calls)
_disabled: set[str] = set()


def translate(text: str, source_lang: str = "en", target_lang: str = "zh") -> str:
    """
    Translate text with fallback chain:
      1. GLM-4.7-Flash (free LLM, best quality)
      2. translators lib: Bing → Alibaba → Sogou
      3. Return empty string → caller falls back to Haiku

    Returns translated text, or empty string on complete failure.
    """
    if not text or not text.strip():
        return ""

    # 1. GLM-4.7-Flash
    if "glm" not in _disabled:
        try:
            result = _translate_glm(text, source_lang, target_lang)
            if result:
                return result
        except Exception as e:
            log.warning(f"GLM translation failed, disabling for session: {e}")
            _disabled.add("glm")

    # 2. translators library (3 engines fallback)
    for engine in ("bing", "alibaba", "sogou"):
        if engine in _disabled:
            continue
        try:
            result = _translate_lib(text, engine, source_lang, target_lang)
            if result:
                return result
        except Exception as e:
            log.warning(f"translators/{engine} failed, disabling for session: {e}")
            _disabled.add(engine)

    # 3. All failed → empty string → Haiku fallback in claude_processor.py
    return ""


def _translate_glm(text: str, source_lang: str, target_lang: str) -> str:
    """Translate using GLM-4.7-Flash via OpenAI-compatible API."""
    api_key = os.environ.get("ZHIPUAI_API_KEY", "")
    if not api_key:
        return ""

    resp = requests.post(
        "https://open.bigmodel.cn/api/paas/v4/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "glm-4.7-flash",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a professional academic translator. "
                    "Translate the given English text to Chinese. "
                    "Output ONLY the translation, nothing else.",
                },
                {"role": "user", "content": text},
            ],
            "max_tokens": 4096,
            "temperature": 0.1,
        },
        timeout=30,
    )
    resp.raise_for_status()

    choices = resp.json().get("choices", [])
    if choices:
        return choices[0]["message"]["content"].strip()
    return ""


def _translate_lib(
    text: str, engine: str, source_lang: str, target_lang: str
) -> str:
    """Translate using the translators library."""
    import translators as ts

    result = ts.translate_text(
        text,
        translator=engine,
        from_language=source_lang,
        to_language=target_lang,
    )
    return result if isinstance(result, str) else ""
